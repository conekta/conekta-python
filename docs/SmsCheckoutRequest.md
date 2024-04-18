# SmsCheckoutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phonenumber** | **str** |  | 

## Example

```python
from conekta.models.sms_checkout_request import SmsCheckoutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SmsCheckoutRequest from a JSON string
sms_checkout_request_instance = SmsCheckoutRequest.from_json(json)
# print the JSON string representation of the object
print(SmsCheckoutRequest.to_json())

# convert the object into a dict
sms_checkout_request_dict = sms_checkout_request_instance.to_dict()
# create an instance of SmsCheckoutRequest from a dict
sms_checkout_request_from_dict = SmsCheckoutRequest.from_dict(sms_checkout_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


