# ChargeUpdateRequest

requested field for update a charge

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_id** | **str** | custom reference id | [optional] 

## Example

```python
from conekta.models.charge_update_request import ChargeUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeUpdateRequest from a JSON string
charge_update_request_instance = ChargeUpdateRequest.from_json(json)
# print the JSON string representation of the object
print ChargeUpdateRequest.to_json()

# convert the object into a dict
charge_update_request_dict = charge_update_request_instance.to_dict()
# create an instance of ChargeUpdateRequest from a dict
charge_update_request_form_dict = charge_update_request.from_dict(charge_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


