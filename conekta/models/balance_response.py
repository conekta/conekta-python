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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel
from pydantic import Field
from conekta.models.balance_common_field import BalanceCommonField
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class BalanceResponse(BaseModel):
    """
    balance model
    """ # noqa: E501
    available: Optional[List[BalanceCommonField]] = Field(default=None, description="The balance's available")
    cashout_retention_amount: Optional[List[BalanceCommonField]] = Field(default=None, description="The balance's cashout retention amount")
    conekta_retention: Optional[List[BalanceCommonField]] = Field(default=None, description="The balance's conekta retention")
    gateway: Optional[List[BalanceCommonField]] = Field(default=None, description="The balance's gateway")
    pending: Optional[List[BalanceCommonField]] = Field(default=None, description="The balance's pending")
    retained: Optional[List[BalanceCommonField]] = Field(default=None, description="The balance's retained")
    retention_amount: Optional[List[BalanceCommonField]] = Field(default=None, description="The balance's retention amount")
    target_collateral_amount: Optional[Union[str, Any]] = Field(default=None, description="The balance's target collateral amount")
    target_retention_amount: Optional[List[BalanceCommonField]] = Field(default=None, description="The balance's target retention amount")
    temporarily_retained: Optional[List[BalanceCommonField]] = Field(default=None, description="The balance's temporarily retained")
    __properties: ClassVar[List[str]] = ["available", "cashout_retention_amount", "conekta_retention", "gateway", "pending", "retained", "retention_amount", "target_collateral_amount", "target_retention_amount", "temporarily_retained"]

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
        """Create an instance of BalanceResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in available (list)
        _items = []
        if self.available:
            for _item in self.available:
                if _item:
                    _items.append(_item.to_dict())
            _dict['available'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in cashout_retention_amount (list)
        _items = []
        if self.cashout_retention_amount:
            for _item in self.cashout_retention_amount:
                if _item:
                    _items.append(_item.to_dict())
            _dict['cashout_retention_amount'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in conekta_retention (list)
        _items = []
        if self.conekta_retention:
            for _item in self.conekta_retention:
                if _item:
                    _items.append(_item.to_dict())
            _dict['conekta_retention'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in gateway (list)
        _items = []
        if self.gateway:
            for _item in self.gateway:
                if _item:
                    _items.append(_item.to_dict())
            _dict['gateway'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in pending (list)
        _items = []
        if self.pending:
            for _item in self.pending:
                if _item:
                    _items.append(_item.to_dict())
            _dict['pending'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in retained (list)
        _items = []
        if self.retained:
            for _item in self.retained:
                if _item:
                    _items.append(_item.to_dict())
            _dict['retained'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in retention_amount (list)
        _items = []
        if self.retention_amount:
            for _item in self.retention_amount:
                if _item:
                    _items.append(_item.to_dict())
            _dict['retention_amount'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in target_retention_amount (list)
        _items = []
        if self.target_retention_amount:
            for _item in self.target_retention_amount:
                if _item:
                    _items.append(_item.to_dict())
            _dict['target_retention_amount'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in temporarily_retained (list)
        _items = []
        if self.temporarily_retained:
            for _item in self.temporarily_retained:
                if _item:
                    _items.append(_item.to_dict())
            _dict['temporarily_retained'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of BalanceResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "available": [BalanceCommonField.from_dict(_item) for _item in obj.get("available")] if obj.get("available") is not None else None,
            "cashout_retention_amount": [BalanceCommonField.from_dict(_item) for _item in obj.get("cashout_retention_amount")] if obj.get("cashout_retention_amount") is not None else None,
            "conekta_retention": [BalanceCommonField.from_dict(_item) for _item in obj.get("conekta_retention")] if obj.get("conekta_retention") is not None else None,
            "gateway": [BalanceCommonField.from_dict(_item) for _item in obj.get("gateway")] if obj.get("gateway") is not None else None,
            "pending": [BalanceCommonField.from_dict(_item) for _item in obj.get("pending")] if obj.get("pending") is not None else None,
            "retained": [BalanceCommonField.from_dict(_item) for _item in obj.get("retained")] if obj.get("retained") is not None else None,
            "retention_amount": [BalanceCommonField.from_dict(_item) for _item in obj.get("retention_amount")] if obj.get("retention_amount") is not None else None,
            "target_collateral_amount": obj.get("target_collateral_amount"),
            "target_retention_amount": [BalanceCommonField.from_dict(_item) for _item in obj.get("target_retention_amount")] if obj.get("target_retention_amount") is not None else None,
            "temporarily_retained": [BalanceCommonField.from_dict(_item) for _item in obj.get("temporarily_retained")] if obj.get("temporarily_retained") is not None else None
        })
        return _obj

