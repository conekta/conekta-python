# ChargesDataResponse


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
**fee** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**livemode** | **bool** |  | [optional] 
**object** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**paid_at** | **int** |  | [optional] 
**payment_method** | [**ChargeResponsePaymentMethod**](ChargeResponsePaymentMethod.md) |  | [optional] 
**reference_id** | **str** | Reference ID of the charge | [optional] 
**refunds** | [**ChargeResponseRefunds**](ChargeResponseRefunds.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from conekta.models.charges_data_response import ChargesDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChargesDataResponse from a JSON string
charges_data_response_instance = ChargesDataResponse.from_json(json)
# print the JSON string representation of the object
print ChargesDataResponse.to_json()

# convert the object into a dict
charges_data_response_dict = charges_data_response_instance.to_dict()
# create an instance of ChargesDataResponse from a dict
charges_data_response_form_dict = charges_data_response.from_dict(charges_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


