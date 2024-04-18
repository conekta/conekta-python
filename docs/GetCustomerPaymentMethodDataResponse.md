# GetCustomerPaymentMethodDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | 
**object** | **str** |  | 
**created_at** | **int** |  | 
**parent_id** | **str** |  | [optional] 
**reference** | **str** |  | [optional] 
**barcode** | **str** |  | [optional] 
**barcode_url** | **str** |  | [optional] 
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
from conekta.models.get_customer_payment_method_data_response import GetCustomerPaymentMethodDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCustomerPaymentMethodDataResponse from a JSON string
get_customer_payment_method_data_response_instance = GetCustomerPaymentMethodDataResponse.from_json(json)
# print the JSON string representation of the object
print(GetCustomerPaymentMethodDataResponse.to_json())

# convert the object into a dict
get_customer_payment_method_data_response_dict = get_customer_payment_method_data_response_instance.to_dict()
# create an instance of GetCustomerPaymentMethodDataResponse from a dict
get_customer_payment_method_data_response_from_dict = GetCustomerPaymentMethodDataResponse.from_dict(get_customer_payment_method_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


