# CustomerFiscalEntitiesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** | Indicates if there are more pages to be requested | 
**object** | **str** | Object type, in this case is list | 
**data** | [**List[CustomerFiscalEntitiesDataResponse]**](CustomerFiscalEntitiesDataResponse.md) |  | [optional] 

## Example

```python
from conekta.models.customer_fiscal_entities_response import CustomerFiscalEntitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerFiscalEntitiesResponse from a JSON string
customer_fiscal_entities_response_instance = CustomerFiscalEntitiesResponse.from_json(json)
# print the JSON string representation of the object
print(CustomerFiscalEntitiesResponse.to_json())

# convert the object into a dict
customer_fiscal_entities_response_dict = customer_fiscal_entities_response_instance.to_dict()
# create an instance of CustomerFiscalEntitiesResponse from a dict
customer_fiscal_entities_response_from_dict = CustomerFiscalEntitiesResponse.from_dict(customer_fiscal_entities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


