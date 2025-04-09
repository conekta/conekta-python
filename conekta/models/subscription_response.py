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
from typing import Optional, Set
from typing_extensions import Self

class SubscriptionResponse(BaseModel):
    """
    subscription model
    """ # noqa: E501
    billing_cycle_start: Optional[StrictInt] = None
    billing_cycle_end: Optional[StrictInt] = None
    canceled_at: Optional[StrictInt] = None
    canceled_reason: Optional[StrictStr] = Field(default=None, description="Reason for cancellation. This field appears when the subscription status is 'canceled'.")
    card_id: Optional[StrictStr] = None
    charge_id: Optional[StrictStr] = None
    created_at: Optional[StrictInt] = None
    customer_custom_reference: Optional[StrictStr] = None
    customer_id: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    last_billing_cycle_order_id: Optional[StrictStr] = None
    object: Optional[StrictStr] = None
    paused_at: Optional[StrictInt] = None
    plan_id: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    subscription_start: Optional[StrictInt] = None
    trial_start: Optional[StrictInt] = None
    trial_end: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["billing_cycle_start", "billing_cycle_end", "canceled_at", "canceled_reason", "card_id", "charge_id", "created_at", "customer_custom_reference", "customer_id", "id", "last_billing_cycle_order_id", "object", "paused_at", "plan_id", "status", "subscription_start", "trial_start", "trial_end"]

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
        """Create an instance of SubscriptionResponse from a JSON string"""
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
        # set to None if billing_cycle_start (nullable) is None
        # and model_fields_set contains the field
        if self.billing_cycle_start is None and "billing_cycle_start" in self.model_fields_set:
            _dict['billing_cycle_start'] = None

        # set to None if billing_cycle_end (nullable) is None
        # and model_fields_set contains the field
        if self.billing_cycle_end is None and "billing_cycle_end" in self.model_fields_set:
            _dict['billing_cycle_end'] = None

        # set to None if canceled_at (nullable) is None
        # and model_fields_set contains the field
        if self.canceled_at is None and "canceled_at" in self.model_fields_set:
            _dict['canceled_at'] = None

        # set to None if charge_id (nullable) is None
        # and model_fields_set contains the field
        if self.charge_id is None and "charge_id" in self.model_fields_set:
            _dict['charge_id'] = None

        # set to None if paused_at (nullable) is None
        # and model_fields_set contains the field
        if self.paused_at is None and "paused_at" in self.model_fields_set:
            _dict['paused_at'] = None

        # set to None if trial_start (nullable) is None
        # and model_fields_set contains the field
        if self.trial_start is None and "trial_start" in self.model_fields_set:
            _dict['trial_start'] = None

        # set to None if trial_end (nullable) is None
        # and model_fields_set contains the field
        if self.trial_end is None and "trial_end" in self.model_fields_set:
            _dict['trial_end'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SubscriptionResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "billing_cycle_start": obj.get("billing_cycle_start"),
            "billing_cycle_end": obj.get("billing_cycle_end"),
            "canceled_at": obj.get("canceled_at"),
            "canceled_reason": obj.get("canceled_reason"),
            "card_id": obj.get("card_id"),
            "charge_id": obj.get("charge_id"),
            "created_at": obj.get("created_at"),
            "customer_custom_reference": obj.get("customer_custom_reference"),
            "customer_id": obj.get("customer_id"),
            "id": obj.get("id"),
            "last_billing_cycle_order_id": obj.get("last_billing_cycle_order_id"),
            "object": obj.get("object"),
            "paused_at": obj.get("paused_at"),
            "plan_id": obj.get("plan_id"),
            "status": obj.get("status"),
            "subscription_start": obj.get("subscription_start"),
            "trial_start": obj.get("trial_start"),
            "trial_end": obj.get("trial_end")
        })
        return _obj


