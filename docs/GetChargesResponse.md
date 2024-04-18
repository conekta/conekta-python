# GetChargesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** | Indicates if there are more pages to be requested | 
**object** | **str** | Object type, in this case is list | 
**next_page_url** | **str** | URL of the next page. | [optional] 
**previous_page_url** | **str** | Url of the previous page. | [optional] 
**data** | [**List[ChargeResponse]**](ChargeResponse.md) |  | [optional] 

## Example

```python
from conekta.models.get_charges_response import GetChargesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetChargesResponse from a JSON string
get_charges_response_instance = GetChargesResponse.from_json(json)
# print the JSON string representation of the object
print(GetChargesResponse.to_json())

# convert the object into a dict
get_charges_response_dict = get_charges_response_instance.to_dict()
# create an instance of GetChargesResponse from a dict
get_charges_response_from_dict = GetChargesResponse.from_dict(get_charges_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


