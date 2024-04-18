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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class OrderFiscalEntityAddressResponse(BaseModel):
    """
    Address of the fiscal entity
    """ # noqa: E501
    street1: StrictStr = Field(description="Street name and number")
    street2: Optional[StrictStr] = Field(default=None, description="Street name and number")
    postal_code: StrictStr = Field(description="Postal code")
    city: StrictStr = Field(description="City")
    state: Optional[StrictStr] = Field(default=None, description="State")
    country: StrictStr = Field(description="this field follows the [ISO 3166-1 alpha-2 standard](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)")
    external_number: StrictStr = Field(description="External number")
    object: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["street1", "street2", "postal_code", "city", "state", "country", "external_number", "object"]

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
        """Create an instance of OrderFiscalEntityAddressResponse from a JSON string"""
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
        # set to None if street2 (nullable) is None
        # and model_fields_set contains the field
        if self.street2 is None and "street2" in self.model_fields_set:
            _dict['street2'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderFiscalEntityAddressResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "street1": obj.get("street1"),
            "street2": obj.get("street2"),
            "postal_code": obj.get("postal_code"),
            "city": obj.get("city"),
            "state": obj.get("state"),
            "country": obj.get("country"),
            "external_number": obj.get("external_number"),
            "object": obj.get("object")
        })
        return _obj


