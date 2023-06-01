# CheckoutsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** | Indicates if there are more pages to be requested | 
**object** | **str** | Object type, in this case is list | 
**next_page_url** | **str** | URL of the next page. | [optional] 
**previous_page_url** | **str** | Url of the previous page. | [optional] 
**data** | [**List[CheckoutResponse]**](CheckoutResponse.md) |  | [optional] 

## Example

```python
from conekta.models.checkouts_response import CheckoutsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutsResponse from a JSON string
checkouts_response_instance = CheckoutsResponse.from_json(json)
# print the JSON string representation of the object
print CheckoutsResponse.to_json()

# convert the object into a dict
checkouts_response_dict = checkouts_response_instance.to_dict()
# create an instance of CheckoutsResponse from a dict
checkouts_response_form_dict = checkouts_response.from_dict(checkouts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


