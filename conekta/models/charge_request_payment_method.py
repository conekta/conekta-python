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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ChargeRequestPaymentMethod(BaseModel):
    """
    Payment method used in the charge. Go to the [payment methods](https://developers.conekta.com/reference/m%C3%A9todos-de-pago) section for more details 
    """ # noqa: E501
    expires_at: Optional[StrictInt] = Field(default=None, description="Method expiration date as unix timestamp")
    monthly_installments: Optional[StrictInt] = Field(default=None, description="How many months without interest to apply, it can be 3, 6, 9, 12 or 18")
    type: StrictStr
    token_id: Optional[StrictStr] = None
    payment_source_id: Optional[StrictStr] = None
    contract_id: Optional[StrictStr] = Field(default=None, description="Optional id sent to indicate the bank contract for recurrent card charges.")
    __properties: ClassVar[List[str]] = ["expires_at", "monthly_installments", "type", "token_id", "payment_source_id", "contract_id"]

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
        """Create an instance of ChargeRequestPaymentMethod from a JSON string"""
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
        """Create an instance of ChargeRequestPaymentMethod from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "expires_at": obj.get("expires_at"),
            "monthly_installments": obj.get("monthly_installments"),
            "type": obj.get("type"),
            "token_id": obj.get("token_id"),
            "payment_source_id": obj.get("payment_source_id"),
            "contract_id": obj.get("contract_id")
        })
        return _obj


