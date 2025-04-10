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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class ProductOrderResponse(BaseModel):
    """
    ProductOrderResponse
    """ # noqa: E501
    antifraud_info: Optional[Dict[str, Any]] = None
    brand: Optional[StrictStr] = Field(default=None, description="The brand of the item.")
    description: Optional[Annotated[str, Field(strict=True, max_length=250)]] = Field(default=None, description="Short description of the item")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="It is a key/value hash that can hold custom fields. Maximum 100 elements and allows special characters.")
    name: StrictStr = Field(description="The name of the item. It will be displayed in the order.")
    quantity: Annotated[int, Field(strict=True, ge=1)] = Field(description="The quantity of the item in the order.")
    sku: Optional[StrictStr] = Field(default=None, description="The stock keeping unit for the item. It is used to identify the item in the order.")
    tags: Optional[List[StrictStr]] = Field(default=None, description="List of tags for the item. It is used to identify the item in the order.")
    unit_price: Annotated[int, Field(strict=True, ge=0)] = Field(description="The price of the item in cents.")
    id: Optional[StrictStr] = None
    object: Optional[StrictStr] = None
    parent_id: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["antifraud_info", "brand", "description", "metadata", "name", "quantity", "sku", "tags", "unit_price", "id", "object", "parent_id"]

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
        """Create an instance of ProductOrderResponse from a JSON string"""
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
        """Create an instance of ProductOrderResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "antifraud_info": obj.get("antifraud_info"),
            "brand": obj.get("brand"),
            "description": obj.get("description"),
            "metadata": obj.get("metadata"),
            "name": obj.get("name"),
            "quantity": obj.get("quantity"),
            "sku": obj.get("sku"),
            "tags": obj.get("tags"),
            "unit_price": obj.get("unit_price"),
            "id": obj.get("id"),
            "object": obj.get("object"),
            "parent_id": obj.get("parent_id")
        })
        return _obj


