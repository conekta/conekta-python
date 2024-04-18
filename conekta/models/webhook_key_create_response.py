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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class WebhookKeyCreateResponse(BaseModel):
    """
    webhook keys model
    """ # noqa: E501
    active: Optional[StrictBool] = Field(default=None, description="Indicates if the webhook key is active")
    created_at: Optional[StrictInt] = Field(default=None, description="Unix timestamp in seconds with the creation date of the webhook key")
    id: Optional[StrictStr] = Field(default=None, description="Unique identifier of the webhook key")
    livemode: Optional[StrictBool] = Field(default=None, description="Indicates if the webhook key is in live mode")
    object: Optional[StrictStr] = Field(default=None, description="Object name, value is webhook_key")
    public_key: Optional[StrictStr] = Field(default=None, description="Public key to be used in the webhook")
    __properties: ClassVar[List[str]] = ["active", "created_at", "id", "livemode", "object", "public_key"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of WebhookKeyCreateResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebhookKeyCreateResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "active": obj.get("active"),
            "created_at": obj.get("created_at"),
            "id": obj.get("id"),
            "livemode": obj.get("livemode"),
            "object": obj.get("object"),
            "public_key": obj.get("public_key")
        })
        return _obj


