# coding: utf-8

"""
    Conekta API

    Conekta sdk

    The version of the OpenAPI document: 2.1.0
    Contact: engineering@conekta.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ApiKeyResponse(BaseModel):
    """
    api keys model
    """ # noqa: E501
    active: Optional[StrictBool] = Field(default=None, description="Indicates if the api key is active")
    created_at: Optional[StrictInt] = Field(default=None, description="Unix timestamp in seconds of when the api key was created")
    updated_at: Optional[StrictInt] = Field(default=None, description="Unix timestamp in seconds of when the api key was last updated")
    deactivated_at: Optional[StrictInt] = Field(default=None, description="Unix timestamp in seconds of when the api key was deleted")
    description: Optional[StrictStr] = Field(default=None, description="A name or brief explanation of what this api key is used for")
    id: Optional[StrictStr] = Field(default=None, description="Unique identifier of the api key")
    livemode: Optional[StrictBool] = Field(default=None, description="Indicates if the api key is in production")
    deleted: Optional[StrictBool] = Field(default=None, description="Indicates if the api key was deleted")
    object: Optional[StrictStr] = Field(default=None, description="Object name, value is 'api_key'")
    prefix: Optional[StrictStr] = Field(default=None, description="The first few characters of the authentication_token")
    role: Optional[StrictStr] = Field(default=None, description="Indicates if the api key is private or public")
    __properties: ClassVar[List[str]] = ["active", "created_at", "updated_at", "deactivated_at", "description", "id", "livemode", "deleted", "object", "prefix", "role"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ApiKeyResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # set to None if deactivated_at (nullable) is None
        # and model_fields_set contains the field
        if self.deactivated_at is None and "deactivated_at" in self.model_fields_set:
            _dict['deactivated_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ApiKeyResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "active": obj.get("active"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "deactivated_at": obj.get("deactivated_at"),
            "description": obj.get("description"),
            "id": obj.get("id"),
            "livemode": obj.get("livemode"),
            "deleted": obj.get("deleted"),
            "object": obj.get("object"),
            "prefix": obj.get("prefix"),
            "role": obj.get("role")
        })
        return _obj


