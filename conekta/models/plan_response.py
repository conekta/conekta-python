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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class PlanResponse(BaseModel):
    """
    plans model
    """ # noqa: E501
    amount: Optional[StrictInt] = None
    created_at: Optional[StrictInt] = None
    currency: Optional[Annotated[str, Field(strict=True, max_length=3)]] = None
    expiry_count: Optional[StrictInt] = None
    frequency: Optional[StrictInt] = None
    id: Optional[StrictStr] = None
    interval: Optional[StrictStr] = None
    livemode: Optional[StrictBool] = None
    name: Optional[StrictStr] = None
    object: Optional[StrictStr] = None
    trial_period_days: Optional[StrictInt] = None
    max_retries: Optional[StrictInt] = None
    retry_delay_hours: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["amount", "created_at", "currency", "expiry_count", "frequency", "id", "interval", "livemode", "name", "object", "trial_period_days", "max_retries", "retry_delay_hours"]

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
        """Create an instance of PlanResponse from a JSON string"""
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
        # set to None if expiry_count (nullable) is None
        # and model_fields_set contains the field
        if self.expiry_count is None and "expiry_count" in self.model_fields_set:
            _dict['expiry_count'] = None

        # set to None if trial_period_days (nullable) is None
        # and model_fields_set contains the field
        if self.trial_period_days is None and "trial_period_days" in self.model_fields_set:
            _dict['trial_period_days'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PlanResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": obj.get("amount"),
            "created_at": obj.get("created_at"),
            "currency": obj.get("currency"),
            "expiry_count": obj.get("expiry_count"),
            "frequency": obj.get("frequency"),
            "id": obj.get("id"),
            "interval": obj.get("interval"),
            "livemode": obj.get("livemode"),
            "name": obj.get("name"),
            "object": obj.get("object"),
            "trial_period_days": obj.get("trial_period_days"),
            "max_retries": obj.get("max_retries"),
            "retry_delay_hours": obj.get("retry_delay_hours")
        })
        return _obj


