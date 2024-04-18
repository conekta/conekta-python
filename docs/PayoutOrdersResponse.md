# PayoutOrdersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** | Indicates if there are more pages to be requested | 
**object** | **str** | Object type, in this case is list | 
**next_page_url** | **str** | URL of the next page. | [optional] 
**previous_page_url** | **str** | Url of the previous page. | [optional] 
**data** | [**List[PayoutOrderResponse]**](PayoutOrderResponse.md) |  | [optional] 

## Example

```python
from conekta.models.payout_orders_response import PayoutOrdersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutOrdersResponse from a JSON string
payout_orders_response_instance = PayoutOrdersResponse.from_json(json)
# print the JSON string representation of the object
print(PayoutOrdersResponse.to_json())

# convert the object into a dict
payout_orders_response_dict = payout_orders_response_instance.to_dict()
# create an instance of PayoutOrdersResponse from a dict
payout_orders_response_from_dict = PayoutOrdersResponse.from_dict(payout_orders_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


