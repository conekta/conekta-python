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

class CheckoutRequest(BaseModel):
    """
    [Checkout](https://developers.conekta.com/v2.1.0/reference/payment-link) details 
    """ # noqa: E501
    allowed_payment_methods: List[StrictStr] = Field(description="Are the payment methods available for this link")
    expires_at: Optional[StrictInt] = Field(default=None, description="Unix timestamp of checkout expiration")
    failure_url: Optional[StrictStr] = Field(default=None, description="Redirection url back to the site in case of failed payment, applies only to HostedPayment.")
    monthly_installments_enabled: Optional[StrictBool] = None
    monthly_installments_options: Optional[List[StrictInt]] = None
    name: Optional[StrictStr] = Field(default=None, description="Reason for payment")
    on_demand_enabled: Optional[StrictBool] = None
    redirection_time: Optional[StrictInt] = Field(default=None, description="number of seconds to wait before redirecting to the success_url")
    success_url: Optional[StrictStr] = Field(default=None, description="Redirection url back to the site in case of successful payment, applies only to HostedPayment")
    type: Optional[StrictStr] = Field(default=None, description="This field represents the type of checkout")
    __properties: ClassVar[List[str]] = ["allowed_payment_methods", "expires_at", "failure_url", "monthly_installments_enabled", "monthly_installments_options", "name", "on_demand_enabled", "redirection_time", "success_url", "type"]

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
        """Create an instance of CheckoutRequest from a JSON string"""
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
        """Create an instance of CheckoutRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allowed_payment_methods": obj.get("allowed_payment_methods"),
            "expires_at": obj.get("expires_at"),
            "failure_url": obj.get("failure_url"),
            "monthly_installments_enabled": obj.get("monthly_installments_enabled"),
            "monthly_installments_options": obj.get("monthly_installments_options"),
            "name": obj.get("name"),
            "on_demand_enabled": obj.get("on_demand_enabled"),
            "redirection_time": obj.get("redirection_time"),
            "success_url": obj.get("success_url"),
            "type": obj.get("type")
        })
        return _obj


