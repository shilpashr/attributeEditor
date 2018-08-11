# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from api_server.common_rdm.base_rdm import Model
from api_server import util


class AttributeDetails(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, description: str=None, tags: List[str]=None):  # noqa: E501
        """AttributeDetails - a model defined in Swagger

        :param name: The name of this AttributeDetails.  # noqa: E501
        :type name: str
        :param description: The description of this AttributeDetails.  # noqa: E501
        :type description: str
        :param tags: The tags of this AttributeDetails.  # noqa: E501
        :type tags: List[str]
        """
        self.swagger_types = {
            'name': str,
            'description': str,
            'tags': List[str]
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'tags': 'tags'
        }

        self._name = name
        self._description = description
        self._tags = tags

    @classmethod
    def from_dict(cls, dikt) -> 'AttributeDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AttributeDetails of this AttributeDetails.  # noqa: E501
        :rtype: AttributeDetails
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this AttributeDetails.


        :return: The name of this AttributeDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this AttributeDetails.


        :param name: The name of this AttributeDetails.
        :type name: str
        """

        self._name = name

    @property
    def description(self) -> str:
        """Gets the description of this AttributeDetails.

        first name of the consumer  # noqa: E501

        :return: The description of this AttributeDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this AttributeDetails.

        first name of the consumer  # noqa: E501

        :param description: The description of this AttributeDetails.
        :type description: str
        """

        self._description = description

    @property
    def tags(self) -> List[str]:
        """Gets the tags of this AttributeDetails.

        A Tag which refers the attribute, it can be a list of tags.  # noqa: E501

        :return: The tags of this AttributeDetails.
        :rtype: List[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags: List[str]):
        """Sets the tags of this AttributeDetails.

        A Tag which refers the attribute, it can be a list of tags.  # noqa: E501

        :param tags: The tags of this AttributeDetails.
        :type tags: List[str]
        """

        self._tags = tags
