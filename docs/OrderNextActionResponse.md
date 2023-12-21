# OrderNextActionResponse

contains the following attributes that will guide to continue the flow

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_to_url** | [**OrderNextActionResponseRedirectToUrl**](OrderNextActionResponseRedirectToUrl.md) |  | [optional] 
**type** | **str** | Indicates the type of action to be taken | [optional] 

## Example

```python
from conekta.models.order_next_action_response import OrderNextActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderNextActionResponse from a JSON string
order_next_action_response_instance = OrderNextActionResponse.from_json(json)
# print the JSON string representation of the object
print OrderNextActionResponse.to_json()

# convert the object into a dict
order_next_action_response_dict = order_next_action_response_instance.to_dict()
# create an instance of OrderNextActionResponse from a dict
order_next_action_response_form_dict = order_next_action_response.from_dict(order_next_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


