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
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from conekta.models.payment_method_bank_transfer import PaymentMethodBankTransfer
from conekta.models.payment_method_bnpl_payment import PaymentMethodBnplPayment
from conekta.models.payment_method_card import PaymentMethodCard
from conekta.models.payment_method_cash import PaymentMethodCash
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

CHARGERESPONSEPAYMENTMETHOD_ONE_OF_SCHEMAS = ["PaymentMethodBankTransfer", "PaymentMethodBnplPayment", "PaymentMethodCard", "PaymentMethodCash"]

class ChargeResponsePaymentMethod(BaseModel):
    """
    ChargeResponsePaymentMethod
    """
    # data type: PaymentMethodCash
    oneof_schema_1_validator: Optional[PaymentMethodCash] = None
    # data type: PaymentMethodCard
    oneof_schema_2_validator: Optional[PaymentMethodCard] = None
    # data type: PaymentMethodBankTransfer
    oneof_schema_3_validator: Optional[PaymentMethodBankTransfer] = None
    # data type: PaymentMethodBnplPayment
    oneof_schema_4_validator: Optional[PaymentMethodBnplPayment] = None
    actual_instance: Optional[Union[PaymentMethodBankTransfer, PaymentMethodBnplPayment, PaymentMethodCard, PaymentMethodCash]] = None
    one_of_schemas: Set[str] = { "PaymentMethodBankTransfer", "PaymentMethodBnplPayment", "PaymentMethodCard", "PaymentMethodCash" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = ChargeResponsePaymentMethod.model_construct()
        error_messages = []
        match = 0
        # validate data type: PaymentMethodCash
        if not isinstance(v, PaymentMethodCash):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PaymentMethodCash`")
        else:
            match += 1
        # validate data type: PaymentMethodCard
        if not isinstance(v, PaymentMethodCard):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PaymentMethodCard`")
        else:
            match += 1
        # validate data type: PaymentMethodBankTransfer
        if not isinstance(v, PaymentMethodBankTransfer):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PaymentMethodBankTransfer`")
        else:
            match += 1
        # validate data type: PaymentMethodBnplPayment
        if not isinstance(v, PaymentMethodBnplPayment):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PaymentMethodBnplPayment`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ChargeResponsePaymentMethod with oneOf schemas: PaymentMethodBankTransfer, PaymentMethodBnplPayment, PaymentMethodCard, PaymentMethodCash. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ChargeResponsePaymentMethod with oneOf schemas: PaymentMethodBankTransfer, PaymentMethodBnplPayment, PaymentMethodCard, PaymentMethodCash. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # use oneOf discriminator to lookup the data type
        _data_type = json.loads(json_str).get("object")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `object` in the input.")

        # check if data type is `PaymentMethodBankTransfer`
        if _data_type == "bank_transfer_payment":
            instance.actual_instance = PaymentMethodBankTransfer.from_json(json_str)
            return instance

        # check if data type is `PaymentMethodBnplPayment`
        if _data_type == "bnpl_payment":
            instance.actual_instance = PaymentMethodBnplPayment.from_json(json_str)
            return instance

        # check if data type is `PaymentMethodCard`
        if _data_type == "card_payment":
            instance.actual_instance = PaymentMethodCard.from_json(json_str)
            return instance

        # check if data type is `PaymentMethodCash`
        if _data_type == "cash_payment":
            instance.actual_instance = PaymentMethodCash.from_json(json_str)
            return instance

        # check if data type is `PaymentMethodBankTransfer`
        if _data_type == "payment_method_bank_transfer":
            instance.actual_instance = PaymentMethodBankTransfer.from_json(json_str)
            return instance

        # check if data type is `PaymentMethodBnplPayment`
        if _data_type == "payment_method_bnpl_payment":
            instance.actual_instance = PaymentMethodBnplPayment.from_json(json_str)
            return instance

        # check if data type is `PaymentMethodCard`
        if _data_type == "payment_method_card":
            instance.actual_instance = PaymentMethodCard.from_json(json_str)
            return instance

        # check if data type is `PaymentMethodCash`
        if _data_type == "payment_method_cash":
            instance.actual_instance = PaymentMethodCash.from_json(json_str)
            return instance

        # deserialize data into PaymentMethodCash
        try:
            instance.actual_instance = PaymentMethodCash.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PaymentMethodCard
        try:
            instance.actual_instance = PaymentMethodCard.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PaymentMethodBankTransfer
        try:
            instance.actual_instance = PaymentMethodBankTransfer.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PaymentMethodBnplPayment
        try:
            instance.actual_instance = PaymentMethodBnplPayment.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ChargeResponsePaymentMethod with oneOf schemas: PaymentMethodBankTransfer, PaymentMethodBnplPayment, PaymentMethodCard, PaymentMethodCash. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ChargeResponsePaymentMethod with oneOf schemas: PaymentMethodBankTransfer, PaymentMethodBnplPayment, PaymentMethodCard, PaymentMethodCash. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], PaymentMethodBankTransfer, PaymentMethodBnplPayment, PaymentMethodCard, PaymentMethodCash]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


