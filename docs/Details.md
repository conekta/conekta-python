# Details


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**List[DetailsError]**](DetailsError.md) |  | [optional] 

## Example

```python
from conekta.models.details import Details

# TODO update the JSON string below
json = "{}"
# create an instance of Details from a JSON string
details_instance = Details.from_json(json)
# print the JSON string representation of the object
print(Details.to_json())

# convert the object into a dict
details_dict = details_instance.to_dict()
# create an instance of Details from a dict
details_from_dict = Details.from_dict(details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


