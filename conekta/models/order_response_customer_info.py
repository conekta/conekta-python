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
from typing import Optional, Set
from typing_extensions import Self

class OrderResponseCustomerInfo(BaseModel):
    """
    OrderResponseCustomerInfo
    """ # noqa: E501
    customer_custom_reference: Optional[StrictStr] = Field(default=None, description="Custom reference")
    name: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    phone: Optional[StrictStr] = None
    corporate: Optional[StrictBool] = False
    object: Optional[StrictStr] = None
    customer_id: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["customer_custom_reference", "name", "email", "phone", "corporate", "object", "customer_id"]

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
        """Create an instance of OrderResponseCustomerInfo from a JSON string"""
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
        # set to None if customer_custom_reference (nullable) is None
        # and model_fields_set contains the field
        if self.customer_custom_reference is None and "customer_custom_reference" in self.model_fields_set:
            _dict['customer_custom_reference'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderResponseCustomerInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "customer_custom_reference": obj.get("customer_custom_reference"),
            "name": obj.get("name"),
            "email": obj.get("email"),
            "phone": obj.get("phone"),
            "corporate": obj.get("corporate") if obj.get("corporate") is not None else False,
            "object": obj.get("object"),
            "customer_id": obj.get("customer_id")
        })
        return _obj


