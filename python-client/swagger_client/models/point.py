# coding: utf-8

"""
    Betaface API 2.0

    Betaface face recognition API.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Point(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'x': 'float',
        'y': 'float',
        'type': 'int',
        'name': 'str'
    }

    attribute_map = {
        'x': 'x',
        'y': 'y',
        'type': 'type',
        'name': 'name'
    }

    def __init__(self, x=None, y=None, type=None, name=None):  # noqa: E501
        """Point - a model defined in Swagger"""  # noqa: E501

        self._x = None
        self._y = None
        self._type = None
        self._name = None
        self.discriminator = None

        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name

    @property
    def x(self):
        """Gets the x of this Point.  # noqa: E501

        x coordinate of the face point in pixels.  # noqa: E501

        :return: The x of this Point.  # noqa: E501
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this Point.

        x coordinate of the face point in pixels.  # noqa: E501

        :param x: The x of this Point.  # noqa: E501
        :type: float
        """

        self._x = x

    @property
    def y(self):
        """Gets the y of this Point.  # noqa: E501

        y coordinate of the face point in pixels.  # noqa: E501

        :return: The y of this Point.  # noqa: E501
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this Point.

        y coordinate of the face point in pixels.  # noqa: E501

        :param y: The y of this Point.  # noqa: E501
        :type: float
        """

        self._y = y

    @property
    def type(self):
        """Gets the type of this Point.  # noqa: E501

        numerical face point unique type identifier.  # noqa: E501

        :return: The type of this Point.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Point.

        numerical face point unique type identifier.  # noqa: E501

        :param type: The type of this Point.  # noqa: E501
        :type: int
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this Point.  # noqa: E501

        face point type name for display.  # noqa: E501

        :return: The name of this Point.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Point.

        face point type name for display.  # noqa: E501

        :param name: The name of this Point.  # noqa: E501
        :type: str
        """

        self._name = name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Point, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Point):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other