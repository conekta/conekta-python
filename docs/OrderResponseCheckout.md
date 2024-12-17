# OrderResponseCheckout


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
**id** | **str** |  | [optional] 
**is_redirect_on_failure** | **bool** |  | [optional] 
**livemode** | **bool** |  | [optional] 
**max_failed_retries** | **int** | Number of retries allowed before the checkout is marked as failed | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**monthly_installments_enabled** | **bool** |  | [optional] 
**monthly_installments_options** | **List[int]** |  | [optional] 
**name** | **str** |  | [optional] 
**needs_shipping_contact** | **bool** |  | [optional] 
**object** | **str** |  | [optional] 
**on_demand_enabled** | **bool** |  | [optional] 
**paid_payments_count** | **int** |  | [optional] 
**recurrent** | **bool** |  | [optional] 
**redirection_time** | **int** | number of seconds to wait before redirecting to the success_url | [optional] 
**slug** | **str** |  | [optional] 
**sms_sent** | **int** |  | [optional] 
**success_url** | **str** |  | [optional] 
**starts_at** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from conekta.models.order_response_checkout import OrderResponseCheckout

# TODO update the JSON string below
json = "{}"
# create an instance of OrderResponseCheckout from a JSON string
order_response_checkout_instance = OrderResponseCheckout.from_json(json)
# print the JSON string representation of the object
print(OrderResponseCheckout.to_json())

# convert the object into a dict
order_response_checkout_dict = order_response_checkout_instance.to_dict()
# create an instance of OrderResponseCheckout from a dict
order_response_checkout_from_dict = OrderResponseCheckout.from_dict(order_response_checkout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


