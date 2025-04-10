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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from conekta.models.payment_method_cash_response_all_of_agreements import PaymentMethodCashResponseAllOfAgreements
from typing import Optional, Set
from typing_extensions import Self

class PaymentMethodCashResponse(BaseModel):
    """
    PaymentMethodCashResponse
    """ # noqa: E501
    type: StrictStr
    id: StrictStr
    object: StrictStr
    created_at: StrictInt
    parent_id: Optional[StrictStr] = None
    agreements: Optional[List[PaymentMethodCashResponseAllOfAgreements]] = None
    reference: Optional[StrictStr] = None
    barcode: Optional[StrictStr] = None
    barcode_url: Optional[StrictStr] = Field(default=None, description="URL to the barcode image, reference is the same as barcode")
    expires_at: Optional[StrictInt] = None
    provider: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["type", "id", "object", "created_at", "parent_id", "agreements", "reference", "barcode", "barcode_url", "expires_at", "provider"]

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
        """Create an instance of PaymentMethodCashResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in agreements (list)
        _items = []
        if self.agreements:
            for _item_agreements in self.agreements:
                if _item_agreements:
                    _items.append(_item_agreements.to_dict())
            _dict['agreements'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentMethodCashResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "id": obj.get("id"),
            "object": obj.get("object"),
            "created_at": obj.get("created_at"),
            "parent_id": obj.get("parent_id"),
            "agreements": [PaymentMethodCashResponseAllOfAgreements.from_dict(_item) for _item in obj["agreements"]] if obj.get("agreements") is not None else None,
            "reference": obj.get("reference"),
            "barcode": obj.get("barcode"),
            "barcode_url": obj.get("barcode_url"),
            "expires_at": obj.get("expires_at"),
            "provider": obj.get("provider")
        })
        return _obj


