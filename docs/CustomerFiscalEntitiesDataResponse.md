# CustomerFiscalEntitiesDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**CustomerAddress**](CustomerAddress.md) |  | 
**tax_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**company_name** | **str** |  | [optional] 
**id** | **str** |  | 
**object** | **str** |  | 
**created_at** | **int** |  | 
**parent_id** | **str** |  | [optional] 
**default** | **bool** |  | [optional] 

## Example

```python
from conekta.models.customer_fiscal_entities_data_response import CustomerFiscalEntitiesDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerFiscalEntitiesDataResponse from a JSON string
customer_fiscal_entities_data_response_instance = CustomerFiscalEntitiesDataResponse.from_json(json)
# print the JSON string representation of the object
print(CustomerFiscalEntitiesDataResponse.to_json())

# convert the object into a dict
customer_fiscal_entities_data_response_dict = customer_fiscal_entities_data_response_instance.to_dict()
# create an instance of CustomerFiscalEntitiesDataResponse from a dict
customer_fiscal_entities_data_response_from_dict = CustomerFiscalEntitiesDataResponse.from_dict(customer_fiscal_entities_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


