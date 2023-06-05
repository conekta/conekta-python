# OrderResponseProducts


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** | Indicates if there are more pages to be requested | 
**object** | **str** | Object type, in this case is list | 
**next_page_url** | **str** | URL of the next page. | [optional] 
**previous_page_url** | **str** | Url of the previous page. | [optional] 
**data** | [**List[ProductDataResponse]**](ProductDataResponse.md) |  | [optional] 

## Example

```python
from conekta.models.order_response_products import OrderResponseProducts

# TODO update the JSON string below
json = "{}"
# create an instance of OrderResponseProducts from a JSON string
order_response_products_instance = OrderResponseProducts.from_json(json)
# print the JSON string representation of the object
print OrderResponseProducts.to_json()

# convert the object into a dict
order_response_products_dict = order_response_products_instance.to_dict()
# create an instance of OrderResponseProducts from a dict
order_response_products_form_dict = order_response_products.from_dict(order_response_products_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


