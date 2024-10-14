# Checkout

It is a sub-resource of the Order model that can be stipulated in order to configure its corresponding checkout

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_payment_methods** | **List[str]** | Those are the payment methods that will be available for the link | 
**expires_at** | **int** | It is the time when the link will expire. It is expressed in seconds since the Unix epoch. The valid range is from 2 to 365 days (the valid range will be taken from the next day of the creation date at 00:01 hrs)  | 
**monthly_installments_enabled** | **bool** | This flag allows you to specify if months without interest will be active. | [optional] 
**monthly_installments_options** | **List[int]** | This field allows you to specify the number of months without interest. | [optional] 
**three_ds_mode** | **str** | Indicates the 3DS2 mode for the order, either smart or strict. | [optional] 
**name** | **str** | Reason for charge | 
**needs_shipping_contact** | **bool** | This flag allows you to fill in the shipping information at checkout. | [optional] 
**on_demand_enabled** | **bool** | This flag allows you to specify if the link will be on demand. | [optional] 
**order_template** | [**CheckoutOrderTemplate**](CheckoutOrderTemplate.md) |  | 
**payments_limit_count** | **int** | It is the number of payments that can be made through the link. | [optional] 
**recurrent** | **bool** | false: single use. true: multiple payments | 
**type** | **str** | It is the type of link that will be created. It must be a valid type. | 

## Example

```python
from conekta.models.checkout import Checkout

# TODO update the JSON string below
json = "{}"
# create an instance of Checkout from a JSON string
checkout_instance = Checkout.from_json(json)
# print the JSON string representation of the object
print(Checkout.to_json())

# convert the object into a dict
checkout_dict = checkout_instance.to_dict()
# create an instance of Checkout from a dict
checkout_from_dict = Checkout.from_dict(checkout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


