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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from pydantic import Field
from typing_extensions import Annotated
from conekta.models.checkout_order_template_customer_info import CheckoutOrderTemplateCustomerInfo
from conekta.models.product import Product
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CheckoutOrderTemplate(BaseModel):
    """
    It maintains the attributes with which the order will be created when receiving a new payment.
    """ # noqa: E501
    currency: Annotated[str, Field(strict=True, max_length=3)] = Field(description="It is the currency in which the order will be created. It must be a valid ISO 4217 currency code.")
    customer_info: Optional[CheckoutOrderTemplateCustomerInfo] = None
    line_items: List[Product] = Field(description="They are the products to buy. Each contains the \"unit price\" and \"quantity\" parameters that are used to calculate the total amount of the order.")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="It is a set of key-value pairs that you can attach to the order. It can be used to store additional information about the order in a structured format.")
    __properties: ClassVar[List[str]] = ["currency", "customer_info", "line_items", "metadata"]

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
        """Create an instance of CheckoutOrderTemplate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of customer_info
        if self.customer_info:
            _dict['customer_info'] = self.customer_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in line_items (list)
        _items = []
        if self.line_items:
            for _item in self.line_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['line_items'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CheckoutOrderTemplate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "currency": obj.get("currency"),
            "customer_info": CheckoutOrderTemplateCustomerInfo.from_dict(obj.get("customer_info")) if obj.get("customer_info") is not None else None,
            "line_items": [Product.from_dict(_item) for _item in obj.get("line_items")] if obj.get("line_items") is not None else None,
            "metadata": obj.get("metadata")
        })
        return _obj


