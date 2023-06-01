# UpdateCustomerFiscalEntitiesResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**object** | **str** |  | 
**created_at** | **int** |  | 
**parent_id** | **str** |  | [optional] 
**default** | **bool** |  | [optional] 

## Example

```python
from conekta.models.update_customer_fiscal_entities_response_all_of import UpdateCustomerFiscalEntitiesResponseAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomerFiscalEntitiesResponseAllOf from a JSON string
update_customer_fiscal_entities_response_all_of_instance = UpdateCustomerFiscalEntitiesResponseAllOf.from_json(json)
# print the JSON string representation of the object
print UpdateCustomerFiscalEntitiesResponseAllOf.to_json()

# convert the object into a dict
update_customer_fiscal_entities_response_all_of_dict = update_customer_fiscal_entities_response_all_of_instance.to_dict()
# create an instance of UpdateCustomerFiscalEntitiesResponseAllOf from a dict
update_customer_fiscal_entities_response_all_of_form_dict = update_customer_fiscal_entities_response_all_of.from_dict(update_customer_fiscal_entities_response_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


