# CheckoutOrderTemplateCustomerInfo

It is the information of the customer who will be created when receiving a new payment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**email** | **str** |  | 
**phone** | **str** |  | 
**corporate** | **bool** |  | [optional] 
**object** | **str** |  | [optional] 
**customer_id** | **str** |  | 

## Example

```python
from conekta.models.checkout_order_template_customer_info import CheckoutOrderTemplateCustomerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutOrderTemplateCustomerInfo from a JSON string
checkout_order_template_customer_info_instance = CheckoutOrderTemplateCustomerInfo.from_json(json)
# print the JSON string representation of the object
print(CheckoutOrderTemplateCustomerInfo.to_json())

# convert the object into a dict
checkout_order_template_customer_info_dict = checkout_order_template_customer_info_instance.to_dict()
# create an instance of CheckoutOrderTemplateCustomerInfo from a dict
checkout_order_template_customer_info_from_dict = CheckoutOrderTemplateCustomerInfo.from_dict(checkout_order_template_customer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


