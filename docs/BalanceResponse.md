# BalanceResponse

balance model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | [**List[BalanceCommonField]**](BalanceCommonField.md) | The balance&#39;s available | [optional] 
**cashout_retention_amount** | [**List[BalanceCommonField]**](BalanceCommonField.md) | The balance&#39;s cashout retention amount | [optional] 
**conekta_retention** | [**List[BalanceCommonField]**](BalanceCommonField.md) | The balance&#39;s conekta retention | [optional] 
**gateway** | [**List[BalanceCommonField]**](BalanceCommonField.md) | The balance&#39;s gateway | [optional] 
**pending** | [**List[BalanceCommonField]**](BalanceCommonField.md) | The balance&#39;s pending | [optional] 
**retained** | [**List[BalanceCommonField]**](BalanceCommonField.md) | The balance&#39;s retained | [optional] 
**retention_amount** | [**List[BalanceCommonField]**](BalanceCommonField.md) | The balance&#39;s retention amount | [optional] 
**target_collateral_amount** | **object** | The balance&#39;s target collateral amount | [optional] 
**target_retention_amount** | [**List[BalanceCommonField]**](BalanceCommonField.md) | The balance&#39;s target retention amount | [optional] 
**temporarily_retained** | [**List[BalanceCommonField]**](BalanceCommonField.md) | The balance&#39;s temporarily retained | [optional] 

## Example

```python
from conekta.models.balance_response import BalanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceResponse from a JSON string
balance_response_instance = BalanceResponse.from_json(json)
# print the JSON string representation of the object
print(BalanceResponse.to_json())

# convert the object into a dict
balance_response_dict = balance_response_instance.to_dict()
# create an instance of BalanceResponse from a dict
balance_response_from_dict = BalanceResponse.from_dict(balance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


