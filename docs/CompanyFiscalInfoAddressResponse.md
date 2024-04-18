# CompanyFiscalInfoAddressResponse

Company fiscal info address model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The resource&#39;s type | [optional] 
**street1** | **str** | Street Address | [optional] 
**street2** | **str** | Colonia | [optional] 
**city** | **str** | City | [optional] 
**state** | **str** | State | [optional] 
**country** | **str** | Country | [optional] 
**postal_code** | **str** | Postal code | [optional] 
**external_number** | **str** | Street number | [optional] 
**internal_number** | **str** | Unit / apartment number | [optional] 

## Example

```python
from conekta.models.company_fiscal_info_address_response import CompanyFiscalInfoAddressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyFiscalInfoAddressResponse from a JSON string
company_fiscal_info_address_response_instance = CompanyFiscalInfoAddressResponse.from_json(json)
# print the JSON string representation of the object
print(CompanyFiscalInfoAddressResponse.to_json())

# convert the object into a dict
company_fiscal_info_address_response_dict = company_fiscal_info_address_response_instance.to_dict()
# create an instance of CompanyFiscalInfoAddressResponse from a dict
company_fiscal_info_address_response_from_dict = CompanyFiscalInfoAddressResponse.from_dict(company_fiscal_info_address_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


