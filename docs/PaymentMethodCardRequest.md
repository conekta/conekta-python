# PaymentMethodCardRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of payment method | 
**cvc** | **str** | Card security code | 
**exp_month** | **str** | Card expiration month | 
**exp_year** | **str** | Card expiration year | 
**name** | **str** | Cardholder name | 
**number** | **str** | Card number | 
**customer_ip_address** | **str** | Optional field used to capture the customer&#39;s IP address for fraud prevention and security monitoring purposes | [optional] 

## Example

```python
from conekta.models.payment_method_card_request import PaymentMethodCardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodCardRequest from a JSON string
payment_method_card_request_instance = PaymentMethodCardRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodCardRequest.to_json())

# convert the object into a dict
payment_method_card_request_dict = payment_method_card_request_instance.to_dict()
# create an instance of PaymentMethodCardRequest from a dict
payment_method_card_request_from_dict = PaymentMethodCardRequest.from_dict(payment_method_card_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


