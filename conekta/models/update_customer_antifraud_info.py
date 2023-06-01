# coding: utf-8

"""
    Conekta API

    Conekta sdk  # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Contact: engineering@conekta.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictInt

class UpdateCustomerAntifraudInfo(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    account_created_at: Optional[StrictInt] = None
    first_paid_at: Optional[StrictInt] = None
    __properties = ["account_created_at", "first_paid_at"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> UpdateCustomerAntifraudInfo:
        """Create an instance of UpdateCustomerAntifraudInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateCustomerAntifraudInfo:
        """Create an instance of UpdateCustomerAntifraudInfo from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return UpdateCustomerAntifraudInfo.parse_obj(obj)

        _obj = UpdateCustomerAntifraudInfo.parse_obj({
            "account_created_at": obj.get("account_created_at"),
            "first_paid_at": obj.get("first_paid_at")
        })
        return _obj

