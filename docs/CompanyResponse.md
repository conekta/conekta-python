# CompanyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the company. | 
**name** | **str** | The name of the company. | 
**active** | **bool** | Indicates if the company is active. | 
**account_status** | **str** | The current status of the company&#39;s account. | 
**parent_company_id** | **str** | The identifier of the parent company, if any. | [optional] 
**onboarding_status** | **str** | The current status of the company&#39;s onboarding process. | 
**documents** | [**List[CompanyResponseDocumentsInner]**](CompanyResponseDocumentsInner.md) | A list of documents related to the company. | 
**created_at** | **int** | Timestamp of when the company was created. | 
**object** | **str** | The type of object, typically \&quot;company\&quot;. | 

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


