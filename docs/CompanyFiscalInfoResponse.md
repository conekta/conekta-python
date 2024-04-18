# CompanyFiscalInfoResponse

Company fiscal info model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The resource&#39;s type | [optional] 
**tax_id** | **str** | Tax ID of the company | [optional] 
**legal_entity_name** | **str** | Legal name of the company | [optional] 
**business_type** | **str** | Business type of the company | [optional] 
**phone** | **str** | Phone number of the company | [optional] 
**physical_person_business_type** | **str** | Business type if &#39;persona_fisica&#39; | [optional] 
**address** | [**CompanyFiscalInfoAddressResponse**](CompanyFiscalInfoAddressResponse.md) |  | [optional] 

## Example

```python
from conekta.models.company_fiscal_info_response import CompanyFiscalInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyFiscalInfoResponse from a JSON string
company_fiscal_info_response_instance = CompanyFiscalInfoResponse.from_json(json)
# print the JSON string representation of the object
print(CompanyFiscalInfoResponse.to_json())

# convert the object into a dict
company_fiscal_info_response_dict = company_fiscal_info_response_instance.to_dict()
# create an instance of CompanyFiscalInfoResponse from a dict
company_fiscal_info_response_from_dict = CompanyFiscalInfoResponse.from_dict(company_fiscal_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


