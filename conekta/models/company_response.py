# coding: utf-8

"""
    Conekta API

    Conekta sdk  # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Contact: engineering@conekta.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, validator
from conekta.models.company_fiscal_info_response import CompanyFiscalInfoResponse
from conekta.models.company_payout_destination_response import CompanyPayoutDestinationResponse

class CompanyResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[StrictStr] = Field(None, description="The child company's unique identifier")
    created_at: Optional[StrictInt] = Field(None, description="The resource's creation date (unix timestamp)")
    name: Optional[StrictStr] = Field(None, description="The child company's name")
    object: Optional[StrictStr] = Field(None, description="The resource's type")
    parent_company_id: Optional[StrictStr] = Field(None, description="Id of the parent company")
    use_parent_fiscal_data: Optional[StrictBool] = Field(None, description="Whether the parent company's fiscal data is to be used for liquidation and tax purposes")
    payout_destination: Optional[CompanyPayoutDestinationResponse] = None
    fiscal_info: Optional[CompanyFiscalInfoResponse] = None
    __properties = ["id", "created_at", "name", "object", "parent_company_id", "use_parent_fiscal_data", "payout_destination", "fiscal_info"]

    @validator('object')
    def object_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('company'):
            raise ValueError("must validate the enum values ('company')")
        return v

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> CompanyResponse:
        """Create an instance of CompanyResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of payout_destination
        if self.payout_destination:
            _dict['payout_destination'] = self.payout_destination.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fiscal_info
        if self.fiscal_info:
            _dict['fiscal_info'] = self.fiscal_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CompanyResponse:
        """Create an instance of CompanyResponse from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return CompanyResponse.parse_obj(obj)

        _obj = CompanyResponse.parse_obj({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "name": obj.get("name"),
            "object": obj.get("object"),
            "parent_company_id": obj.get("parent_company_id"),
            "use_parent_fiscal_data": obj.get("use_parent_fiscal_data"),
            "payout_destination": CompanyPayoutDestinationResponse.from_dict(obj.get("payout_destination")) if obj.get("payout_destination") is not None else None,
            "fiscal_info": CompanyFiscalInfoResponse.from_dict(obj.get("fiscal_info")) if obj.get("fiscal_info") is not None else None
        })
        return _obj
