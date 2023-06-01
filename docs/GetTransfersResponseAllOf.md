# GetTransfersResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TransfersResponse]**](TransfersResponse.md) | Transfers | [optional] 

## Example

```python
from conekta.models.get_transfers_response_all_of import GetTransfersResponseAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransfersResponseAllOf from a JSON string
get_transfers_response_all_of_instance = GetTransfersResponseAllOf.from_json(json)
# print the JSON string representation of the object
print GetTransfersResponseAllOf.to_json()

# convert the object into a dict
get_transfers_response_all_of_dict = get_transfers_response_all_of_instance.to_dict()
# create an instance of GetTransfersResponseAllOf from a dict
get_transfers_response_all_of_form_dict = get_transfers_response_all_of.from_dict(get_transfers_response_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


