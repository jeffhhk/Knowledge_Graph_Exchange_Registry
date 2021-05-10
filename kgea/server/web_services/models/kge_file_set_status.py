# coding: utf-8

from typing import List

from kgea.server.web_services.models.base_model_ import Model
from kgea.server.web_services.models.kge_file import KgeFile
from kgea.server.web_services.models.kge_file_set_status_code import KgeFileSetStatusCode
from kgea.server.web_services import util


class KgeFileSetStatus(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, kg_id: str=None, kg_version: str=None, status: KgeFileSetStatusCode=None, files: List[KgeFile]=None):
        """KgeFileSetStatus - a model defined in OpenAPI

        :param kg_id: The kg_id of this KgeFileSetStatus.
        :param kg_version: The kg_version of this KgeFileSetStatus.
        :param status: The status of this KgeFileSetStatus.
        :param files: The files of this KgeFileSetStatus.
        """
        self.openapi_types = {
            'kg_id': str,
            'kg_version': str,
            'status': KgeFileSetStatusCode,
            'files': List[KgeFile]
        }

        self.attribute_map = {
            'kg_id': 'kg_id',
            'kg_version': 'kg_version',
            'status': 'status',
            'files': 'files'
        }

        self._kg_id = kg_id
        self._kg_version = kg_version
        self._status = status
        self._files = files

    @classmethod
    def from_dict(cls, dikt: dict) -> 'KgeFileSetStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The KgeFileSetStatus of this KgeFileSetStatus.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def kg_id(self):
        """Gets the kg_id of this KgeFileSetStatus.

        Identifier of the knowledge graph that owns the file set.

        :return: The kg_id of this KgeFileSetStatus.
        :rtype: str
        """
        return self._kg_id

    @kg_id.setter
    def kg_id(self, kg_id):
        """Sets the kg_id of this KgeFileSetStatus.

        Identifier of the knowledge graph that owns the file set.

        :param kg_id: The kg_id of this KgeFileSetStatus.
        :type kg_id: str
        """

        self._kg_id = kg_id

    @property
    def kg_version(self):
        """Gets the kg_version of this KgeFileSetStatus.

        Version identifier of the file set.

        :return: The kg_version of this KgeFileSetStatus.
        :rtype: str
        """
        return self._kg_version

    @kg_version.setter
    def kg_version(self, kg_version):
        """Sets the kg_version of this KgeFileSetStatus.

        Version identifier of the file set.

        :param kg_version: The kg_version of this KgeFileSetStatus.
        :type kg_version: str
        """

        self._kg_version = kg_version

    @property
    def status(self):
        """Gets the status of this KgeFileSetStatus.


        :return: The status of this KgeFileSetStatus.
        :rtype: KgeFileSetStatusCode
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this KgeFileSetStatus.


        :param status: The status of this KgeFileSetStatus.
        :type status: KgeFileSetStatusCode
        """

        self._status = status

    @property
    def files(self):
        """Gets the files of this KgeFileSetStatus.

        Annotated list of files within a given file set.

        :return: The files of this KgeFileSetStatus.
        :rtype: List[KgeFile]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this KgeFileSetStatus.

        Annotated list of files within a given file set.

        :param files: The files of this KgeFileSetStatus.
        :type files: List[KgeFile]
        """

        self._files = files
