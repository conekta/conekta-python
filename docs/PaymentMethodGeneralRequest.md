# PaymentMethodGeneralRequest

Payment method used in the charge. Go to the [payment methods](https://developers.conekta.com/reference/m%C3%A9todos-de-pago) section for more details 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **int** | Method expiration date as unix timestamp | [optional] 
**monthly_installments** | **int** | How many months without interest to apply, it can be 3, 6, 9, 12 or 18 | [optional] 
**type** | **str** | Type of payment method | 
**token_id** | **str** |  | [optional] 
**payment_source_id** | **str** |  | [optional] 
**cvc** | **str** | Optional, It is a value that allows identifying the security code of the card. Only for PCI merchants | [optional] 
**contract_id** | **str** | Optional id sent to indicate the bank contract for recurrent card charges. | [optional] 
**customer_ip_address** | **str** | Optional field used to capture the customer&#39;s IP address for fraud prevention and security monitoring purposes | [optional] 

## Example

```python
from conekta.models.payment_method_general_request import PaymentMethodGeneralRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodGeneralRequest from a JSON string
payment_method_general_request_instance = PaymentMethodGeneralRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodGeneralRequest.to_json())

# convert the object into a dict
payment_method_general_request_dict = payment_method_general_request_instance.to_dict()
# create an instance of PaymentMethodGeneralRequest from a dict
payment_method_general_request_from_dict = PaymentMethodGeneralRequest.from_dict(payment_method_general_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


