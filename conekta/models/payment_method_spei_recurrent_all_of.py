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
from pydantic import BaseModel, StrictStr

class PaymentMethodSpeiRecurrentAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    reference: Optional[StrictStr] = None
    expires_at: Optional[StrictStr] = None
    __properties = ["reference", "expires_at"]

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
    def from_json(cls, json_str: str) -> PaymentMethodSpeiRecurrentAllOf:
        """Create an instance of PaymentMethodSpeiRecurrentAllOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PaymentMethodSpeiRecurrentAllOf:
        """Create an instance of PaymentMethodSpeiRecurrentAllOf from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return PaymentMethodSpeiRecurrentAllOf.parse_obj(obj)

        _obj = PaymentMethodSpeiRecurrentAllOf.parse_obj({
            "reference": obj.get("reference"),
            "expires_at": obj.get("expires_at")
        })
        return _obj

