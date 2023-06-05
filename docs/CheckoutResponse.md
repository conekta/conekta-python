# CheckoutResponse

checkout response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_payment_methods** | **List[str]** |  | [optional] 
**can_not_expire** | **bool** |  | [optional] 
**emails_sent** | **int** |  | [optional] 
**exclude_card_networks** | **List[object]** |  | [optional] 
**expires_at** | **int** |  | [optional] 
**failure_url** | **str** |  | [optional] 
**force_3ds_flow** | **bool** |  | [optional] 
**id** | **str** |  | 
**livemode** | **bool** |  | 
**metadata** | **Dict[str, object]** |  | [optional] 
**monthly_installments_enabled** | **bool** |  | [optional] 
**monthly_installments_options** | **List[int]** |  | [optional] 
**name** | **str** | Reason for charge | 
**needs_shipping_contact** | **bool** |  | [optional] 
**object** | **str** |  | 
**paid_payments_count** | **int** |  | [optional] 
**payments_limit_count** | **int** |  | [optional] 
**recurrent** | **bool** |  | [optional] 
**slug** | **str** |  | [optional] 
**sms_sent** | **int** |  | [optional] 
**starts_at** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**success_url** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from conekta.models.checkout_response import CheckoutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutResponse from a JSON string
checkout_response_instance = CheckoutResponse.from_json(json)
# print the JSON string representation of the object
print CheckoutResponse.to_json()

# convert the object into a dict
checkout_response_dict = checkout_response_instance.to_dict()
# create an instance of CheckoutResponse from a dict
checkout_response_form_dict = checkout_response.from_dict(checkout_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


