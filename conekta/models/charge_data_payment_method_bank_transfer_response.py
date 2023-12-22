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
from pydantic import BaseModel, StrictInt, StrictStr
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ChargeDataPaymentMethodBankTransferResponse(BaseModel):
    """
    use for bank transfer responses
    """ # noqa: E501
    bank: Optional[StrictStr] = None
    clabe: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    executed_at: Optional[StrictInt] = None
    expires_at: Optional[StrictInt] = None
    issuing_account_bank: Optional[StrictStr] = None
    issuing_account_number: Optional[StrictStr] = None
    issuing_account_holder_name: Optional[StrictStr] = None
    issuing_account_tax_id: Optional[StrictStr] = None
    payment_attempts: Optional[List[Any]] = None
    receiving_account_holder_name: Optional[StrictStr] = None
    receiving_account_number: Optional[StrictStr] = None
    receiving_account_bank: Optional[StrictStr] = None
    receiving_account_tax_id: Optional[StrictStr] = None
    reference_number: Optional[StrictStr] = None
    tracking_code: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["bank", "clabe", "description", "executed_at", "expires_at", "issuing_account_bank", "issuing_account_number", "issuing_account_holder_name", "issuing_account_tax_id", "payment_attempts", "receiving_account_holder_name", "receiving_account_number", "receiving_account_bank", "receiving_account_tax_id", "reference_number", "tracking_code"]

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
        """Create an instance of ChargeDataPaymentMethodBankTransferResponse from a JSON string"""
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
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if executed_at (nullable) is None
        # and model_fields_set contains the field
        if self.executed_at is None and "executed_at" in self.model_fields_set:
            _dict['executed_at'] = None

        # set to None if issuing_account_bank (nullable) is None
        # and model_fields_set contains the field
        if self.issuing_account_bank is None and "issuing_account_bank" in self.model_fields_set:
            _dict['issuing_account_bank'] = None

        # set to None if issuing_account_number (nullable) is None
        # and model_fields_set contains the field
        if self.issuing_account_number is None and "issuing_account_number" in self.model_fields_set:
            _dict['issuing_account_number'] = None

        # set to None if issuing_account_holder_name (nullable) is None
        # and model_fields_set contains the field
        if self.issuing_account_holder_name is None and "issuing_account_holder_name" in self.model_fields_set:
            _dict['issuing_account_holder_name'] = None

        # set to None if issuing_account_tax_id (nullable) is None
        # and model_fields_set contains the field
        if self.issuing_account_tax_id is None and "issuing_account_tax_id" in self.model_fields_set:
            _dict['issuing_account_tax_id'] = None

        # set to None if receiving_account_holder_name (nullable) is None
        # and model_fields_set contains the field
        if self.receiving_account_holder_name is None and "receiving_account_holder_name" in self.model_fields_set:
            _dict['receiving_account_holder_name'] = None

        # set to None if receiving_account_tax_id (nullable) is None
        # and model_fields_set contains the field
        if self.receiving_account_tax_id is None and "receiving_account_tax_id" in self.model_fields_set:
            _dict['receiving_account_tax_id'] = None

        # set to None if reference_number (nullable) is None
        # and model_fields_set contains the field
        if self.reference_number is None and "reference_number" in self.model_fields_set:
            _dict['reference_number'] = None

        # set to None if tracking_code (nullable) is None
        # and model_fields_set contains the field
        if self.tracking_code is None and "tracking_code" in self.model_fields_set:
            _dict['tracking_code'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ChargeDataPaymentMethodBankTransferResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bank": obj.get("bank"),
            "clabe": obj.get("clabe"),
            "description": obj.get("description"),
            "executed_at": obj.get("executed_at"),
            "expires_at": obj.get("expires_at"),
            "issuing_account_bank": obj.get("issuing_account_bank"),
            "issuing_account_number": obj.get("issuing_account_number"),
            "issuing_account_holder_name": obj.get("issuing_account_holder_name"),
            "issuing_account_tax_id": obj.get("issuing_account_tax_id"),
            "payment_attempts": obj.get("payment_attempts"),
            "receiving_account_holder_name": obj.get("receiving_account_holder_name"),
            "receiving_account_number": obj.get("receiving_account_number"),
            "receiving_account_bank": obj.get("receiving_account_bank"),
            "receiving_account_tax_id": obj.get("receiving_account_tax_id"),
            "reference_number": obj.get("reference_number"),
            "tracking_code": obj.get("tracking_code")
        })
        return _obj


