# TaxLinesDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The amount to be collected for tax in cents | 
**description** | **str** | description or tax&#39;s name | 
**metadata** | **Dict[str, object]** |  | [optional] 
**id** | **str** |  | 
**object** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 

## Example

```python
from conekta.models.tax_lines_data_response import TaxLinesDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaxLinesDataResponse from a JSON string
tax_lines_data_response_instance = TaxLinesDataResponse.from_json(json)
# print the JSON string representation of the object
print(TaxLinesDataResponse.to_json())

# convert the object into a dict
tax_lines_data_response_dict = tax_lines_data_response_instance.to_dict()
# create an instance of TaxLinesDataResponse from a dict
tax_lines_data_response_from_dict = TaxLinesDataResponse.from_dict(tax_lines_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


