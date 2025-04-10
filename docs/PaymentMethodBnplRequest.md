# PaymentMethodBnplRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the payment method | 
**cancel_url** | **str** | URL to redirect the customer after a canceled payment | 
**can_not_expire** | **bool** | Indicates if the payment method can not expire | 
**failure_url** | **str** | URL to redirect the customer after a failed payment | 
**product_type** | **str** | Product type of the payment method, use for the payment method to know the product type | 
**success_url** | **str** | URL to redirect the customer after a successful payment | 

## Example

```python
from conekta.models.payment_method_bnpl_request import PaymentMethodBnplRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodBnplRequest from a JSON string
payment_method_bnpl_request_instance = PaymentMethodBnplRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodBnplRequest.to_json())

# convert the object into a dict
payment_method_bnpl_request_dict = payment_method_bnpl_request_instance.to_dict()
# create an instance of PaymentMethodBnplRequest from a dict
payment_method_bnpl_request_from_dict = PaymentMethodBnplRequest.from_dict(payment_method_bnpl_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


