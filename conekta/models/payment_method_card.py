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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class PaymentMethodCard(BaseModel):
    """
    PaymentMethodCard
    """ # noqa: E501
    type: Optional[StrictStr] = None
    object: StrictStr
    account_type: Optional[StrictStr] = Field(default=None, description="Account type of the card")
    auth_code: Optional[StrictStr] = None
    brand: Optional[StrictStr] = Field(default=None, description="Brand of the card")
    contract_id: Optional[StrictStr] = Field(default=None, description="Id sent for recurrent charges.")
    country: Optional[StrictStr] = Field(default=None, description="Country of the card")
    exp_month: Optional[StrictStr] = Field(default=None, description="Expiration month of the card")
    exp_year: Optional[StrictStr] = Field(default=None, description="Expiration year of the card")
    fraud_indicators: Optional[List[Any]] = None
    issuer: Optional[StrictStr] = Field(default=None, description="Issuer of the card")
    last4: Optional[StrictStr] = Field(default=None, description="Last 4 digits of the card")
    name: Optional[StrictStr] = Field(default=None, description="Name of the cardholder")
    customer_ip_address: Optional[StrictStr] = Field(default=None, description="Optional field used to capture the customer's IP address for fraud prevention and security monitoring purposes")
    __properties: ClassVar[List[str]] = ["type", "object", "account_type", "auth_code", "brand", "contract_id", "country", "exp_month", "exp_year", "fraud_indicators", "issuer", "last4", "name", "customer_ip_address"]

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
        """Create an instance of PaymentMethodCard from a JSON string"""
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
        """Create an instance of PaymentMethodCard from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "object": obj.get("object"),
            "account_type": obj.get("account_type"),
            "auth_code": obj.get("auth_code"),
            "brand": obj.get("brand"),
            "contract_id": obj.get("contract_id"),
            "country": obj.get("country"),
            "exp_month": obj.get("exp_month"),
            "exp_year": obj.get("exp_year"),
            "fraud_indicators": obj.get("fraud_indicators"),
            "issuer": obj.get("issuer"),
            "last4": obj.get("last4"),
            "name": obj.get("name"),
            "customer_ip_address": obj.get("customer_ip_address")
        })
        return _obj


