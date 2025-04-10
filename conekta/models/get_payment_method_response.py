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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from conekta.models.get_customer_payment_method_data_response import GetCustomerPaymentMethodDataResponse
from typing import Optional, Set
from typing_extensions import Self

class GetPaymentMethodResponse(BaseModel):
    """
    GetPaymentMethodResponse
    """ # noqa: E501
    has_more: StrictBool = Field(description="Indicates if there are more pages to be requested")
    object: StrictStr = Field(description="Object type, in this case is list")
    next_page_url: Optional[StrictStr] = Field(default=None, description="URL of the next page.")
    previous_page_url: Optional[StrictStr] = Field(default=None, description="Url of the previous page.")
    data: Optional[List[GetCustomerPaymentMethodDataResponse]] = None
    __properties: ClassVar[List[str]] = ["has_more", "object", "next_page_url", "previous_page_url", "data"]

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
        """Create an instance of GetPaymentMethodResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item_data in self.data:
                if _item_data:
                    _items.append(_item_data.to_dict())
            _dict['data'] = _items
        # set to None if next_page_url (nullable) is None
        # and model_fields_set contains the field
        if self.next_page_url is None and "next_page_url" in self.model_fields_set:
            _dict['next_page_url'] = None

        # set to None if previous_page_url (nullable) is None
        # and model_fields_set contains the field
        if self.previous_page_url is None and "previous_page_url" in self.model_fields_set:
            _dict['previous_page_url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetPaymentMethodResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "has_more": obj.get("has_more"),
            "object": obj.get("object"),
            "next_page_url": obj.get("next_page_url"),
            "previous_page_url": obj.get("previous_page_url"),
            "data": [GetCustomerPaymentMethodDataResponse.from_dict(_item) for _item in obj["data"]] if obj.get("data") is not None else None
        })
        return _obj


