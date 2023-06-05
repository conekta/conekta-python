# GetEventsResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EventResponse]**](EventResponse.md) |  | [optional] 

## Example

```python
from conekta.models.get_events_response_all_of import GetEventsResponseAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetEventsResponseAllOf from a JSON string
get_events_response_all_of_instance = GetEventsResponseAllOf.from_json(json)
# print the JSON string representation of the object
print GetEventsResponseAllOf.to_json()

# convert the object into a dict
get_events_response_all_of_dict = get_events_response_all_of_instance.to_dict()
# create an instance of GetEventsResponseAllOf from a dict
get_events_response_all_of_form_dict = get_events_response_all_of.from_dict(get_events_response_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


