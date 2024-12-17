# ChargesOrderResponseAllOfData


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
from conekta.models.charges_order_response_all_of_data import ChargesOrderResponseAllOfData

# TODO update the JSON string below
json = "{}"
# create an instance of ChargesOrderResponseAllOfData from a JSON string
charges_order_response_all_of_data_instance = ChargesOrderResponseAllOfData.from_json(json)
# print the JSON string representation of the object
print(ChargesOrderResponseAllOfData.to_json())

# convert the object into a dict
charges_order_response_all_of_data_dict = charges_order_response_all_of_data_instance.to_dict()
# create an instance of ChargesOrderResponseAllOfData from a dict
charges_order_response_all_of_data_from_dict = ChargesOrderResponseAllOfData.from_dict(charges_order_response_all_of_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


