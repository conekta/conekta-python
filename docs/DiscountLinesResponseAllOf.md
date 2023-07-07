# DiscountLinesResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The discount line id | 
**object** | **str** | The object name | 
**parent_id** | **str** | The order id | 

## Example

```python
from conekta.models.discount_lines_response_all_of import DiscountLinesResponseAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountLinesResponseAllOf from a JSON string
discount_lines_response_all_of_instance = DiscountLinesResponseAllOf.from_json(json)
# print the JSON string representation of the object
print DiscountLinesResponseAllOf.to_json()

# convert the object into a dict
discount_lines_response_all_of_dict = discount_lines_response_all_of_instance.to_dict()
# create an instance of DiscountLinesResponseAllOf from a dict
discount_lines_response_all_of_form_dict = discount_lines_response_all_of.from_dict(discount_lines_response_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


