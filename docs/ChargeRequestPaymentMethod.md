# ChargeRequestPaymentMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of payment method | 
**cancel_url** | **str** | URL to redirect the customer after a canceled payment | 
**can_not_expire** | **bool** | Indicates if the payment method can not expire | 
**failure_url** | **str** | URL to redirect the customer after a failed payment | 
**product_type** | **str** | Product type of the payment method, use for the payment method to know the product type | 
**success_url** | **str** | URL to redirect the customer after a successful payment | 
**cvc** | **str** | Optional, It is a value that allows identifying the security code of the card. Only for PCI merchants | 
**exp_month** | **str** | Card expiration month | 
**exp_year** | **str** | Card expiration year | 
**name** | **str** | Cardholder name | 
**number** | **str** | Card number | 
**customer_ip_address** | **str** | Optional field used to capture the customer&#39;s IP address for fraud prevention and security monitoring purposes | [optional] 
**expires_at** | **int** | Method expiration date as unix timestamp | [optional] 
**monthly_installments** | **int** | How many months without interest to apply, it can be 3, 6, 9, 12 or 18 | [optional] 
**token_id** | **str** |  | [optional] 
**payment_source_id** | **str** |  | [optional] 
**contract_id** | **str** | Optional id sent to indicate the bank contract for recurrent card charges. | [optional] 

## Example

```python
from conekta.models.charge_request_payment_method import ChargeRequestPaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeRequestPaymentMethod from a JSON string
charge_request_payment_method_instance = ChargeRequestPaymentMethod.from_json(json)
# print the JSON string representation of the object
print(ChargeRequestPaymentMethod.to_json())

# convert the object into a dict
charge_request_payment_method_dict = charge_request_payment_method_instance.to_dict()
# create an instance of ChargeRequestPaymentMethod from a dict
charge_request_payment_method_from_dict = ChargeRequestPaymentMethod.from_dict(charge_request_payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


