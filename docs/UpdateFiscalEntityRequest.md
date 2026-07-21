# UpdateFiscalEntityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**FiscalEntityRequestAddress**](FiscalEntityRequestAddress.md) |  | [optional] 
**tax_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**company_name** | **str** |  | [optional] 

## Example

```python
from conekta.models.update_fiscal_entity_request import UpdateFiscalEntityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFiscalEntityRequest from a JSON string
update_fiscal_entity_request_instance = UpdateFiscalEntityRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateFiscalEntityRequest.to_json())

# convert the object into a dict
update_fiscal_entity_request_dict = update_fiscal_entity_request_instance.to_dict()
# create an instance of UpdateFiscalEntityRequest from a dict
update_fiscal_entity_request_from_dict = UpdateFiscalEntityRequest.from_dict(update_fiscal_entity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


