# DetailsError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**param** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**debug_message** | **str** |  | [optional] 

## Example

```python
from conekta.models.details_error import DetailsError

# TODO update the JSON string below
json = "{}"
# create an instance of DetailsError from a JSON string
details_error_instance = DetailsError.from_json(json)
# print the JSON string representation of the object
print DetailsError.to_json()

# convert the object into a dict
details_error_dict = details_error_instance.to_dict()
# create an instance of DetailsError from a dict
details_error_form_dict = details_error.from_dict(details_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


