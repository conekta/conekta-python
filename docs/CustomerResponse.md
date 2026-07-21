# CustomerResponse

customer response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**antifraud_info** | [**CustomerAntifraudInfoResponse**](CustomerAntifraudInfoResponse.md) |  | [optional] 
**corporate** | **bool** | true if the customer is a company | [optional] 
**created_at** | **int** | Creation date of the object | 
**custom_reference** | **str** | Custom reference | [optional] 
**date_of_birth** | **str** | It is a parameter that allows to identify the date of birth of the client. | [optional] 
**default_fiscal_entity_id** | **str** |  | [optional] 
**default_shipping_contact_id** | **str** |  | [optional] 
**default_payment_source_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**fiscal_entities** | [**CustomerFiscalEntitiesResponse**](CustomerFiscalEntitiesResponse.md) |  | [optional] 
**id** | **str** | Customer&#39;s ID | 
**livemode** | **bool** | true if the object exists in live mode or the value false if the object exists in test mode | 
**name** | **str** | Customer&#39;s name | 
**national_id** | **str** | It is a parameter that allows to identify the national identification number of the client. | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**object** | **str** |  | 
**payment_sources** | [**CustomerPaymentMethodsResponse**](CustomerPaymentMethodsResponse.md) |  | [optional] 
**phone** | **str** | Customer&#39;s phone number | [optional] 
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
print(CustomerResponse.to_json())

# convert the object into a dict
customer_response_dict = customer_response_instance.to_dict()
# create an instance of CustomerResponse from a dict
customer_response_from_dict = CustomerResponse.from_dict(customer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


