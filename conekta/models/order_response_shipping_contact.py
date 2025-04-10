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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from conekta.models.customer_shipping_contacts_response_address import CustomerShippingContactsResponseAddress
from typing import Optional, Set
from typing_extensions import Self

class OrderResponseShippingContact(BaseModel):
    """
    OrderResponseShippingContact
    """ # noqa: E501
    phone: Optional[StrictStr] = None
    receiver: Optional[StrictStr] = None
    between_streets: Optional[StrictStr] = None
    address: Optional[CustomerShippingContactsResponseAddress] = None
    parent_id: Optional[StrictStr] = None
    default: Optional[StrictBool] = None
    id: Optional[StrictStr] = None
    created_at: Optional[StrictInt] = None
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="Metadata associated with the shipping contact")
    object: Optional[StrictStr] = None
    deleted: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["phone", "receiver", "between_streets", "address", "parent_id", "default", "id", "created_at", "metadata", "object", "deleted"]

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
        """Create an instance of OrderResponseShippingContact from a JSON string"""
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
        # set to None if between_streets (nullable) is None
        # and model_fields_set contains the field
        if self.between_streets is None and "between_streets" in self.model_fields_set:
            _dict['between_streets'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderResponseShippingContact from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "phone": obj.get("phone"),
            "receiver": obj.get("receiver"),
            "between_streets": obj.get("between_streets"),
            "address": CustomerShippingContactsResponseAddress.from_dict(obj["address"]) if obj.get("address") is not None else None,
            "parent_id": obj.get("parent_id"),
            "default": obj.get("default"),
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "metadata": obj.get("metadata"),
            "object": obj.get("object"),
            "deleted": obj.get("deleted")
        })
        return _obj


