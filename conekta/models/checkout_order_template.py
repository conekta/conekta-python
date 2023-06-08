# coding: utf-8

"""
    Conekta API

    Conekta sdk  # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Contact: engineering@conekta.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, conlist, constr
from conekta.models.checkout_order_template_customer_info import CheckoutOrderTemplateCustomerInfo
from conekta.models.product import Product

class CheckoutOrderTemplate(BaseModel):
    """
    It maintains the attributes with which the order will be created when receiving a new payment.
    """
    currency: constr(strict=True, max_length=3) = Field(..., description="It is the currency in which the order will be created. It must be a valid ISO 4217 currency code.")
    customer_info: Optional[CheckoutOrderTemplateCustomerInfo] = None
    line_items: conlist(Product) = Field(..., description="They are the products to buy. Each contains the \"unit price\" and \"quantity\" parameters that are used to calculate the total amount of the order.")
    metadata: Optional[Dict[str, Any]] = Field(None, description="It is a set of key-value pairs that you can attach to the order. It can be used to store additional information about the order in a structured format.")
    __properties = ["currency", "customer_info", "line_items", "metadata"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> CheckoutOrderTemplate:
        """Create an instance of CheckoutOrderTemplate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
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
    def from_dict(cls, obj: dict) -> CheckoutOrderTemplate:
        """Create an instance of CheckoutOrderTemplate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CheckoutOrderTemplate.parse_obj(obj)

        _obj = CheckoutOrderTemplate.parse_obj({
            "currency": obj.get("currency"),
            "customer_info": CheckoutOrderTemplateCustomerInfo.from_dict(obj.get("customer_info")) if obj.get("customer_info") is not None else None,
            "line_items": [Product.from_dict(_item) for _item in obj.get("line_items")] if obj.get("line_items") is not None else None,
            "metadata": obj.get("metadata")
        })
        return _obj

