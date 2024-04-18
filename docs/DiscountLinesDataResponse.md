# DiscountLinesDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The amount to be deducted from the total sum of all payments, in cents. | 
**code** | **str** | Discount code. | 
**type** | **str** | It can be &#39;loyalty&#39;, &#39;campaign&#39;, &#39;coupon&#39; o &#39;sign&#39; | 
**id** | **str** | The discount line id | 
**object** | **str** | The object name | 
**parent_id** | **str** | The order id | 

## Example

```python
from conekta.models.discount_lines_data_response import DiscountLinesDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountLinesDataResponse from a JSON string
discount_lines_data_response_instance = DiscountLinesDataResponse.from_json(json)
# print the JSON string representation of the object
print(DiscountLinesDataResponse.to_json())

# convert the object into a dict
discount_lines_data_response_dict = discount_lines_data_response_instance.to_dict()
# create an instance of DiscountLinesDataResponse from a dict
discount_lines_data_response_from_dict = DiscountLinesDataResponse.from_dict(discount_lines_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


