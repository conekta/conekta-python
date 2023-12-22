# OrderNextActionResponseRedirectToUrl

contains the following attributes that will guide to continue the flow

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | pay.conekta.com/{id} Indicates the url of the Conekta component to authenticate the flow through 3DS2. | [optional] 
**return_url** | **str** | Indicates the url to which the 3DS2 flow returns at the end, when the integration is redirected. | [optional] 

## Example

```python
from conekta.models.order_next_action_response_redirect_to_url import OrderNextActionResponseRedirectToUrl

# TODO update the JSON string below
json = "{}"
# create an instance of OrderNextActionResponseRedirectToUrl from a JSON string
order_next_action_response_redirect_to_url_instance = OrderNextActionResponseRedirectToUrl.from_json(json)
# print the JSON string representation of the object
print OrderNextActionResponseRedirectToUrl.to_json()

# convert the object into a dict
order_next_action_response_redirect_to_url_dict = order_next_action_response_redirect_to_url_instance.to_dict()
# create an instance of OrderNextActionResponseRedirectToUrl from a dict
order_next_action_response_redirect_to_url_form_dict = order_next_action_response_redirect_to_url.from_dict(order_next_action_response_redirect_to_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


