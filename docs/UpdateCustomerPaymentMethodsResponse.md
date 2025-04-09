# UpdateCustomerPaymentMethodsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | 
**object** | **str** |  | 
**created_at** | **int** |  | 
**parent_id** | **str** |  | [optional] 
**agreements** | [**List[PaymentMethodCashResponseAllOfAgreements]**](PaymentMethodCashResponseAllOfAgreements.md) |  | [optional] 
**reference** | **str** |  | [optional] 
**barcode** | **str** |  | [optional] 
**barcode_url** | **str** | URL to the barcode image, reference is the same as barcode | [optional] 
**expires_at** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**last4** | **str** |  | [optional] 
**bin** | **str** |  | [optional] 
**card_type** | **str** |  | [optional] 
**exp_month** | **str** |  | [optional] 
**exp_year** | **str** |  | [optional] 
**brand** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**default** | **bool** |  | [optional] 
**visible_on_checkout** | **bool** |  | [optional] 
**payment_source_status** | **str** |  | [optional] 

## Example

```python
from conekta.models.update_customer_payment_methods_response import UpdateCustomerPaymentMethodsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomerPaymentMethodsResponse from a JSON string
update_customer_payment_methods_response_instance = UpdateCustomerPaymentMethodsResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateCustomerPaymentMethodsResponse.to_json())

# convert the object into a dict
update_customer_payment_methods_response_dict = update_customer_payment_methods_response_instance.to_dict()
# create an instance of UpdateCustomerPaymentMethodsResponse from a dict
update_customer_payment_methods_response_from_dict = UpdateCustomerPaymentMethodsResponse.from_dict(update_customer_payment_methods_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


