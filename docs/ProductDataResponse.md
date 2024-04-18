# ProductDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**antifraud_info** | **Dict[str, object]** |  | [optional] 
**brand** | **str** | The brand of the item. | [optional] 
**description** | **str** | Short description of the item | [optional] 
**metadata** | **Dict[str, str]** | It is a key/value hash that can hold custom fields. Maximum 100 elements and allows special characters. | [optional] 
**name** | **str** | The name of the item. It will be displayed in the order. | 
**quantity** | **int** | The quantity of the item in the order. | 
**sku** | **str** | The stock keeping unit for the item. It is used to identify the item in the order. | [optional] 
**tags** | **List[str]** | List of tags for the item. It is used to identify the item in the order. | [optional] 
**unit_price** | **int** | The price of the item in cents. | 
**id** | **str** |  | [optional] 
**object** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 

## Example

```python
from conekta.models.product_data_response import ProductDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProductDataResponse from a JSON string
product_data_response_instance = ProductDataResponse.from_json(json)
# print the JSON string representation of the object
print(ProductDataResponse.to_json())

# convert the object into a dict
product_data_response_dict = product_data_response_instance.to_dict()
# create an instance of ProductDataResponse from a dict
product_data_response_from_dict = ProductDataResponse.from_dict(product_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


