# CreateCompanyRequestBankAccountInfo

Bank account information for the company.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clabe** | **str** | The 18-digit CLABE for the bank account. | [optional] 

## Example

```python
from conekta.models.create_company_request_bank_account_info import CreateCompanyRequestBankAccountInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCompanyRequestBankAccountInfo from a JSON string
create_company_request_bank_account_info_instance = CreateCompanyRequestBankAccountInfo.from_json(json)
# print the JSON string representation of the object
print(CreateCompanyRequestBankAccountInfo.to_json())

# convert the object into a dict
create_company_request_bank_account_info_dict = create_company_request_bank_account_info_instance.to_dict()
# create an instance of CreateCompanyRequestBankAccountInfo from a dict
create_company_request_bank_account_info_from_dict = CreateCompanyRequestBankAccountInfo.from_dict(create_company_request_bank_account_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


