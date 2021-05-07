# coding: utf-8

from typing import List

from kgea.server.web_services.models.base_model_ import Model
from kgea.server.web_services import util


class KgeFileSetStatus(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, status: str=None, errors: List[str]=None):
        """KgeFileSetStatus - a model defined in OpenAPI

        :param status: The status of this KgeFileSetStatus.
        :param errors: The errors of this KgeFileSetStatus.
        """
        self.openapi_types = {
            'status': str,
            'errors': List[str]
        }

        self.attribute_map = {
            'status': 'status',
            'errors': 'errors'
        }

        self._status = status
        self._errors = errors

    @classmethod
    def from_dict(cls, dikt: dict) -> 'KgeFileSetStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The KgeFileSetStatus of this KgeFileSetStatus.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def status(self):
        """Gets the status of this KgeFileSetStatus.

        KGE File Set status code, one of 'processing', 'validated' or 'error'.

        :return: The status of this KgeFileSetStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this KgeFileSetStatus.

        KGE File Set status code, one of 'processing', 'validated' or 'error'.

        :param status: The status of this KgeFileSetStatus.
        :type status: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status

    @property
    def errors(self):
        """Gets the errors of this KgeFileSetStatus.

        A list of error status messages with an 'error' status code.

        :return: The errors of this KgeFileSetStatus.
        :rtype: List[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this KgeFileSetStatus.

        A list of error status messages with an 'error' status code.

        :param errors: The errors of this KgeFileSetStatus.
        :type errors: List[str]
        """

        self._errors = errors
