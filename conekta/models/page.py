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
from pydantic import BaseModel, Field, StrictStr

class Page(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    next_page_url: Optional[StrictStr] = Field(None, description="URL of the next page.")
    previous_page_url: Optional[StrictStr] = Field(None, description="Url of the previous page.")
    __properties = ["next_page_url", "previous_page_url"]

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
    def from_json(cls, json_str: str) -> Page:
        """Create an instance of Page from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if next_page_url (nullable) is None
        if self.next_page_url is None:
            _dict['next_page_url'] = None

        # set to None if previous_page_url (nullable) is None
        if self.previous_page_url is None:
            _dict['previous_page_url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Page:
        """Create an instance of Page from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Page.parse_obj(obj)

        _obj = Page.parse_obj({
            "next_page_url": obj.get("next_page_url"),
            "previous_page_url": obj.get("previous_page_url")
        })
        return _obj
