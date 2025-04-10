# coding: utf-8

"""
    Conekta API

    Conekta sdk

    The version of the OpenAPI document: 2.2.0
    Contact: engineering@conekta.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from conekta.models.token_response_checkout import TokenResponseCheckout
from typing import Optional, Set
from typing_extensions import Self

class TokenResponse(BaseModel):
    """
    token response
    """ # noqa: E501
    checkout: Optional[TokenResponseCheckout] = None
    id: StrictStr = Field(description="Unique identifier for the token generated by Conekta.")
    livemode: StrictBool = Field(description="Indicates whether the token is in live mode or test mode.")
    object: StrictStr = Field(description="Indicates the type of object, in this case token")
    used: StrictBool = Field(description="Indicates if the token has been used")
    __properties: ClassVar[List[str]] = ["checkout", "id", "livemode", "object", "used"]

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
        """Create an instance of TokenResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of checkout
        if self.checkout:
            _dict['checkout'] = self.checkout.to_dict()
        # set to None if checkout (nullable) is None
        # and model_fields_set contains the field
        if self.checkout is None and "checkout" in self.model_fields_set:
            _dict['checkout'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TokenResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "checkout": TokenResponseCheckout.from_dict(obj["checkout"]) if obj.get("checkout") is not None else None,
            "id": obj.get("id"),
            "livemode": obj.get("livemode"),
            "object": obj.get("object"),
            "used": obj.get("used")
        })
        return _obj


