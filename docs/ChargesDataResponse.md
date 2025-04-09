# ChargesDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** |  | 
**channel** | [**ChargeResponseChannel**](ChargeResponseChannel.md) |  | [optional] 
**created_at** | **int** |  | 
**currency** | **str** |  | 
**customer_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**device_fingerprint** | **str** |  | [optional] 
**failure_code** | **str** |  | [optional] 
**failure_message** | **str** |  | [optional] 
**id** | **str** | Charge ID | 
**livemode** | **bool** | Whether the charge was made in live mode or not | 
**object** | **str** |  | 
**order_id** | **str** | Order ID | 
**paid_at** | **int** | Payment date | [optional] 
**payment_method** | [**ChargeResponsePaymentMethod**](ChargeResponsePaymentMethod.md) |  | [optional] 
**reference_id** | **str** | Reference ID of the charge | [optional] 
**refunds** | [**ChargeResponseRefunds**](ChargeResponseRefunds.md) |  | [optional] 
**status** | **str** | Charge status | 

## Example

```python
from conekta.models.charges_data_response import ChargesDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChargesDataResponse from a JSON string
charges_data_response_instance = ChargesDataResponse.from_json(json)
# print the JSON string representation of the object
print(ChargesDataResponse.to_json())

# convert the object into a dict
charges_data_response_dict = charges_data_response_instance.to_dict()
# create an instance of ChargesDataResponse from a dict
charges_data_response_from_dict = ChargesDataResponse.from_dict(charges_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


