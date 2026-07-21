# OrderResponseCheckout


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_payment_methods** | **List[str]** | Are the payment methods available for this link | [optional] 
**excluded_payment_methods** | **List[str]** | Payment methods excluded from the checkout. This field is only returned when excluded_payment_methods is provided in the request. | [optional] 
**can_not_expire** | **bool** |  | [optional] 
**emails_sent** | **int** |  | [optional] 
**exclude_card_networks** | **List[str]** |  | [optional] 
**expires_at** | **int** |  | [optional] 
**failure_url** | **str** |  | [optional] 
**force_3ds_flow** | **bool** |  | [optional] 
**force_save_card** | **bool** | Indicates whether the card used for the payment should be saved for future purchases. This field is only applicable for card payments. | [optional] 
**id** | **str** |  | 
**is_redirect_on_failure** | **bool** |  | [optional] 
**livemode** | **bool** |  | 
**max_failed_retries** | **int** | Number of retries allowed before the checkout is marked as failed | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**monthly_installments_enabled** | **bool** |  | [optional] 
**monthly_installments_options** | **List[int]** |  | [optional] 
**name** | **str** |  | 
**needs_shipping_contact** | **bool** |  | [optional] 
**object** | **str** |  | 
**on_demand_enabled** | **bool** |  | [optional] 
**paid_payments_count** | **int** |  | [optional] 
**recurrent** | **bool** |  | [optional] 
**redirection_time** | **int** | number of seconds to wait before redirecting to the success_url | [optional] 
**slug** | **str** |  | [optional] 
**sms_sent** | **int** |  | [optional] 
**success_url** | **str** | Redirection url back to the site in case of successful payment, applies only to HostedPayment | [optional] 
**starts_at** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**type** | **str** | This field represents the type of checkout, which determines the user experience during the payment process. &#39;HostedPayment&#39; will redirect the customer to a Conekta-hosted page to complete the payment, while &#39;Integration&#39; allows the payment process to be handled entirely on your site using Conekta&#39;s APIs and SDKs. | 
**url** | **str** | Indicate the url of the Conekta component to complete the payment. For HostedPayment, this will be a Conekta-hosted page | [optional] 

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


