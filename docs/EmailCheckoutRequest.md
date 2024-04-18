# EmailCheckoutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 

## Example

```python
from conekta.models.email_checkout_request import EmailCheckoutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmailCheckoutRequest from a JSON string
email_checkout_request_instance = EmailCheckoutRequest.from_json(json)
# print the JSON string representation of the object
print(EmailCheckoutRequest.to_json())

# convert the object into a dict
email_checkout_request_dict = email_checkout_request_instance.to_dict()
# create an instance of EmailCheckoutRequest from a dict
email_checkout_request_from_dict = EmailCheckoutRequest.from_dict(email_checkout_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


