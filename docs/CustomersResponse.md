# CustomersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** | Indicates if there are more pages to be requested | 
**object** | **str** | Object type, in this case is list | 
**next_page_url** | **str** | URL of the next page. | [optional] 
**previous_page_url** | **str** | Url of the previous page. | [optional] 
**data** | [**List[CustomerResponse]**](CustomerResponse.md) |  | [optional] 

## Example

```python
from conekta.models.customers_response import CustomersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomersResponse from a JSON string
customers_response_instance = CustomersResponse.from_json(json)
# print the JSON string representation of the object
print(CustomersResponse.to_json())

# convert the object into a dict
customers_response_dict = customers_response_instance.to_dict()
# create an instance of CustomersResponse from a dict
customers_response_from_dict = CustomersResponse.from_dict(customers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


