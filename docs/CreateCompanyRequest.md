# CreateCompanyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the company. | [optional] 
**type_company** | **str** | The type of company, &#39;owner&#39; | [optional] 
**comercial_info** | [**CreateCompanyRequestComercialInfo**](CreateCompanyRequestComercialInfo.md) |  | [optional] 
**fiscal_info** | [**CreateCompanyRequestFiscalInfo**](CreateCompanyRequestFiscalInfo.md) |  | [optional] 
**bank_account_info** | [**CreateCompanyRequestBankAccountInfo**](CreateCompanyRequestBankAccountInfo.md) |  | [optional] 

## Example

```python
from conekta.models.create_company_request import CreateCompanyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCompanyRequest from a JSON string
create_company_request_instance = CreateCompanyRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCompanyRequest.to_json())

# convert the object into a dict
create_company_request_dict = create_company_request_instance.to_dict()
# create an instance of CreateCompanyRequest from a dict
create_company_request_from_dict = CreateCompanyRequest.from_dict(create_company_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


