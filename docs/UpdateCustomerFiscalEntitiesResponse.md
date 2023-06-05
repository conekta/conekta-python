# UpdateCustomerFiscalEntitiesResponse


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
from conekta.models.update_customer_fiscal_entities_response import UpdateCustomerFiscalEntitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomerFiscalEntitiesResponse from a JSON string
update_customer_fiscal_entities_response_instance = UpdateCustomerFiscalEntitiesResponse.from_json(json)
# print the JSON string representation of the object
print UpdateCustomerFiscalEntitiesResponse.to_json()

# convert the object into a dict
update_customer_fiscal_entities_response_dict = update_customer_fiscal_entities_response_instance.to_dict()
# create an instance of UpdateCustomerFiscalEntitiesResponse from a dict
update_customer_fiscal_entities_response_form_dict = update_customer_fiscal_entities_response.from_dict(update_customer_fiscal_entities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


