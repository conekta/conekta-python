# CreateCustomerFiscalEntitiesResponseAllOf


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
from conekta.models.create_customer_fiscal_entities_response_all_of import CreateCustomerFiscalEntitiesResponseAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomerFiscalEntitiesResponseAllOf from a JSON string
create_customer_fiscal_entities_response_all_of_instance = CreateCustomerFiscalEntitiesResponseAllOf.from_json(json)
# print the JSON string representation of the object
print CreateCustomerFiscalEntitiesResponseAllOf.to_json()

# convert the object into a dict
create_customer_fiscal_entities_response_all_of_dict = create_customer_fiscal_entities_response_all_of_instance.to_dict()
# create an instance of CreateCustomerFiscalEntitiesResponseAllOf from a dict
create_customer_fiscal_entities_response_all_of_form_dict = create_customer_fiscal_entities_response_all_of.from_dict(create_customer_fiscal_entities_response_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


