# CheckoutRequest

[Checkout](https://developers.conekta.com/reference/checkout) details 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_payment_methods** | **List[str]** | Are the payment methods available for this link | 
**expires_at** | **int** | Unix timestamp of checkout expiration | [optional] 
**failure_url** | **str** | Redirection url back to the site in case of failed payment, applies only to HostedPayment. | [optional] 
**monthly_installments_enabled** | **bool** |  | [optional] 
**monthly_installments_options** | **List[int]** |  | [optional] 
**name** | **str** | Reason for payment | [optional] 
**on_demand_enabled** | **bool** |  | [optional] 
**success_url** | **str** | Redirection url back to the site in case of successful payment, applies only to HostedPayment | [optional] 
**type** | **str** | This field represents the type of checkout | [optional] 

## Example

```python
from conekta.models.checkout_request import CheckoutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutRequest from a JSON string
checkout_request_instance = CheckoutRequest.from_json(json)
# print the JSON string representation of the object
print CheckoutRequest.to_json()

# convert the object into a dict
checkout_request_dict = checkout_request_instance.to_dict()
# create an instance of CheckoutRequest from a dict
checkout_request_form_dict = checkout_request.from_dict(checkout_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


