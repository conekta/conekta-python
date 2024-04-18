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
import json
from enum import Enum
from typing_extensions import Self


class EventTypes(str, Enum):
    """
    It is a parameter that allows to identify in the response, the type of event that is being generated.
    """

    """
    allowed enum values
    """
    WEBHOOK_PING = 'webhook_ping'
    ORDER_DOT_PAID = 'order.paid'
    ORDER_DOT_EXPIRED = 'order.expired'
    ORDER_DOT_CANCELED = 'order.canceled'
    ORDER_DOT_PENDING_PAYMENT = 'order.pending_payment'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EventTypes from a JSON string"""
        return cls(json.loads(json_str))

