# UpdateProduct


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**antifraud_info** | **Dict[str, object]** |  | [optional] 
**description** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**unit_price** | **int** |  | [optional] 
**quantity** | **int** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**brand** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 

## Example

```python
from conekta.models.update_product import UpdateProduct

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProduct from a JSON string
update_product_instance = UpdateProduct.from_json(json)
# print the JSON string representation of the object
print UpdateProduct.to_json()

# convert the object into a dict
update_product_dict = update_product_instance.to_dict()
# create an instance of UpdateProduct from a dict
update_product_form_dict = update_product.from_dict(update_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


