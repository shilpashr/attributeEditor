# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from api_server.common_rdm.base_rdm import Model
from api_server import util


class AttributeTags(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self):  # noqa: E501
        """AttributeTags - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'AttributeTags':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AttributeTags of this AttributeTags.  # noqa: E501
        :rtype: AttributeTags
        """
        return util.deserialize_model(dikt, cls)