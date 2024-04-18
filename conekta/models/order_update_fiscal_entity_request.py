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
from conekta.models.fiscal_entity_address import FiscalEntityAddress
from typing import Optional, Set
from typing_extensions import Self

class OrderUpdateFiscalEntityRequest(BaseModel):
    """
    Fiscal entity of the order, Currently it is a purely informative field
    """ # noqa: E501
    address: FiscalEntityAddress
    email: Optional[StrictStr] = Field(default=None, description="Email of the fiscal entity")
    name: Optional[StrictStr] = Field(default=None, description="Name of the fiscal entity")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="Metadata associated with the fiscal entity")
    phone: Optional[StrictStr] = Field(default=None, description="Phone of the fiscal entity")
    tax_id: Optional[StrictStr] = Field(default=None, description="Tax ID of the fiscal entity")
    __properties: ClassVar[List[str]] = ["address", "email", "name", "metadata", "phone", "tax_id"]

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
        """Create an instance of OrderUpdateFiscalEntityRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if tax_id (nullable) is None
        # and model_fields_set contains the field
        if self.tax_id is None and "tax_id" in self.model_fields_set:
            _dict['tax_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderUpdateFiscalEntityRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address": FiscalEntityAddress.from_dict(obj["address"]) if obj.get("address") is not None else None,
            "email": obj.get("email"),
            "name": obj.get("name"),
            "metadata": obj.get("metadata"),
            "phone": obj.get("phone"),
            "tax_id": obj.get("tax_id")
        })
        return _obj


