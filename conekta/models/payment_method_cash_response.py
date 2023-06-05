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
from pydantic import BaseModel, StrictInt, StrictStr

class PaymentMethodCashResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    type: StrictStr = ...
    id: StrictStr = ...
    object: StrictStr = ...
    created_at: StrictInt = ...
    parent_id: Optional[StrictStr] = None
    reference: Optional[StrictStr] = None
    barcode: Optional[StrictStr] = None
    barcode_url: Optional[StrictStr] = None
    expires_at: Optional[StrictInt] = None
    provider: Optional[StrictStr] = None
    __properties = ["type", "id", "object", "created_at", "parent_id", "reference", "barcode", "barcode_url", "expires_at", "provider"]

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
    def from_json(cls, json_str: str) -> PaymentMethodCashResponse:
        """Create an instance of PaymentMethodCashResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PaymentMethodCashResponse:
        """Create an instance of PaymentMethodCashResponse from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return PaymentMethodCashResponse.parse_obj(obj)

        _obj = PaymentMethodCashResponse.parse_obj({
            "type": obj.get("type"),
            "id": obj.get("id"),
            "object": obj.get("object"),
            "created_at": obj.get("created_at"),
            "parent_id": obj.get("parent_id"),
            "reference": obj.get("reference"),
            "barcode": obj.get("barcode"),
            "barcode_url": obj.get("barcode_url"),
            "expires_at": obj.get("expires_at"),
            "provider": obj.get("provider")
        })
        return _obj
