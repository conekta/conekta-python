# OrderResponseProductsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ProductDataResponse]**](ProductDataResponse.md) |  | [optional] 

## Example

```python
from conekta.models.order_response_products_all_of import OrderResponseProductsAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of OrderResponseProductsAllOf from a JSON string
order_response_products_all_of_instance = OrderResponseProductsAllOf.from_json(json)
# print the JSON string representation of the object
print OrderResponseProductsAllOf.to_json()

# convert the object into a dict
order_response_products_all_of_dict = order_response_products_all_of_instance.to_dict()
# create an instance of OrderResponseProductsAllOf from a dict
order_response_products_all_of_form_dict = order_response_products_all_of.from_dict(order_response_products_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


