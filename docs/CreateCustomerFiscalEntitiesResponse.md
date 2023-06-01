# CreateCustomerFiscalEntitiesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**CustomerFiscalEntitiesRequestAddress**](CustomerFiscalEntitiesRequestAddress.md) |  | 
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
from conekta.models.create_customer_fiscal_entities_response import CreateCustomerFiscalEntitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomerFiscalEntitiesResponse from a JSON string
create_customer_fiscal_entities_response_instance = CreateCustomerFiscalEntitiesResponse.from_json(json)
# print the JSON string representation of the object
print CreateCustomerFiscalEntitiesResponse.to_json()

# convert the object into a dict
create_customer_fiscal_entities_response_dict = create_customer_fiscal_entities_response_instance.to_dict()
# create an instance of CreateCustomerFiscalEntitiesResponse from a dict
create_customer_fiscal_entities_response_form_dict = create_customer_fiscal_entities_response.from_dict(create_customer_fiscal_entities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


