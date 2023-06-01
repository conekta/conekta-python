# UpdatePaymentMethods


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from conekta.models.update_payment_methods import UpdatePaymentMethods

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePaymentMethods from a JSON string
update_payment_methods_instance = UpdatePaymentMethods.from_json(json)
# print the JSON string representation of the object
print UpdatePaymentMethods.to_json()

# convert the object into a dict
update_payment_methods_dict = update_payment_methods_instance.to_dict()
# create an instance of UpdatePaymentMethods from a dict
update_payment_methods_form_dict = update_payment_methods.from_dict(update_payment_methods_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


