# CashAgreementsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agreement** | **str** | Agreement number, you can use this number to pay in the store/bbva | [optional] 
**provider** | **str** | Provider name, you can use this to know where to pay | [optional] 

## Example

```python
from conekta.models.cash_agreements_response import CashAgreementsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CashAgreementsResponse from a JSON string
cash_agreements_response_instance = CashAgreementsResponse.from_json(json)
# print the JSON string representation of the object
print(CashAgreementsResponse.to_json())

# convert the object into a dict
cash_agreements_response_dict = cash_agreements_response_instance.to_dict()
# create an instance of CashAgreementsResponse from a dict
cash_agreements_response_from_dict = CashAgreementsResponse.from_dict(cash_agreements_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


