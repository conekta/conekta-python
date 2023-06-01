# OrderResponseCharges

The charges associated with the order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** | Indicates if there are more pages to be requested | 
**object** | **str** | Object type, in this case is list | 
**data** | [**List[ChargesDataResponse]**](ChargesDataResponse.md) |  | [optional] 

## Example

```python
from conekta.models.order_response_charges import OrderResponseCharges

# TODO update the JSON string below
json = "{}"
# create an instance of OrderResponseCharges from a JSON string
order_response_charges_instance = OrderResponseCharges.from_json(json)
# print the JSON string representation of the object
print OrderResponseCharges.to_json()

# convert the object into a dict
order_response_charges_dict = order_response_charges_instance.to_dict()
# create an instance of OrderResponseCharges from a dict
order_response_charges_form_dict = order_response_charges.from_dict(order_response_charges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


