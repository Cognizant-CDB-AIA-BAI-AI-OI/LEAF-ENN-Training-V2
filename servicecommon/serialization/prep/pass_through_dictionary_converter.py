
from servicecommon.serialization.interface.dictionary_converter \
    import DictionaryConverter


class PassThroughDictionaryConverter(DictionaryConverter):
    """
    DictionaryConverter implementation which always returns
    the original object for to_dict() (assumes it's a dictionary)
    and returns the dictionary for from_dict().
    """

    def __init__(self, allow_restore_none=True):
        """
        Constructor.

        :param allow_restore_none: When True (the default), None values are
                allowed to come back from restore() when there is no dictionary
                as input.  When False, the same case has restore() returning
                an empty dictionary.
        """
        self.allow_restore_none = allow_restore_none


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

        return obj


    def from_dict(self, obj_dict):
        """
        :param obj_dict: The data-only dictionary to be converted into an object
        :return: An object instance created from the given dictionary.
                By default, if obj_dict is None, then the returned object will
                also be None.  If obj_dict is not the correct type, it is also
                reasonable to return None.  However, if allow_restore_none is
                False, then these None cases will return an empty dictionary.
        """
        if obj_dict is None or \
            not isinstance(obj_dict, dict):

            obj_dict = None
            if not self.allow_restore_none:
                obj_dict = {}

        return obj_dict
