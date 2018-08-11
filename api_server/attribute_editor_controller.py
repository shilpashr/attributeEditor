import connexion
import six

from api_server.common_rdm.attribute import Attribute  # noqa: E501
from api_server.common_rdm.attribute_data_type import AttributeDataType  # noqa: E501
from api_server.common_rdm.attribute_details import AttributeDetails  # noqa: E501
from api_server.common_rdm.attribute_tags import AttributeTags  # noqa: E501
from api_server.common_rdm.attribute_type import AttributeType  # noqa: E501
from api_server import util


def add_attribute_definition(body):  # noqa: E501
    """Add New Attribute

    Add attribute # noqa: E501

    :param body: Attribute definition that needs to be added
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = Attribute.from_dict(connexion.request.get_json())  # noqa: E501
    return 'sucess!'


def get_attribute_data_type():  # noqa: E501
    """Gets list of available attribute data type

    API to get a list of attribute tata ype available in the system # noqa: E501


    :rtype: List[AttributeDataType]
    """
    return ["str","int","bool"]


def get_attribute_definition():  # noqa: E501
    """Gets list of available attributes

    API to get a list of attribute definitions available in the system # noqa: E501


    :rtype: List[Attribute]
    """
    result = [
        {"name": "firstName", "type": "SingleValue", "dataType": "str", "description": "first name of the consumer",
         "path": "/", "tags": ["name", "title"]},
        {"name": "lastName", "type": "SingleValue", "dataType": "str", "description": "first name of the consumer",
         "path": "/", "tags": ["name", "title"]},
        {"name": "Address", "type": "SingleValue", "dataType": "address", "description": "address of the consumer",
         "path": "/", "tags": ["primary", "location"]},
        {"name": "age", "type": "SingleValue", "dataType": "str", "description": "age of the consumer", "path": "/",
         "tags": [""]},
        {"name": "sportsLover", "type": "SingleValue", "dataType": "str", "description": "sports lover", "path": "/",
         "tags": [""]},
        {"name": "title", "type": "SingleValue", "dataType": "str", "description": "title of the consumer", "path": "/",
         "tags": [""]},
        {"name": "emailId", "type": "SingleValue", "dataType": "str", "description": "email id of the consumer", "path": "/",
         "tags": [""]}

    ]
    return result


def get_attribute_tags():  # noqa: E501
    """Gets list of available attribute tags

    API to get a list of attribute tags available in the system # noqa: E501


    :rtype: List[AttributeTags]
    """
    return ["name","title","age","address"]


def get_attribute_type():  # noqa: E501
    """Gets list of available attribute type

    API to get a list of attribute type available in the system # noqa: E501


    :rtype: List[AttributeType]
    """
    return ["SingleValue","ArrayValue"]


def modify_attribute_definition(body):  # noqa: E501
    """Attribute modification , only description and tags are supported.

    Modify attribute definition # noqa: E501

    :param body: Attribute definition needs to modify
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = AttributeDetails.from_dict(connexion.request.get_json())  # noqa: E501
    return 'sucess!'
