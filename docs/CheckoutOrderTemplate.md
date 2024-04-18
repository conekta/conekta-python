# CheckoutOrderTemplate

It maintains the attributes with which the order will be created when receiving a new payment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | It is the currency in which the order will be created. It must be a valid ISO 4217 currency code. | 
**customer_info** | [**CheckoutOrderTemplateCustomerInfo**](CheckoutOrderTemplateCustomerInfo.md) |  | [optional] 
**line_items** | [**List[Product]**](Product.md) | They are the products to buy. Each contains the \&quot;unit price\&quot; and \&quot;quantity\&quot; parameters that are used to calculate the total amount of the order. | 
**metadata** | **Dict[str, object]** | It is a set of key-value pairs that you can attach to the order. It can be used to store additional information about the order in a structured format. | [optional] 

## Example

```python
from conekta.models.checkout_order_template import CheckoutOrderTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutOrderTemplate from a JSON string
checkout_order_template_instance = CheckoutOrderTemplate.from_json(json)
# print the JSON string representation of the object
print(CheckoutOrderTemplate.to_json())

# convert the object into a dict
checkout_order_template_dict = checkout_order_template_instance.to_dict()
# create an instance of CheckoutOrderTemplate from a dict
checkout_order_template_from_dict = CheckoutOrderTemplate.from_dict(checkout_order_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


