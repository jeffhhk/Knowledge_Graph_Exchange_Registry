# coding: utf-8

from kgea.server.web_services.models.base_model_ import Model
from kgea.server.web_services import util


class UploadProgressToken(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, upload_token: str=None, current_position: int=0, end_position: int=0):
        """UploadProgressToken - a model defined in OpenAPI

        :param upload_token: The upload_token of this UploadProgressToken.
        :param current_position: The current_position of this UploadProgressToken.
        :param end_position: The end_position of this UploadProgressToken.
        """
        self.openapi_types = {
            'upload_token': str,
            'current_position': int,
            'end_position': int
        }

        self.attribute_map = {
            'upload_token': 'upload_token',
            'current_position': 'current_position',
            'end_position': 'end_position'
        }

        self._upload_token = upload_token
        self._current_position = current_position
        self._end_position = end_position

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UploadProgressToken':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UploadProgressToken of this UploadProgressToken.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def upload_token(self):
        """Gets the upload_token of this UploadProgressToken.

        Upload token associated with a given uploading file.

        :return: The upload_token of this UploadProgressToken.
        :rtype: str
        """
        return self._upload_token

    @upload_token.setter
    def upload_token(self, upload_token):
        """Sets the upload_token of this UploadProgressToken.

        Upload token associated with a given uploading file.

        :param upload_token: The upload_token of this UploadProgressToken.
        :type upload_token: str
        """
        if upload_token is None:
            raise ValueError("Invalid value for `upload_token`, must not be `None`")

        self._upload_token = upload_token

    @property
    def current_position(self):
        """Gets the current_position of this UploadProgressToken.

        Number of bytes uploaded so far.

        :return: The current_position of this UploadProgressToken.
        :rtype: int
        """
        return self._current_position

    @current_position.setter
    def current_position(self, current_position):
        """Sets the current_position of this UploadProgressToken.

        Number of bytes uploaded so far.

        :param current_position: The current_position of this UploadProgressToken.
        :type current_position: int
        """
        if current_position is None:
            raise ValueError("Invalid value for `current_position`, must not be `None`")

        self._current_position = current_position

    @property
    def end_position(self):
        """Gets the end_position of this UploadProgressToken.

        Total expected bytes to be uploaded.

        :return: The end_position of this UploadProgressToken.
        :rtype: int
        """
        return self._end_position

    @end_position.setter
    def end_position(self, end_position):
        """Sets the end_position of this UploadProgressToken.

        Total expected bytes to be uploaded.

        :param end_position: The end_position of this UploadProgressToken.
        :type end_position: int
        """
        if end_position is None:
            raise ValueError("Invalid value for `end_position`, must not be `None`")

        self._end_position = end_position
