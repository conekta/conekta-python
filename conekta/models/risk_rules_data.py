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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class RiskRulesData(BaseModel):
    """
    RiskRulesData
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="rule id")
    field: Optional[StrictStr] = Field(default=None, description="field to be used for the rule")
    created_at: Optional[StrictStr] = Field(default=None, description="rule creation date")
    value: Optional[StrictStr] = Field(default=None, description="value to be used for the rule")
    is_global: Optional[StrictBool] = Field(default=None, description="if the rule is global")
    is_test: Optional[StrictBool] = Field(default=None, description="if the rule is test")
    description: Optional[StrictStr] = Field(default=None, description="description of the rule")
    __properties: ClassVar[List[str]] = ["id", "field", "created_at", "value", "is_global", "is_test", "description"]

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
        """Create an instance of RiskRulesData from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of RiskRulesData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "field": obj.get("field"),
            "created_at": obj.get("created_at"),
            "value": obj.get("value"),
            "is_global": obj.get("is_global"),
            "is_test": obj.get("is_test"),
            "description": obj.get("description")
        })
        return _obj


