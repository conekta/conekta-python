# TokenResponseCheckout


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_payment_methods** | **List[str]** |  | [optional] 
**can_not_expire** | **bool** | Indicates if the checkout can not expire. | [optional] 
**emails_sent** | **int** |  | [optional] 
**exclude_card_networks** | **List[str]** |  | [optional] 
**expires_at** | **int** | Date and time when the checkout expires. | [optional] 
**failure_url** | **str** | URL to redirect the customer to if the payment process fails. | [optional] 
**force_3ds_flow** | **bool** | Indicates if the checkout forces the 3DS flow. | [optional] 
**id** | **str** |  | [optional] 
**livemode** | **bool** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**monthly_installments_enabled** | **bool** | Indicates if the checkout allows monthly installments. | [optional] 
**monthly_installments_options** | **List[int]** | List of monthly installments options. | [optional] 
**name** | **str** |  | [optional] 
**needs_shipping_contact** | **bool** |  | [optional] 
**object** | **str** | Indicates the type of object, in this case checkout. | [optional] 
**on_demand_enabled** | **bool** | Indicates if the checkout allows on demand payments. | [optional] 
**paid_payments_count** | **int** | Number of payments that have been paid. | [optional] 
**recurrent** | **bool** | Indicates if the checkout is recurrent. | [optional] 
**sms_sent** | **int** |  | [optional] 
**starts_at** | **int** | Date and time when the checkout starts. | [optional] 
**status** | **str** | Status of the checkout. | [optional] 
**success_url** | **str** | URL to redirect the customer to after the payment process is completed. | [optional] 
**type** | **str** | Type of checkout. | [optional] 

## Example

```python
from conekta.models.token_response_checkout import TokenResponseCheckout

# TODO update the JSON string below
json = "{}"
# create an instance of TokenResponseCheckout from a JSON string
token_response_checkout_instance = TokenResponseCheckout.from_json(json)
# print the JSON string representation of the object
print(TokenResponseCheckout.to_json())

# convert the object into a dict
token_response_checkout_dict = token_response_checkout_instance.to_dict()
# create an instance of TokenResponseCheckout from a dict
token_response_checkout_from_dict = TokenResponseCheckout.from_dict(token_response_checkout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


