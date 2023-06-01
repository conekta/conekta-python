# CustomerPaymentMethods


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CustomerPaymentMethodsData]**](CustomerPaymentMethodsData.md) |  | [optional] 

## Example

```python
from conekta.models.customer_payment_methods import CustomerPaymentMethods

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerPaymentMethods from a JSON string
customer_payment_methods_instance = CustomerPaymentMethods.from_json(json)
# print the JSON string representation of the object
print CustomerPaymentMethods.to_json()

# convert the object into a dict
customer_payment_methods_dict = customer_payment_methods_instance.to_dict()
# create an instance of CustomerPaymentMethods from a dict
customer_payment_methods_form_dict = customer_payment_methods.from_dict(customer_payment_methods_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


