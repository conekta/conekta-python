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



from pydantic import BaseModel, Field, StrictBool, StrictStr

class ApiKeyRequest(BaseModel):
    """
    ApiKeyRequest
    """
    active: StrictBool = Field(..., description="Indicates if the api key is active")
    description: StrictStr = Field(..., description="Detail of the use that will be given to the api key")
    role: StrictStr = Field(...)
    __properties = ["active", "description", "role"]

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
    def from_json(cls, json_str: str) -> ApiKeyRequest:
        """Create an instance of ApiKeyRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiKeyRequest:
        """Create an instance of ApiKeyRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiKeyRequest.parse_obj(obj)

        _obj = ApiKeyRequest.parse_obj({
            "active": obj.get("active"),
            "description": obj.get("description"),
            "role": obj.get("role")
        })
        return _obj

