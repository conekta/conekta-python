# ErrorAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_id** | **str** | log id | [optional] 
**type** | **str** |  | [optional] 
**object** | **str** |  | [optional] 

## Example

```python
from conekta.models.error_all_of import ErrorAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorAllOf from a JSON string
error_all_of_instance = ErrorAllOf.from_json(json)
# print the JSON string representation of the object
print ErrorAllOf.to_json()

# convert the object into a dict
error_all_of_dict = error_all_of_instance.to_dict()
# create an instance of ErrorAllOf from a dict
error_all_of_form_dict = error_all_of.from_dict(error_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


