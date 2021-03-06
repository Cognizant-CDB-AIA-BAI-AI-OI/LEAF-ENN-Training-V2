
from past.builtins import basestring

from servicecommon.fitness.comparator import Comparator
from servicecommon.fitness.metrics_provider import MetricsProvider
from servicecommon.fitness.number_comparator import NumberComparator

from servicecommon.parsers.field_extractor import FieldExtractor


class MetricsBasedIndividualComparator(Comparator):
    """
    A comparator that compares metrics_providers based on a given metric.
    """

    def __init__(self, metric_name, raise_on_problems=True):
        """
        Creates a comparator that compares MetricsProviders based on the the
        value of the passed metric.

        :param metric_name: the name of the metric to use to compare 2
            MetricsProviders.
        :param raise_on_problems: True (default) if comparison problems
            are allowed to raise exceptions.
            False will always return -1 when there are comparison issues.
            While this behavior isn't necessarily desirable, it avoids
            problems where this comparator is used in services.
        """
        self._metric_name = metric_name
        self._raise_on_problems = raise_on_problems
        self._field_extractor = FieldExtractor()
        self._number_comparator = NumberComparator()


    def compare(self, obj1, obj2):
        """
        :param obj1: The first MetricsProvider offered for comparison
        :param obj2: The second MetricsProvider offered for comparison
        :return:  A negative integer, zero, or a positive integer as the first
                argument is less than, equal to, or greater than the second.
        """

        metrics_provider_1 = obj1
        metrics_provider_2 = obj2

        metric_1 = self.get_metric_value(metrics_provider_1)
        metric_2 = self.get_metric_value(metrics_provider_2)

        if metric_1 is None or metric_2 is None or \
           isinstance(metric_1, int) or isinstance(metric_1, float):

            # Int and Float and None are supported in here
            return self._number_comparator.compare(metric_1, metric_2)


        # String and Boolean are supported here.
        # Unfortunately, Record.getField() returns an Object so we have to cast
        retval = -1
        if isinstance(metric_1, basestring):
            str2 = str(metric_2)
            if metric_1 < str2:
                retval = -1
            elif metric_1 > str2:
                retval = 1
            else:
                retval = 0

        elif isinstance(metric_1, bool):
            if metric_1 == bool(metric_2):
                retval = 0
            elif metric_1:
                retval = 1
            else:
                retval = -1

        elif not self._raise_on_problems:
            retval = -1
        else:
            raise ValueError("Cannot compare metric type {0}".format(
                            type(metric_1).__name__))
        return retval


    def get_metric_value(self, metrics_provider):
        """
        Returns the value of this selector's metric for the passed
        metrics_provider.

        :param metrics_provider: the metrics_provider for which to
            retrieve the metric value. Can be a metrics dictionary
            in and of itself as well.
        :return: the value of the of the metric field
        """

        metric = None

        # Allow a MetricsProvider, or a metrics dict itself
        metrics = metrics_provider
        if isinstance(metrics_provider, MetricsProvider):
            metrics = metrics_provider.get_metrics()

        if metrics is not None:
            metric = self._field_extractor.get_field(metrics, self._metric_name)

        return metric
