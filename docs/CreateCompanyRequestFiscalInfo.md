# CreateCompanyRequestFiscalInfo

Fiscal information for the company.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_phone** | **str** | The business phone number for fiscal purposes. | [optional] 
**fiscal_type** | **str** | The fiscal type of the company (e.g., &#39;moral&#39;, &#39;persona_fisica&#39;). | [optional] 

## Example

```python
from conekta.models.create_company_request_fiscal_info import CreateCompanyRequestFiscalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCompanyRequestFiscalInfo from a JSON string
create_company_request_fiscal_info_instance = CreateCompanyRequestFiscalInfo.from_json(json)
# print the JSON string representation of the object
print(CreateCompanyRequestFiscalInfo.to_json())

# convert the object into a dict
create_company_request_fiscal_info_dict = create_company_request_fiscal_info_instance.to_dict()
# create an instance of CreateCompanyRequestFiscalInfo from a dict
create_company_request_fiscal_info_from_dict = CreateCompanyRequestFiscalInfo.from_dict(create_company_request_fiscal_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


