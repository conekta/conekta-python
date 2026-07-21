# FiscalEntityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**FiscalEntityRequestAddress**](FiscalEntityRequestAddress.md) |  | 
**tax_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**company_name** | **str** |  | [optional] 

## Example

```python
from conekta.models.fiscal_entity_request import FiscalEntityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalEntityRequest from a JSON string
fiscal_entity_request_instance = FiscalEntityRequest.from_json(json)
# print the JSON string representation of the object
print(FiscalEntityRequest.to_json())

# convert the object into a dict
fiscal_entity_request_dict = fiscal_entity_request_instance.to_dict()
# create an instance of FiscalEntityRequest from a dict
fiscal_entity_request_from_dict = FiscalEntityRequest.from_dict(fiscal_entity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


