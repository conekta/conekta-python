# CreateCompanyRequestComercialInfo

Commercial information for the company.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**website** | **str** | The company&#39;s website URL. | [optional] 
**mcc** | **str** | The Merchant Category Code (MCC) for the company. | [optional] 
**merchant_support_email** | **str** | Email address for merchant support. | [optional] 
**merchant_support_phone** | **str** | Phone number for merchant support. | [optional] 

## Example

```python
from conekta.models.create_company_request_comercial_info import CreateCompanyRequestComercialInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCompanyRequestComercialInfo from a JSON string
create_company_request_comercial_info_instance = CreateCompanyRequestComercialInfo.from_json(json)
# print the JSON string representation of the object
print(CreateCompanyRequestComercialInfo.to_json())

# convert the object into a dict
create_company_request_comercial_info_dict = create_company_request_comercial_info_instance.to_dict()
# create an instance of CreateCompanyRequestComercialInfo from a dict
create_company_request_comercial_info_from_dict = CreateCompanyRequestComercialInfo.from_dict(create_company_request_comercial_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


