# PayoutMethod

The payout method of the payout order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the payout method. | 

## Example

```python
from conekta.models.payout_method import PayoutMethod

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutMethod from a JSON string
payout_method_instance = PayoutMethod.from_json(json)
# print the JSON string representation of the object
print(PayoutMethod.to_json())

# convert the object into a dict
payout_method_dict = payout_method_instance.to_dict()
# create an instance of PayoutMethod from a dict
payout_method_from_dict = PayoutMethod.from_dict(payout_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


