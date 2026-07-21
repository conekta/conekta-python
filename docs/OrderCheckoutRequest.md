# OrderCheckoutRequest

[Checkout](https://developers.conekta.com/v2.3.0/reference/payment-link) details 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_payment_methods** | **List[str]** | Are the payment methods available for this link. For subscriptions, only &#39;card&#39; is allowed due to the recurring nature of the payments. This field is mutually exclusive with excluded_payment_methods. | [optional] 
**excluded_payment_methods** | **List[str]** | Payment methods to be excluded from the checkout. This field is mutually exclusive with allowed_payment_methods. | [optional] 
**exclude_card_networks** | **List[str]** | List of card networks to exclude from the checkout. This field is only applicable for card payments. | [optional] 
**plan_ids** | **List[str]** | List of plan IDs that will be available for subscription. This field is required for subscription payments. | [optional] 
**expires_at** | **int** | It is the time when the link will expire.  It is expressed in seconds since the Unix epoch. The valid range is from 5 minutes to 365 days from the creation date.  | [optional] 
**failure_url** | **str** | Redirection url back to the site in case of failed payment, applies only to HostedPayment. | [optional] 
**force_save_card** | **bool** | Indicates whether the card used for the payment should be saved for future purchases. This field is only applicable for card payments. | [optional] 
**monthly_installments_enabled** | **bool** |  | [optional] 
**monthly_installments_options** | **List[int]** |  | [optional] 
**max_failed_retries** | **int** | Number of retries allowed before the checkout is marked as failed | [optional] 
**name** | **str** | Reason for payment | [optional] 
**on_demand_enabled** | **bool** |  | [optional] 
**redirection_time** | **int** | number of seconds to wait before redirecting to the success_url | [optional] 
**success_url** | **str** | Redirection url back to the site in case of successful payment, applies only to HostedPayment | [optional] 
**type** | **str** | Required. This field represents the type of checkout, which determines the user experience during the payment process. &#39;HostedPayment&#39; will redirect the customer to a Conekta-hosted page to complete the payment, while &#39;Integration&#39; allows the payment process to be handled entirely on your site using Conekta&#39;s APIs and SDKs. | [optional] 

## Example

```python
from conekta.models.order_checkout_request import OrderCheckoutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCheckoutRequest from a JSON string
order_checkout_request_instance = OrderCheckoutRequest.from_json(json)
# print the JSON string representation of the object
print(OrderCheckoutRequest.to_json())

# convert the object into a dict
order_checkout_request_dict = order_checkout_request_instance.to_dict()
# create an instance of OrderCheckoutRequest from a dict
order_checkout_request_from_dict = OrderCheckoutRequest.from_dict(order_checkout_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


