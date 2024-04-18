# GetTransactionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** | Indicates if there are more pages to be requested | 
**object** | **str** | Object type, in this case is list | 
**next_page_url** | **str** | URL of the next page. | [optional] 
**previous_page_url** | **str** | Url of the previous page. | [optional] 
**data** | [**List[TransactionResponse]**](TransactionResponse.md) | Transactions | [optional] 

## Example

```python
from conekta.models.get_transactions_response import GetTransactionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionsResponse from a JSON string
get_transactions_response_instance = GetTransactionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetTransactionsResponse.to_json())

# convert the object into a dict
get_transactions_response_dict = get_transactions_response_instance.to_dict()
# create an instance of GetTransactionsResponse from a dict
get_transactions_response_from_dict = GetTransactionsResponse.from_dict(get_transactions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


