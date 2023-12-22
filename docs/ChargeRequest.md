# ChargeRequest

The charges to be made

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** |  | [optional] 
**payment_method** | [**ChargeRequestPaymentMethod**](ChargeRequestPaymentMethod.md) |  | 
**reference_id** | **str** | Custom reference to add to the charge | [optional] 

## Example

```python
from conekta.models.charge_request import ChargeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeRequest from a JSON string
charge_request_instance = ChargeRequest.from_json(json)
# print the JSON string representation of the object
print ChargeRequest.to_json()

# convert the object into a dict
charge_request_dict = charge_request_instance.to_dict()
# create an instance of ChargeRequest from a dict
charge_request_form_dict = charge_request.from_dict(charge_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


