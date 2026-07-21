# TokenRequestCheckout


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**returns_control_on** | **str** | It is a value that allows identifying the returns control on. | [optional] 

## Example

```python
from conekta.models.token_request_checkout import TokenRequestCheckout

# TODO update the JSON string below
json = "{}"
# create an instance of TokenRequestCheckout from a JSON string
token_request_checkout_instance = TokenRequestCheckout.from_json(json)
# print the JSON string representation of the object
print(TokenRequestCheckout.to_json())

# convert the object into a dict
token_request_checkout_dict = token_request_checkout_instance.to_dict()
# create an instance of TokenRequestCheckout from a dict
token_request_checkout_from_dict = TokenRequestCheckout.from_dict(token_request_checkout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


