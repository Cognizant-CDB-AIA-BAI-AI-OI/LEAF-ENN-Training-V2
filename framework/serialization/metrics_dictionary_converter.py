
import copy

from past.builtins import basestring

import numpy as np

from servicecommon.serialization.prep.pass_through_dictionary_converter \
    import PassThroughDictionaryConverter


class MetricsDictionaryConverter(PassThroughDictionaryConverter):
    """
    A DictionaryConverter implementation which knows how to clean up
    a metrics dictionary for serialization by filtering out
    numpy types that might creep into the metrics.
    """

    def to_dict(self, obj):
        """
        :param obj: The object to be converted into a dictionary
        :return: A data-only dictionary that represents all the data for
                the given object, either in primitives
                (booleans, ints, floats, strings), arrays, or dictionaries.
                If obj is None, then the returned dictionary should also be
                None.  If obj is not the correct type, it is also reasonable
                to return None.
        """
        metrics = copy.deepcopy(obj)

        # Clean up the metrics from having any numpy business
        # JSON will not convert these correctly.
        new_metrics = self.cleanup_metrics(metrics)

        # Make any evaluation error tracebacks pretty
        execution = new_metrics.get('execution', None)
        if execution is not None:
            eval_error = execution.get('eval_error', None)
            if eval_error is not None and \
                isinstance(eval_error, basestring):

                # Break up any traceback as an array of lines
                execution['eval_error'] = eval_error.splitlines()

        return new_metrics


    def is_numpy_type(self, value):
        """
        :param value: The value to inspect
        :return: True if the object came from numpy. False otherwise.
        """
        return type(value).__module__ == np.__name__


    def cleanup_metrics(self, datum):
        """
        Clean up a specific metrics field.
        Intended to be called recursively.
        Handles deep inspection of scalars, lists, tuples, and dicts.

        :param datum: The datum to inspect
        """

        new_datum = datum

        if isinstance(datum, dict):
            new_datum = {}
            for key, value in datum.items():
                new_datum[key] = self.cleanup_metrics(value)

        elif isinstance(datum, list):
            new_datum = [self.cleanup_metrics(value) for value in datum]

        elif isinstance(datum, tuple):
            new_datum = tuple([self.cleanup_metrics(value) for value in datum])

        elif self.is_numpy_type(datum):
            new_datum = datum.item()

        return new_datum
