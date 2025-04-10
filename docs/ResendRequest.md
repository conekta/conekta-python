# ResendRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhooks_ids** | **List[str]** | webhooks ids to resend event | 

## Example

```python
from conekta.models.resend_request import ResendRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResendRequest from a JSON string
resend_request_instance = ResendRequest.from_json(json)
# print the JSON string representation of the object
print(ResendRequest.to_json())

# convert the object into a dict
resend_request_dict = resend_request_instance.to_dict()
# create an instance of ResendRequest from a dict
resend_request_from_dict = ResendRequest.from_dict(resend_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


