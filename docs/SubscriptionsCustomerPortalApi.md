# conekta.SubscriptionsCustomerPortalApi

All URIs are relative to *https://api.conekta.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customer_portal**](SubscriptionsCustomerPortalApi.md#create_customer_portal) | **POST** /subscriptions/{subscription_id}/customer_portal | Create customer portal
[**get_customer_portal**](SubscriptionsCustomerPortalApi.md#get_customer_portal) | **GET** /subscriptions/{subscription_id}/customer_portal | Get customer portal


# **create_customer_portal**
> CustomerPortalResponse create_customer_portal(subscription_id, accept_language=accept_language, x_child_company_id=x_child_company_id)

Create customer portal

Creates a customer portal for a subscription. If a portal already exists, returns the existing one.

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.customer_portal_response import CustomerPortalResponse
from conekta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.conekta.io
# See configuration.py for a list of all supported configuration parameters.
configuration = conekta.Configuration(
    host = "https://api.conekta.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = conekta.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with conekta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conekta.SubscriptionsCustomerPortalApi(api_client)
    subscription_id = 'sub_2tGzG1GxtDAZHEGPH' # str | Identifier of the subscription resource
    accept_language = 'es' # str | Use for knowing which language to use (optional) (default to 'es')
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Create customer portal
        api_response = api_instance.create_customer_portal(subscription_id, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of SubscriptionsCustomerPortalApi->create_customer_portal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsCustomerPortalApi->create_customer_portal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Identifier of the subscription resource | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to &#39;es&#39;]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**CustomerPortalResponse**](CustomerPortalResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Customer portal created successfully |  * Date - The date and time that the response was sent <br>  * Content-Type - The format of the response body <br>  * Content-Length - The length of the response body in bytes <br>  * Connection - The type of connection used to transfer the response <br>  * Conekta-Media-Type -  <br>  |
**404** | not found entity |  -  |
**401** | authentication error |  -  |
**422** | parameter validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_portal**
> CustomerPortalResponse get_customer_portal(subscription_id, accept_language=accept_language, x_child_company_id=x_child_company_id)

Get customer portal

Retrieves the customer portal for a subscription

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.customer_portal_response import CustomerPortalResponse
from conekta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.conekta.io
# See configuration.py for a list of all supported configuration parameters.
configuration = conekta.Configuration(
    host = "https://api.conekta.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = conekta.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with conekta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conekta.SubscriptionsCustomerPortalApi(api_client)
    subscription_id = 'sub_2tGzG1GxtDAZHEGPH' # str | Identifier of the subscription resource
    accept_language = 'es' # str | Use for knowing which language to use (optional) (default to 'es')
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Get customer portal
        api_response = api_instance.get_customer_portal(subscription_id, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of SubscriptionsCustomerPortalApi->get_customer_portal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsCustomerPortalApi->get_customer_portal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Identifier of the subscription resource | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to &#39;es&#39;]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**CustomerPortalResponse**](CustomerPortalResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Customer portal retrieved successfully |  * Date - The date and time that the response was sent <br>  * Content-Type - The format of the response body <br>  * Content-Length - The length of the response body in bytes <br>  * Connection - The type of connection used to transfer the response <br>  * Conekta-Media-Type -  <br>  |
**404** | not found entity |  -  |
**401** | authentication error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

