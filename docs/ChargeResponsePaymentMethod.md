# ChargeResponsePaymentMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**object** | **str** |  | 
**agreement** | **str** | Agreement ID | [optional] 
**auth_code** | **str** |  | [optional] 
**cashier_id** | **str** |  | [optional] 
**reference** | **str** |  | [optional] 
**barcode_url** | **str** |  | [optional] 
**expires_at** | **int** | Expiration date of the charge | 
**product_type** | **str** | Product type of the charge | 
**service_name** | **str** |  | [optional] 
**store** | **str** |  | [optional] 
**store_name** | **str** |  | [optional] 
**customer_ip_address** | **str** |  | [optional] 
**account_type** | **str** | Account type of the card | [optional] 
**brand** | **str** | Brand of the card | [optional] 
**contract_id** | **str** | Id sent for recurrent charges. | [optional] 
**country** | **str** | Country of the card | [optional] 
**exp_month** | **str** | Expiration month of the card | [optional] 
**exp_year** | **str** | Expiration year of the card | [optional] 
**fraud_indicators** | **List[object]** |  | [optional] 
**issuer** | **str** | Issuer of the card | [optional] 
**last4** | **str** | Last 4 digits of the card | [optional] 
**name** | **str** | Name of the cardholder | [optional] 
**bank** | **str** |  | [optional] 
**clabe** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**executed_at** | **str** |  | [optional] 
**issuing_account_bank** | **str** |  | [optional] 
**issuing_account_number** | **str** |  | [optional] 
**issuing_account_holder_name** | **str** |  | [optional] 
**issuing_account_tax_id** | **str** |  | [optional] 
**payment_attempts** | **List[object]** |  | [optional] 
**receiving_account_holder_name** | **str** |  | [optional] 
**receiving_account_number** | **str** |  | [optional] 
**receiving_account_bank** | **str** |  | [optional] 
**receiving_account_tax_id** | **str** |  | [optional] 
**reference_number** | **str** |  | [optional] 
**tracking_code** | **str** |  | [optional] 
**cancel_url** | **str** | URL to redirect the customer after a canceled payment | [optional] 
**failure_url** | **str** | URL to redirect the customer after a failed payment | [optional] 
**redirect_url** | **str** | URL to redirect the customer to complete the payment | [optional] 
**success_url** | **str** | URL to redirect the customer after a successful payment | [optional] 

## Example

```python
from conekta.models.charge_response_payment_method import ChargeResponsePaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeResponsePaymentMethod from a JSON string
charge_response_payment_method_instance = ChargeResponsePaymentMethod.from_json(json)
# print the JSON string representation of the object
print(ChargeResponsePaymentMethod.to_json())

# convert the object into a dict
charge_response_payment_method_dict = charge_response_payment_method_instance.to_dict()
# create an instance of ChargeResponsePaymentMethod from a dict
charge_response_payment_method_from_dict = ChargeResponsePaymentMethod.from_dict(charge_response_payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


