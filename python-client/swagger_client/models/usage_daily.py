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


class UsageDaily(object):
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
        'year': 'int',
        'month': 'int',
        'day': 'int',
        'images': 'int'
    }

    attribute_map = {
        'year': 'year',
        'month': 'month',
        'day': 'day',
        'images': 'images'
    }

    def __init__(self, year=None, month=None, day=None, images=None):  # noqa: E501
        """UsageDaily - a model defined in Swagger"""  # noqa: E501

        self._year = None
        self._month = None
        self._day = None
        self._images = None
        self.discriminator = None

        if year is not None:
            self.year = year
        if month is not None:
            self.month = month
        if day is not None:
            self.day = day
        if images is not None:
            self.images = images

    @property
    def year(self):
        """Gets the year of this UsageDaily.  # noqa: E501

        year  # noqa: E501

        :return: The year of this UsageDaily.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this UsageDaily.

        year  # noqa: E501

        :param year: The year of this UsageDaily.  # noqa: E501
        :type: int
        """

        self._year = year

    @property
    def month(self):
        """Gets the month of this UsageDaily.  # noqa: E501

        month  # noqa: E501

        :return: The month of this UsageDaily.  # noqa: E501
        :rtype: int
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this UsageDaily.

        month  # noqa: E501

        :param month: The month of this UsageDaily.  # noqa: E501
        :type: int
        """

        self._month = month

    @property
    def day(self):
        """Gets the day of this UsageDaily.  # noqa: E501

        day  # noqa: E501

        :return: The day of this UsageDaily.  # noqa: E501
        :rtype: int
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this UsageDaily.

        day  # noqa: E501

        :param day: The day of this UsageDaily.  # noqa: E501
        :type: int
        """

        self._day = day

    @property
    def images(self):
        """Gets the images of this UsageDaily.  # noqa: E501

        processed images count  # noqa: E501

        :return: The images of this UsageDaily.  # noqa: E501
        :rtype: int
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this UsageDaily.

        processed images count  # noqa: E501

        :param images: The images of this UsageDaily.  # noqa: E501
        :type: int
        """

        self._images = images

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
        if issubclass(UsageDaily, dict):
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
        if not isinstance(other, UsageDaily):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
