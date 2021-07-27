# coding: utf-8

from typing import List, Dict, Type

from kgea.server.web_services.models.base_model_ import Model
from kgea.server.web_services import util


class KgeFileSetEntry(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, versions: List[str]=None):
        """KgeFileSetEntry - a model defined in OpenAPI

        :param name: The name of this KgeFileSetEntry.
        :param versions: The versions of this KgeFileSetEntry.
        """
        self.openapi_types = {
            'name': str,
            'versions': List[str]
        }

        self.attribute_map = {
            'name': 'name',
            'versions': 'versions'
        }

        self._name = name
        self._versions = versions

    @classmethod
    def from_dict(cls, dikt: dict) -> 'KgeFileSetEntry':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The KgeFileSetEntry of this KgeFileSetEntry.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this KgeFileSetEntry.

        Human readable KGE File Set name ('kg_name')

        :return: The name of this KgeFileSetEntry.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this KgeFileSetEntry.

        Human readable KGE File Set name ('kg_name')

        :param name: The name of this KgeFileSetEntry.
        :type name: str
        """

        self._name = name

    @property
    def versions(self):
        """Gets the versions of this KgeFileSetEntry.

        List of versions ('fileset_version') of a KGE File Set

        :return: The versions of this KgeFileSetEntry.
        :rtype: List[str]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this KgeFileSetEntry.

        List of versions ('fileset_version') of a KGE File Set

        :param versions: The versions of this KgeFileSetEntry.
        :type versions: List[str]
        """
        if versions is not None and len(versions) < 1:
            raise ValueError("Invalid value for `versions`, number of items must be greater than or equal to `1`")

        self._versions = versions
