# TokenCheckout


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**returns_control_on** | **str** | It is a value that allows identifying the returns control on. | [optional] 

## Example

```python
from conekta.models.token_checkout import TokenCheckout

# TODO update the JSON string below
json = "{}"
# create an instance of TokenCheckout from a JSON string
token_checkout_instance = TokenCheckout.from_json(json)
# print the JSON string representation of the object
print TokenCheckout.to_json()

# convert the object into a dict
token_checkout_dict = token_checkout_instance.to_dict()
# create an instance of TokenCheckout from a dict
token_checkout_form_dict = token_checkout.from_dict(token_checkout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


