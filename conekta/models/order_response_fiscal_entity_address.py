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
from pydantic import BaseModel, Field, StrictBool, StrictStr

class OrderResponseFiscalEntityAddress(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    street1: StrictStr = ...
    street2: Optional[StrictStr] = None
    postal_code: StrictStr = ...
    city: StrictStr = ...
    state: Optional[StrictStr] = None
    country: Optional[StrictStr] = Field(None, description="this field follows the [ISO 3166-1 alpha-2 standard](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)")
    residential: Optional[StrictBool] = None
    external_number: Optional[StrictStr] = None
    object: Optional[StrictStr] = None
    __properties = ["street1", "street2", "postal_code", "city", "state", "country", "residential", "external_number", "object"]

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
    def from_json(cls, json_str: str) -> OrderResponseFiscalEntityAddress:
        """Create an instance of OrderResponseFiscalEntityAddress from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrderResponseFiscalEntityAddress:
        """Create an instance of OrderResponseFiscalEntityAddress from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return OrderResponseFiscalEntityAddress.parse_obj(obj)

        _obj = OrderResponseFiscalEntityAddress.parse_obj({
            "street1": obj.get("street1"),
            "street2": obj.get("street2"),
            "postal_code": obj.get("postal_code"),
            "city": obj.get("city"),
            "state": obj.get("state"),
            "country": obj.get("country"),
            "residential": obj.get("residential"),
            "external_number": obj.get("external_number"),
            "object": obj.get("object")
        })
        return _obj

