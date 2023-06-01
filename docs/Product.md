# Product


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

## Example

```python
from conekta.models.product import Product

# TODO update the JSON string below
json = "{}"
# create an instance of Product from a JSON string
product_instance = Product.from_json(json)
# print the JSON string representation of the object
print Product.to_json()

# convert the object into a dict
product_dict = product_instance.to_dict()
# create an instance of Product from a dict
product_form_dict = product.from_dict(product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


