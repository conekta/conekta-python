# BalanceCommonFielsResponse

balance common fields model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The balance&#39;s amount | [optional] 
**currency** | **str** | The balance&#39;s currency | [optional] 

## Example

```python
from conekta.models.balance_common_fiels_response import BalanceCommonFielsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceCommonFielsResponse from a JSON string
balance_common_fiels_response_instance = BalanceCommonFielsResponse.from_json(json)
# print the JSON string representation of the object
print(BalanceCommonFielsResponse.to_json())

# convert the object into a dict
balance_common_fiels_response_dict = balance_common_fiels_response_instance.to_dict()
# create an instance of BalanceCommonFielsResponse from a dict
balance_common_fiels_response_from_dict = BalanceCommonFielsResponse.from_dict(balance_common_fiels_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


