# CustomerResponseShippingContacts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** | Indicates if there are more pages to be requested | 
**object** | **str** | Object type, in this case is list | 
**data** | [**List[CustomerShippingContactsDataResponse]**](CustomerShippingContactsDataResponse.md) |  | [optional] 

## Example

```python
from conekta.models.customer_response_shipping_contacts import CustomerResponseShippingContacts

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerResponseShippingContacts from a JSON string
customer_response_shipping_contacts_instance = CustomerResponseShippingContacts.from_json(json)
# print the JSON string representation of the object
print(CustomerResponseShippingContacts.to_json())

# convert the object into a dict
customer_response_shipping_contacts_dict = customer_response_shipping_contacts_instance.to_dict()
# create an instance of CustomerResponseShippingContacts from a dict
customer_response_shipping_contacts_from_dict = CustomerResponseShippingContacts.from_dict(customer_response_shipping_contacts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


