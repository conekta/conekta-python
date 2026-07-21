# CustomerPortalResponse

Customer portal model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** | Unique slug identifier for the portal | [optional] 
**subscription_id** | **str** | Associated subscription ID | [optional] 
**customer_id** | **str** | Associated customer ID | [optional] 
**livemode** | **bool** | Whether this is a live or test mode portal | [optional] 
**subscription** | [**SubscriptionDetails**](SubscriptionDetails.md) |  | [optional] 
**customer** | [**CustomerDetails**](CustomerDetails.md) |  | [optional] 
**id** | **str** | Customer portal ID | [optional] 
**company_id** | **str** | Associated company ID | [optional] 
**object** | **str** |  | [optional] 
**created_at** | **int** | Unix timestamp of creation | [optional] 
**updated_at** | **int** | Unix timestamp of last update | [optional] 
**portal_url** | **str** | URL to access the customer portal | [optional] 

## Example

```python
from conekta.models.customer_portal_response import CustomerPortalResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerPortalResponse from a JSON string
customer_portal_response_instance = CustomerPortalResponse.from_json(json)
# print the JSON string representation of the object
print(CustomerPortalResponse.to_json())

# convert the object into a dict
customer_portal_response_dict = customer_portal_response_instance.to_dict()
# create an instance of CustomerPortalResponse from a dict
customer_portal_response_from_dict = CustomerPortalResponse.from_dict(customer_portal_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


