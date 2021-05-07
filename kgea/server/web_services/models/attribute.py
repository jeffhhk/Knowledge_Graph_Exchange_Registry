# coding: utf-8

from kgea.server.web_services.models.base_model_ import Model
from kgea.server.web_services import util


class Attribute(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type: str=None, value: str=None):
        """Attribute - a model defined in OpenAPI

        :param type: The type of this Attribute.
        :param value: The value of this Attribute.
        """
        self.openapi_types = {
            'type': str,
            'value': str
        }

        self.attribute_map = {
            'type': 'type',
            'value': 'value'
        }

        self._type = type
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Attribute':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Attribute of this Attribute.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self):
        """Gets the type of this Attribute.

        Type of the metadata attribute, from the Translator Registry metadata dictionary.

        :return: The type of this Attribute.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Attribute.

        Type of the metadata attribute, from the Translator Registry metadata dictionary.

        :param type: The type of this Attribute.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def value(self):
        """Gets the value of this Attribute.

        Value of the attribute, encoded as a string.

        :return: The value of this Attribute.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Attribute.

        Value of the attribute, encoded as a string.

        :param value: The value of this Attribute.
        :type value: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")

        self._value = value
