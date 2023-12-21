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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from conekta.models.customer_shipping_contacts_address import CustomerShippingContactsAddress
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CustomerUpdateShippingContacts(BaseModel):
    """
    [Shipping](https://developers.conekta.com/v2.1.0/reference/createcustomershippingcontacts) details, required in case of sending a shipping. If we do not receive a shipping_contact on the order, the default shipping_contact of the customer will be used.
    """ # noqa: E501
    phone: Optional[StrictStr] = Field(default=None, description="Phone contact")
    receiver: Optional[StrictStr] = Field(default=None, description="Name of the person who will receive the order")
    between_streets: Optional[StrictStr] = Field(default=None, description="The street names between which the order will be delivered.")
    address: Optional[CustomerShippingContactsAddress] = None
    parent_id: Optional[StrictStr] = None
    default: Optional[StrictBool] = None
    deleted: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["phone", "receiver", "between_streets", "address", "parent_id", "default", "deleted"]

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
        """Create an instance of CustomerUpdateShippingContacts from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        # set to None if default (nullable) is None
        # and model_fields_set contains the field
        if self.default is None and "default" in self.model_fields_set:
            _dict['default'] = None

        # set to None if deleted (nullable) is None
        # and model_fields_set contains the field
        if self.deleted is None and "deleted" in self.model_fields_set:
            _dict['deleted'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CustomerUpdateShippingContacts from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "phone": obj.get("phone"),
            "receiver": obj.get("receiver"),
            "between_streets": obj.get("between_streets"),
            "address": CustomerShippingContactsAddress.from_dict(obj.get("address")) if obj.get("address") is not None else None,
            "parent_id": obj.get("parent_id"),
            "default": obj.get("default"),
            "deleted": obj.get("deleted")
        })
        return _obj


