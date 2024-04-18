# CompanyResponse

Company model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The child company&#39;s unique identifier | [optional] 
**created_at** | **int** | The resource&#39;s creation date (unix timestamp) | [optional] 
**name** | **str** | The child company&#39;s name | [optional] 
**object** | **str** | The resource&#39;s type | [optional] 
**parent_company_id** | **str** | Id of the parent company | [optional] 
**use_parent_fiscal_data** | **bool** | Whether the parent company&#39;s fiscal data is to be used for liquidation and tax purposes | [optional] 
**payout_destination** | [**CompanyPayoutDestinationResponse**](CompanyPayoutDestinationResponse.md) |  | [optional] 
**fiscal_info** | [**CompanyFiscalInfoResponse**](CompanyFiscalInfoResponse.md) |  | [optional] 

## Example

```python
from conekta.models.company_response import CompanyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyResponse from a JSON string
company_response_instance = CompanyResponse.from_json(json)
# print the JSON string representation of the object
print(CompanyResponse.to_json())

# convert the object into a dict
company_response_dict = company_response_instance.to_dict()
# create an instance of CompanyResponse from a dict
company_response_from_dict = CompanyResponse.from_dict(company_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


