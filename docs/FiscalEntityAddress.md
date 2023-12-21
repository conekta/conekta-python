# FiscalEntityAddress

Address of the fiscal entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street1** | **str** | Street name and number | 
**street2** | **str** | Street name and number | [optional] 
**postal_code** | **str** | Postal code | 
**city** | **str** | City | 
**state** | **str** | State | [optional] 
**country** | **str** | this field follows the [ISO 3166-1 alpha-2 standard](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) | 
**external_number** | **str** | External number | 

## Example

```python
from conekta.models.fiscal_entity_address import FiscalEntityAddress

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalEntityAddress from a JSON string
fiscal_entity_address_instance = FiscalEntityAddress.from_json(json)
# print the JSON string representation of the object
print FiscalEntityAddress.to_json()

# convert the object into a dict
fiscal_entity_address_dict = fiscal_entity_address_instance.to_dict()
# create an instance of FiscalEntityAddress from a dict
fiscal_entity_address_form_dict = fiscal_entity_address.from_dict(fiscal_entity_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


