# ChargeResponse


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
**id** | **str** | Charge ID | [optional] 
**livemode** | **bool** | Whether the charge was made in live mode or not | [optional] 
**object** | **str** |  | [optional] 
**order_id** | **str** | Order ID | [optional] 
**paid_at** | **int** | Payment date | [optional] 
**payment_method** | [**ChargeResponsePaymentMethod**](ChargeResponsePaymentMethod.md) |  | [optional] 
**reference_id** | **str** | Reference ID of the charge | [optional] 
**refunds** | [**ChargeResponseRefunds**](ChargeResponseRefunds.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from conekta.models.charge_response import ChargeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeResponse from a JSON string
charge_response_instance = ChargeResponse.from_json(json)
# print the JSON string representation of the object
print(ChargeResponse.to_json())

# convert the object into a dict
charge_response_dict = charge_response_instance.to_dict()
# create an instance of ChargeResponse from a dict
charge_response_from_dict = ChargeResponse.from_dict(charge_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


