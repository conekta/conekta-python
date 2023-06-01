# CustomerFiscalEntitiesRequestAddress


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street1** | **str** |  | 
**street2** | **str** |  | [optional] 
**postal_code** | **str** |  | 
**city** | **str** |  | 
**state** | **str** |  | [optional] 
**country** | **str** | this field follows the [ISO 3166-1 alpha-2 standard](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) | [optional] 
**residential** | **bool** |  | [optional] 
**external_number** | **str** |  | [optional] 

## Example

```python
from conekta.models.customer_fiscal_entities_request_address import CustomerFiscalEntitiesRequestAddress

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerFiscalEntitiesRequestAddress from a JSON string
customer_fiscal_entities_request_address_instance = CustomerFiscalEntitiesRequestAddress.from_json(json)
# print the JSON string representation of the object
print CustomerFiscalEntitiesRequestAddress.to_json()

# convert the object into a dict
customer_fiscal_entities_request_address_dict = customer_fiscal_entities_request_address_instance.to_dict()
# create an instance of CustomerFiscalEntitiesRequestAddress from a dict
customer_fiscal_entities_request_address_form_dict = customer_fiscal_entities_request_address.from_dict(customer_fiscal_entities_request_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


