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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from conekta.models.webhook_log import WebhookLog
from typing import Optional, Set
from typing_extensions import Self

class EventResponse(BaseModel):
    """
    event model
    """ # noqa: E501
    created_at: Optional[StrictInt] = None
    data: Optional[Dict[str, Any]] = None
    id: Optional[StrictStr] = None
    livemode: Optional[StrictBool] = None
    object: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    webhook_logs: Optional[List[WebhookLog]] = None
    webhook_status: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["created_at", "data", "id", "livemode", "object", "type", "webhook_logs", "webhook_status"]

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
        """Create an instance of EventResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in webhook_logs (list)
        _items = []
        if self.webhook_logs:
            for _item in self.webhook_logs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['webhook_logs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EventResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "data": obj.get("data"),
            "id": obj.get("id"),
            "livemode": obj.get("livemode"),
            "object": obj.get("object"),
            "type": obj.get("type"),
            "webhook_logs": [WebhookLog.from_dict(_item) for _item in obj["webhook_logs"]] if obj.get("webhook_logs") is not None else None,
            "webhook_status": obj.get("webhook_status")
        })
        return _obj


