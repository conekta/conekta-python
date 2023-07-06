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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from conekta.models.discount_lines_response import DiscountLinesResponse

class GetOrderDiscountLinesResponse(BaseModel):
    """
    GetOrderDiscountLinesResponse
    """
    has_more: StrictBool = Field(..., description="Indicates if there are more pages to be requested")
    object: StrictStr = Field(..., description="Object type, in this case is list")
    next_page_url: Optional[StrictStr] = Field(None, description="URL of the next page.")
    previous_page_url: Optional[StrictStr] = Field(None, description="Url of the previous page.")
    data: Optional[conlist(DiscountLinesResponse)] = None
    __properties = ["has_more", "object", "next_page_url", "previous_page_url", "data"]

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
    def from_json(cls, json_str: str) -> GetOrderDiscountLinesResponse:
        """Create an instance of GetOrderDiscountLinesResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['data'] = _items
        # set to None if next_page_url (nullable) is None
        # and __fields_set__ contains the field
        if self.next_page_url is None and "next_page_url" in self.__fields_set__:
            _dict['next_page_url'] = None

        # set to None if previous_page_url (nullable) is None
        # and __fields_set__ contains the field
        if self.previous_page_url is None and "previous_page_url" in self.__fields_set__:
            _dict['previous_page_url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetOrderDiscountLinesResponse:
        """Create an instance of GetOrderDiscountLinesResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetOrderDiscountLinesResponse.parse_obj(obj)

        _obj = GetOrderDiscountLinesResponse.parse_obj({
            "has_more": obj.get("has_more"),
            "object": obj.get("object"),
            "next_page_url": obj.get("next_page_url"),
            "previous_page_url": obj.get("previous_page_url"),
            "data": [DiscountLinesResponse.from_dict(_item) for _item in obj.get("data")] if obj.get("data") is not None else None
        })
        return _obj

