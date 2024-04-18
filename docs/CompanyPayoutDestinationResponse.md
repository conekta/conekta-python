# CompanyPayoutDestinationResponse

Company payout destination model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The resource&#39;s type | [optional] 
**currency** | **str** | currency of the receiving account | [optional] 
**account_holder_name** | **str** | Name of the account holder | [optional] 
**bank** | **str** | Name of the bank | [optional] 
**type** | **str** | Type of the payout destination | [optional] 
**account_number** | **str** | Account number of the receiving account | [optional] 

## Example

```python
from conekta.models.company_payout_destination_response import CompanyPayoutDestinationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyPayoutDestinationResponse from a JSON string
company_payout_destination_response_instance = CompanyPayoutDestinationResponse.from_json(json)
# print the JSON string representation of the object
print(CompanyPayoutDestinationResponse.to_json())

# convert the object into a dict
company_payout_destination_response_dict = company_payout_destination_response_instance.to_dict()
# create an instance of CompanyPayoutDestinationResponse from a dict
company_payout_destination_response_from_dict = CompanyPayoutDestinationResponse.from_dict(company_payout_destination_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


