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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class OrderResponseCheckout(BaseModel):
    """
    OrderResponseCheckout
    """ # noqa: E501
    allowed_payment_methods: Optional[List[StrictStr]] = None
    can_not_expire: Optional[StrictBool] = None
    emails_sent: Optional[StrictInt] = None
    exclude_card_networks: Optional[List[Union[str, Any]]] = None
    expires_at: Optional[StrictInt] = None
    failure_url: Optional[StrictStr] = None
    force_3ds_flow: Optional[StrictBool] = None
    id: Optional[StrictStr] = None
    is_redirect_on_failure: Optional[StrictBool] = None
    livemode: Optional[StrictBool] = None
    metadata: Optional[Dict[str, Any]] = None
    monthly_installments_enabled: Optional[StrictBool] = None
    monthly_installments_options: Optional[List[StrictInt]] = None
    name: Optional[StrictStr] = None
    needs_shipping_contact: Optional[StrictBool] = None
    object: Optional[StrictStr] = None
    on_demand_enabled: Optional[StrictBool] = None
    paid_payments_count: Optional[StrictInt] = None
    recurrent: Optional[StrictBool] = None
    slug: Optional[StrictStr] = None
    sms_sent: Optional[StrictInt] = None
    success_url: Optional[StrictStr] = None
    starts_at: Optional[StrictInt] = None
    status: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["allowed_payment_methods", "can_not_expire", "emails_sent", "exclude_card_networks", "expires_at", "failure_url", "force_3ds_flow", "id", "is_redirect_on_failure", "livemode", "metadata", "monthly_installments_enabled", "monthly_installments_options", "name", "needs_shipping_contact", "object", "on_demand_enabled", "paid_payments_count", "recurrent", "slug", "sms_sent", "success_url", "starts_at", "status", "type", "url"]

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
        """Create an instance of OrderResponseCheckout from a JSON string"""
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
        # set to None if on_demand_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.on_demand_enabled is None and "on_demand_enabled" in self.model_fields_set:
            _dict['on_demand_enabled'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OrderResponseCheckout from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allowed_payment_methods": obj.get("allowed_payment_methods"),
            "can_not_expire": obj.get("can_not_expire"),
            "emails_sent": obj.get("emails_sent"),
            "exclude_card_networks": obj.get("exclude_card_networks"),
            "expires_at": obj.get("expires_at"),
            "failure_url": obj.get("failure_url"),
            "force_3ds_flow": obj.get("force_3ds_flow"),
            "id": obj.get("id"),
            "is_redirect_on_failure": obj.get("is_redirect_on_failure"),
            "livemode": obj.get("livemode"),
            "metadata": obj.get("metadata"),
            "monthly_installments_enabled": obj.get("monthly_installments_enabled"),
            "monthly_installments_options": obj.get("monthly_installments_options"),
            "name": obj.get("name"),
            "needs_shipping_contact": obj.get("needs_shipping_contact"),
            "object": obj.get("object"),
            "on_demand_enabled": obj.get("on_demand_enabled"),
            "paid_payments_count": obj.get("paid_payments_count"),
            "recurrent": obj.get("recurrent"),
            "slug": obj.get("slug"),
            "sms_sent": obj.get("sms_sent"),
            "success_url": obj.get("success_url"),
            "starts_at": obj.get("starts_at"),
            "status": obj.get("status"),
            "type": obj.get("type"),
            "url": obj.get("url")
        })
        return _obj


