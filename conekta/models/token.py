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
from pydantic import BaseModel
from conekta.models.token_card import TokenCard
from conekta.models.token_checkout import TokenCheckout
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Token(BaseModel):
    """
    a token
    """ # noqa: E501
    card: Optional[TokenCard] = None
    checkout: Optional[TokenCheckout] = None
    __properties: ClassVar[List[str]] = ["card", "checkout"]

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
        """Create an instance of Token from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of card
        if self.card:
            _dict['card'] = self.card.to_dict()
        # override the default output from pydantic by calling `to_dict()` of checkout
        if self.checkout:
            _dict['checkout'] = self.checkout.to_dict()
        # set to None if card (nullable) is None
        # and model_fields_set contains the field
        if self.card is None and "card" in self.model_fields_set:
            _dict['card'] = None

        # set to None if checkout (nullable) is None
        # and model_fields_set contains the field
        if self.checkout is None and "checkout" in self.model_fields_set:
            _dict['checkout'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Token from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "card": TokenCard.from_dict(obj.get("card")) if obj.get("card") is not None else None,
            "checkout": TokenCheckout.from_dict(obj.get("checkout")) if obj.get("checkout") is not None else None
        })
        return _obj


