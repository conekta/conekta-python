# CustomerFiscalEntitiesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**CustomerAddress**](CustomerAddress.md) |  | 
**tax_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**company_name** | **str** |  | [optional] 

## Example

```python
from conekta.models.customer_fiscal_entities_request import CustomerFiscalEntitiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerFiscalEntitiesRequest from a JSON string
customer_fiscal_entities_request_instance = CustomerFiscalEntitiesRequest.from_json(json)
# print the JSON string representation of the object
print(CustomerFiscalEntitiesRequest.to_json())

# convert the object into a dict
customer_fiscal_entities_request_dict = customer_fiscal_entities_request_instance.to_dict()
# create an instance of CustomerFiscalEntitiesRequest from a dict
customer_fiscal_entities_request_from_dict = CustomerFiscalEntitiesRequest.from_dict(customer_fiscal_entities_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


