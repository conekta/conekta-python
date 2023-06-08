# coding: utf-8

"""
    Conekta API

    Conekta sdk  # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Contact: engineering@conekta.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, conint

class DiscountLinesResponse(BaseModel):
    """
    DiscountLinesResponse
    """
    amount: conint(strict=True, ge=0) = Field(..., description="The amount to be deducted from the total sum of all payments, in cents.")
    code: StrictStr = Field(..., description="Discount code.")
    type: StrictStr = Field(..., description="It can be 'loyalty', 'campaign', 'coupon' o 'sign'")
    id: Optional[StrictStr] = None
    object: Optional[StrictStr] = None
    parent_id: Optional[StrictStr] = None
    __properties = ["amount", "code", "type", "id", "object", "parent_id"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> DiscountLinesResponse:
        """Create an instance of DiscountLinesResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DiscountLinesResponse:
        """Create an instance of DiscountLinesResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DiscountLinesResponse.parse_obj(obj)

        _obj = DiscountLinesResponse.parse_obj({
            "amount": obj.get("amount"),
            "code": obj.get("code"),
            "type": obj.get("type"),
            "id": obj.get("id"),
            "object": obj.get("object"),
            "parent_id": obj.get("parent_id")
        })
        return _obj

