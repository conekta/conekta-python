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

class UpdateProduct(BaseModel):
    """
    UpdateProduct
    """ # noqa: E501
    antifraud_info: Optional[Dict[str, Dict[str, Any]]] = None
    description: Optional[Annotated[str, Field(strict=True, max_length=250)]] = None
    sku: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    unit_price: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    quantity: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    tags: Optional[List[StrictStr]] = None
    brand: Optional[StrictStr] = None
    metadata: Optional[Dict[str, StrictStr]] = None
    __properties: ClassVar[List[str]] = ["antifraud_info", "description", "sku", "name", "unit_price", "quantity", "tags", "brand", "metadata"]

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
        """Create an instance of UpdateProduct from a JSON string"""
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
        """Create an instance of UpdateProduct from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "antifraud_info": obj.get("antifraud_info"),
            "description": obj.get("description"),
            "sku": obj.get("sku"),
            "name": obj.get("name"),
            "unit_price": obj.get("unit_price"),
            "quantity": obj.get("quantity"),
            "tags": obj.get("tags"),
            "brand": obj.get("brand"),
            "metadata": obj.get("metadata")
        })
        return _obj


