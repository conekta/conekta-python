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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from conekta.models.charge_request import ChargeRequest
from conekta.models.checkout_request import CheckoutRequest
from conekta.models.customer_shipping_contacts import CustomerShippingContacts
from conekta.models.order_discount_lines_request import OrderDiscountLinesRequest
from conekta.models.order_fiscal_entity_request import OrderFiscalEntityRequest
from conekta.models.order_request_customer_info import OrderRequestCustomerInfo
from conekta.models.order_tax_request import OrderTaxRequest
from conekta.models.product import Product
from conekta.models.shipping_request import ShippingRequest
from typing import Optional, Set
from typing_extensions import Self

class OrderRequest(BaseModel):
    """
    a order
    """ # noqa: E501
    charges: Optional[List[ChargeRequest]] = Field(default=None, description="List of [charges](https://developers.conekta.com/v2.1.0/reference/orderscreatecharge) that are applied to the order")
    checkout: Optional[CheckoutRequest] = None
    currency: Annotated[str, Field(strict=True, max_length=3)] = Field(description="Currency with which the payment will be made. It uses the 3-letter code of the [International Standard ISO 4217.](https://es.wikipedia.org/wiki/ISO_4217)")
    customer_info: OrderRequestCustomerInfo
    discount_lines: Optional[List[OrderDiscountLinesRequest]] = Field(default=None, description="List of [discounts](https://developers.conekta.com/v2.1.0/reference/orderscreatediscountline) that are applied to the order. You must have at least one discount.")
    fiscal_entity: Optional[OrderFiscalEntityRequest] = None
    line_items: List[Product] = Field(description="List of [products](https://developers.conekta.com/v2.1.0/reference/orderscreateproduct) that are sold in the order. You must have at least one product.")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="Metadata associated with the order")
    needs_shipping_contact: Optional[StrictBool] = Field(default=None, description="Allows you to fill out the shipping information at checkout")
    pre_authorize: Optional[StrictBool] = Field(default=False, description="Indicates whether the order charges must be preauthorized")
    processing_mode: Optional[StrictStr] = Field(default=None, description="Indicates the processing mode for the order, either ecommerce, recurrent or validation.")
    return_url: Optional[StrictStr] = Field(default=None, description="Indicates the redirection callback upon completion of the 3DS2 flow. Do not use this parameter if your order has a checkout parameter")
    shipping_contact: Optional[CustomerShippingContacts] = None
    shipping_lines: Optional[List[ShippingRequest]] = Field(default=None, description="List of [shipping costs](https://developers.conekta.com/v2.1.0/reference/orderscreateshipping). If the online store offers digital products.")
    tax_lines: Optional[List[OrderTaxRequest]] = Field(default=None, description="List of [taxes](https://developers.conekta.com/v2.1.0/reference/orderscreatetaxes) that are applied to the order.")
    three_ds_mode: Optional[StrictStr] = Field(default=None, description="Indicates the 3DS2 mode for the order, either smart or strict.")
    __properties: ClassVar[List[str]] = ["charges", "checkout", "currency", "customer_info", "discount_lines", "fiscal_entity", "line_items", "metadata", "needs_shipping_contact", "pre_authorize", "processing_mode", "return_url", "shipping_contact", "shipping_lines", "tax_lines", "three_ds_mode"]

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
        """Create an instance of OrderRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in charges (list)
        _items = []
        if self.charges:
            for _item_charges in self.charges:
                if _item_charges:
                    _items.append(_item_charges.to_dict())
            _dict['charges'] = _items
        # override the default output from pydantic by calling `to_dict()` of checkout
        if self.checkout:
            _dict['checkout'] = self.checkout.to_dict()
        # override the default output from pydantic by calling `to_dict()` of customer_info
        if self.customer_info:
            _dict['customer_info'] = self.customer_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in discount_lines (list)
        _items = []
        if self.discount_lines:
            for _item_discount_lines in self.discount_lines:
                if _item_discount_lines:
                    _items.append(_item_discount_lines.to_dict())
            _dict['discount_lines'] = _items
        # override the default output from pydantic by calling `to_dict()` of fiscal_entity
        if self.fiscal_entity:
            _dict['fiscal_entity'] = self.fiscal_entity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in line_items (list)
        _items = []
        if self.line_items:
            for _item_line_items in self.line_items:
                if _item_line_items:
                    _items.append(_item_line_items.to_dict())
            _dict['line_items'] = _items
        # override the default output from pydantic by calling `to_dict()` of shipping_contact
        if self.shipping_contact:
            _dict['shipping_contact'] = self.shipping_contact.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in shipping_lines (list)
        _items = []
        if self.shipping_lines:
            for _item_shipping_lines in self.shipping_lines:
                if _item_shipping_lines:
                    _items.append(_item_shipping_lines.to_dict())
            _dict['shipping_lines'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in tax_lines (list)
        _items = []
        if self.tax_lines:
            for _item_tax_lines in self.tax_lines:
                if _item_tax_lines:
                    _items.append(_item_tax_lines.to_dict())
            _dict['tax_lines'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "charges": [ChargeRequest.from_dict(_item) for _item in obj["charges"]] if obj.get("charges") is not None else None,
            "checkout": CheckoutRequest.from_dict(obj["checkout"]) if obj.get("checkout") is not None else None,
            "currency": obj.get("currency"),
            "customer_info": OrderRequestCustomerInfo.from_dict(obj["customer_info"]) if obj.get("customer_info") is not None else None,
            "discount_lines": [OrderDiscountLinesRequest.from_dict(_item) for _item in obj["discount_lines"]] if obj.get("discount_lines") is not None else None,
            "fiscal_entity": OrderFiscalEntityRequest.from_dict(obj["fiscal_entity"]) if obj.get("fiscal_entity") is not None else None,
            "line_items": [Product.from_dict(_item) for _item in obj["line_items"]] if obj.get("line_items") is not None else None,
            "metadata": obj.get("metadata"),
            "needs_shipping_contact": obj.get("needs_shipping_contact"),
            "pre_authorize": obj.get("pre_authorize") if obj.get("pre_authorize") is not None else False,
            "processing_mode": obj.get("processing_mode"),
            "return_url": obj.get("return_url"),
            "shipping_contact": CustomerShippingContacts.from_dict(obj["shipping_contact"]) if obj.get("shipping_contact") is not None else None,
            "shipping_lines": [ShippingRequest.from_dict(_item) for _item in obj["shipping_lines"]] if obj.get("shipping_lines") is not None else None,
            "tax_lines": [OrderTaxRequest.from_dict(_item) for _item in obj["tax_lines"]] if obj.get("tax_lines") is not None else None,
            "three_ds_mode": obj.get("three_ds_mode")
        })
        return _obj


