# CustomerResponse

customer response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**antifraud_info** | [**CustomerAntifraudInfoResponse**](CustomerAntifraudInfoResponse.md) |  | [optional] 
**corporate** | **bool** |  | [optional] 
**created_at** | **int** |  | 
**custom_reference** | **str** |  | [optional] 
**default_fiscal_entity_id** | **str** |  | [optional] 
**default_shipping_contact_id** | **str** |  | [optional] 
**default_payment_source_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**fiscal_entities** | [**CustomerFiscalEntitiesResponse**](CustomerFiscalEntitiesResponse.md) |  | [optional] 
**id** | **str** |  | 
**livemode** | **bool** |  | 
**name** | **str** |  | [optional] 
**object** | **str** |  | 
**payment_sources** | [**CustomerPaymentMethodsResponse**](CustomerPaymentMethodsResponse.md) |  | [optional] 
**phone** | **str** |  | [optional] 
**shipping_contacts** | [**CustomerResponseShippingContacts**](CustomerResponseShippingContacts.md) |  | [optional] 
**subscription** | [**SubscriptionResponse**](SubscriptionResponse.md) |  | [optional] 

## Example

```python
from conekta.models.customer_response import CustomerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerResponse from a JSON string
customer_response_instance = CustomerResponse.from_json(json)
# print the JSON string representation of the object
print CustomerResponse.to_json()

# convert the object into a dict
customer_response_dict = customer_response_instance.to_dict()
# create an instance of CustomerResponse from a dict
customer_response_form_dict = customer_response.from_dict(customer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


