# ChargeOrderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** |  | [optional] 
**channel** | [**ChargeResponseChannel**](ChargeResponseChannel.md) |  | [optional] 
**created_at** | **int** |  | [optional] 
**currency** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**device_fingerprint** | **str** |  | [optional] 
**failure_code** | **str** |  | [optional] 
**failure_message** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**livemode** | **bool** |  | [optional] 
**monthly_installments** | **int** |  | [optional] 
**object** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**paid_at** | **int** |  | [optional] 
**payment_method** | [**ChargeOrderResponsePaymentMethod**](ChargeOrderResponsePaymentMethod.md) |  | [optional] 
**reference_id** | **str** | Reference ID of the charge | [optional] 
**refunds** | **List[object]** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from conekta.models.charge_order_response import ChargeOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeOrderResponse from a JSON string
charge_order_response_instance = ChargeOrderResponse.from_json(json)
# print the JSON string representation of the object
print(ChargeOrderResponse.to_json())

# convert the object into a dict
charge_order_response_dict = charge_order_response_instance.to_dict()
# create an instance of ChargeOrderResponse from a dict
charge_order_response_from_dict = ChargeOrderResponse.from_dict(charge_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


