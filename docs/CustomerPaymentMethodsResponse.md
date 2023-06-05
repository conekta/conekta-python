# CustomerPaymentMethodsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** | Indicates if there are more pages to be requested | 
**object** | **str** | Object type, in this case is list | 
**next_page_url** | **str** | URL of the next page. | [optional] 
**previous_page_url** | **str** | Url of the previous page. | [optional] 
**data** | [**List[CustomerPaymentMethodsData]**](CustomerPaymentMethodsData.md) |  | [optional] 

## Example

```python
from conekta.models.customer_payment_methods_response import CustomerPaymentMethodsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerPaymentMethodsResponse from a JSON string
customer_payment_methods_response_instance = CustomerPaymentMethodsResponse.from_json(json)
# print the JSON string representation of the object
print CustomerPaymentMethodsResponse.to_json()

# convert the object into a dict
customer_payment_methods_response_dict = customer_payment_methods_response_instance.to_dict()
# create an instance of CustomerPaymentMethodsResponse from a dict
customer_payment_methods_response_form_dict = customer_payment_methods_response.from_dict(customer_payment_methods_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


