# conekta.SubscriptionsApi

All URIs are relative to *https://api.conekta.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_subscription**](SubscriptionsApi.md#cancel_subscription) | **POST** /customers/{id}/subscription/cancel | Cancel Subscription [Deprecated]
[**create_subscription**](SubscriptionsApi.md#create_subscription) | **POST** /customers/{id}/subscription | Create Subscription [Deprecated]
[**get_subscription**](SubscriptionsApi.md#get_subscription) | **GET** /customers/{id}/subscription | Get Subscription [Deprecated]
[**get_subscription_events**](SubscriptionsApi.md#get_subscription_events) | **GET** /customers/{id}/subscription/events | Get Subscription Events [Deprecated]
[**pause_subscription**](SubscriptionsApi.md#pause_subscription) | **POST** /customers/{id}/subscription/pause | Pause Subscription [Deprecated]
[**resume_subscription**](SubscriptionsApi.md#resume_subscription) | **POST** /customers/{id}/subscription/resume | Resume Subscription [Deprecated]
[**subscription_cancel**](SubscriptionsApi.md#subscription_cancel) | **POST** /customers/{customer_id}/subscriptions/{id}/cancel | Cancel Subscription
[**subscription_create**](SubscriptionsApi.md#subscription_create) | **POST** /customers/{customer_id}/subscriptions | Create Subscription
[**subscription_events**](SubscriptionsApi.md#subscription_events) | **GET** /customers/{customer_id}/subscriptions/{id}/events | Get Subscription Events
[**subscription_list**](SubscriptionsApi.md#subscription_list) | **GET** /customers/{customer_id}/subscriptions | List Subscriptions
[**subscription_pause**](SubscriptionsApi.md#subscription_pause) | **POST** /customers/{customer_id}/subscriptions/{id}/pause | Pause Subscription
[**subscription_resume**](SubscriptionsApi.md#subscription_resume) | **POST** /customers/{customer_id}/subscriptions/{id}/resume | Resume Subscription
[**subscription_update**](SubscriptionsApi.md#subscription_update) | **PUT** /customers/{customer_id}/subscriptions/{id} | Update Subscription
[**subscriptions_get**](SubscriptionsApi.md#subscriptions_get) | **GET** /customers/{customer_id}/subscriptions/{id} | Get Subscription
[**subscriptions_retry**](SubscriptionsApi.md#subscriptions_retry) | **POST** /customers/{customer_id}/subscriptions/{id}/retry | Retry Failed Payment
[**update_subscription**](SubscriptionsApi.md#update_subscription) | **PUT** /customers/{id}/subscription | Update Subscription [Deprecated]


# **cancel_subscription**
> SubscriptionResponse cancel_subscription(id, accept_language=accept_language, x_child_company_id=x_child_company_id)

Cancel Subscription [Deprecated]

DEPRECATED: This endpoint will be removed in version 2.3.0.

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.subscription_response import SubscriptionResponse
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
    api_instance = conekta.SubscriptionsApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Cancel Subscription [Deprecated]
        api_response = api_instance.cancel_subscription(id, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of SubscriptionsApi->cancel_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->cancel_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  * Date - The date and time that the response was sent <br>  * Content-Type - The format of the response body <br>  * Content-Length - The length of the response body in bytes <br>  * Connection - The type of connection used to transfer the response <br>  * Conekta-Media-Type -  <br>  |
**401** | authentication error |  -  |
**404** | not found entity |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subscription**
> SubscriptionResponse create_subscription(id, subscription_request, accept_language=accept_language, x_child_company_id=x_child_company_id)

Create Subscription [Deprecated]

DEPRECATED: This endpoint will be removed in version 2.3.0. You can create the subscription to include the plans that your customers consume

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.subscription_request import SubscriptionRequest
from conekta.models.subscription_response import SubscriptionResponse
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
    api_instance = conekta.SubscriptionsApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    subscription_request = conekta.SubscriptionRequest() # SubscriptionRequest | requested field for subscriptions
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Create Subscription [Deprecated]
        api_response = api_instance.create_subscription(id, subscription_request, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of SubscriptionsApi->create_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->create_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **subscription_request** | [**SubscriptionRequest**](SubscriptionRequest.md)| requested field for subscriptions | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  * Date - The date and time that the response was sent <br>  * Content-Type - The format of the response body <br>  * Content-Length - The length of the response body in bytes <br>  * Connection - The type of connection used to transfer the response <br>  * Conekta-Media-Type -  <br>  |
**422** | parameter validation error |  -  |
**401** | authentication error |  -  |
**404** | not found entity |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription**
> SubscriptionResponse get_subscription(id, accept_language=accept_language)

Get Subscription [Deprecated]

DEPRECATED: This endpoint will be removed in version 2.3.0.

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.subscription_response import SubscriptionResponse
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
    api_instance = conekta.SubscriptionsApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)

    try:
        # Get Subscription [Deprecated]
        api_response = api_instance.get_subscription(id, accept_language=accept_language)
        print("The response of SubscriptionsApi->get_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  * Date - The date and time that the response was sent <br>  * Content-Type - The format of the response body <br>  * Content-Length - The length of the response body in bytes <br>  * Connection - The type of connection used to transfer the response <br>  * Conekta-Media-Type -  <br>  |
**401** | authentication error |  -  |
**404** | not found entity |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_events**
> SubscriptionEventsResponse get_subscription_events(id, accept_language=accept_language, x_child_company_id=x_child_company_id)

Get Subscription Events [Deprecated]

DEPRECATED: This endpoint will be removed in version 2.3.0. You can get the events of the subscription(s) of a client, with the customer id

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.subscription_events_response import SubscriptionEventsResponse
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
    api_instance = conekta.SubscriptionsApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Get Subscription Events [Deprecated]
        api_response = api_instance.get_subscription_events(id, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of SubscriptionsApi->get_subscription_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_subscription_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**SubscriptionEventsResponse**](SubscriptionEventsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  * Date - The date and time that the response was sent <br>  * Content-Type - The format of the response body <br>  * Content-Length - The length of the response body in bytes <br>  * Connection - The type of connection used to transfer the response <br>  * Conekta-Media-Type -  <br>  |
**401** | authentication error |  -  |
**402** | payment required error |  -  |
**404** | not found entity |  -  |
**422** | parameter validation error |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_subscription**
> SubscriptionResponse pause_subscription(id, accept_language=accept_language, x_child_company_id=x_child_company_id)

Pause Subscription [Deprecated]

DEPRECATED: This endpoint will be removed in version 2.3.0.

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.subscription_response import SubscriptionResponse
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
    api_instance = conekta.SubscriptionsApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Pause Subscription [Deprecated]
        api_response = api_instance.pause_subscription(id, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of SubscriptionsApi->pause_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->pause_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  * Date - The date and time that the response was sent <br>  * Content-Type - The format of the response body <br>  * Content-Length - The length of the response body in bytes <br>  * Connection - The type of connection used to transfer the response <br>  * Conekta-Media-Type -  <br>  |
**401** | authentication error |  -  |
**402** | payment required error |  -  |
**404** | not found entity |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_subscription**
> SubscriptionResponse resume_subscription(id, accept_language=accept_language, x_child_company_id=x_child_company_id)

Resume Subscription [Deprecated]

DEPRECATED: This endpoint will be removed in version 2.3.0.

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.subscription_response import SubscriptionResponse
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
    api_instance = conekta.SubscriptionsApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Resume Subscription [Deprecated]
        api_response = api_instance.resume_subscription(id, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of SubscriptionsApi->resume_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->resume_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  * Date - The date and time that the response was sent <br>  * Content-Type - The format of the response body <br>  * Content-Length - The length of the response body in bytes <br>  * Connection - The type of connection used to transfer the response <br>  * Conekta-Media-Type -  <br>  |
**401** | authentication error |  -  |
**402** | payment required error |  -  |
**404** | not found entity |  -  |
**422** | parameter validation error |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_cancel**
> SubscriptionResponse subscription_cancel(customer_id, id, accept_language=accept_language, x_child_company_id=x_child_company_id)

Cancel Subscription

Cancel a specific subscription

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.subscription_response import SubscriptionResponse
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
    api_instance = conekta.SubscriptionsApi(api_client)
    customer_id = 'cus_2tGzG1GxtDAZHEGPH' # str | Identifier of the customer resource
    id = 'sub_2tGzG1GxtDAZHEGPH' # str | Identifier of the subscription resource
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Cancel Subscription
        api_response = api_instance.subscription_cancel(customer_id, id, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of SubscriptionsApi->subscription_cancel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscription_cancel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Identifier of the customer resource | 
 **id** | **str**| Identifier of the subscription resource | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  * Date - The date and time that the response was sent <br>  * Content-Type - The format of the response body <br>  * Content-Length - The length of the response body in bytes <br>  * Connection - The type of connection used to transfer the response <br>  * Conekta-Media-Type -  <br>  |
**401** | authentication error |  -  |
**404** | not found entity |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_create**
> SubscriptionResponse subscription_create(customer_id, subscription_request, accept_language=accept_language, x_child_company_id=x_child_company_id)

Create Subscription

Create a new subscription for a customer (keeps existing subscriptions active)

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.subscription_request import SubscriptionRequest
from conekta.models.subscription_response import SubscriptionResponse
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
    api_instance = conekta.SubscriptionsApi(api_client)
    customer_id = 'cus_2tGzG1GxtDAZHEGPH' # str | Identifier of the customer resource
    subscription_request = conekta.SubscriptionRequest() # SubscriptionRequest | requested field for subscriptions
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Create Subscription
        api_response = api_instance.subscription_create(customer_id, subscription_request, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of SubscriptionsApi->subscription_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscription_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Identifier of the customer resource | 
 **subscription_request** | [**SubscriptionRequest**](SubscriptionRequest.md)| requested field for subscriptions | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  * Date - The date and time that the response was sent <br>  * Content-Type - The format of the response body <br>  * Content-Length - The length of the response body in bytes <br>  * Connection - The type of connection used to transfer the response <br>  * Conekta-Media-Type -  <br>  |
**422** | parameter validation error |  -  |
**401** | authentication error |  -  |
**404** | not found entity |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_events**
> SubscriptionEventsResponse subscription_events(customer_id, id, accept_language=accept_language, x_child_company_id=x_child_company_id, limit=limit, search=search, next=next, previous=previous)

Get Subscription Events

Get events for a specific subscription

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.subscription_events_response import SubscriptionEventsResponse
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
    api_instance = conekta.SubscriptionsApi(api_client)
    customer_id = 'cus_2tGzG1GxtDAZHEGPH' # str | Identifier of the customer resource
    id = 'sub_2tGzG1GxtDAZHEGPH' # str | Identifier of the subscription resource
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)
    limit = 20 # int | The numbers of items to return, the maximum value is 250 (optional) (default to 20)
    search = 'search_example' # str | General order search, e.g. by mail, reference etc. (optional)
    next = 'next_example' # str | next page (optional)
    previous = 'previous_example' # str | previous page (optional)

    try:
        # Get Subscription Events
        api_response = api_instance.subscription_events(customer_id, id, accept_language=accept_language, x_child_company_id=x_child_company_id, limit=limit, search=search, next=next, previous=previous)
        print("The response of SubscriptionsApi->subscription_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscription_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Identifier of the customer resource | 
 **id** | **str**| Identifier of the subscription resource | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 
 **limit** | **int**| The numbers of items to return, the maximum value is 250 | [optional] [default to 20]
 **search** | **str**| General order search, e.g. by mail, reference etc. | [optional] 
 **next** | **str**| next page | [optional] 
 **previous** | **str**| previous page | [optional] 

### Return type

[**SubscriptionEventsResponse**](SubscriptionEventsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  * Date - The date and time that the response was sent <br>  * Content-Type - The format of the response body <br>  * Content-Length - The length of the response body in bytes <br>  * Connection - The type of connection used to transfer the response <br>  * Conekta-Media-Type -  <br>  |
**401** | authentication error |  -  |
**404** | not found entity |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_list**
> SubscriptionResponse subscription_list(customer_id, accept_language=accept_language, x_child_company_id=x_child_company_id, limit=limit, search=search, next=next, previous=previous)

List Subscriptions

Get a list of subscriptions for a customer

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.subscription_response import SubscriptionResponse
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
    api_instance = conekta.SubscriptionsApi(api_client)
    customer_id = 'cus_2tGzG1GxtDAZHEGPH' # str | Identifier of the customer resource
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)
    limit = 20 # int | The numbers of items to return, the maximum value is 250 (optional) (default to 20)
    search = 'search_example' # str | General order search, e.g. by mail, reference etc. (optional)
    next = 'next_example' # str | next page (optional)
    previous = 'previous_example' # str | previous page (optional)

    try:
        # List Subscriptions
        api_response = api_instance.subscription_list(customer_id, accept_language=accept_language, x_child_company_id=x_child_company_id, limit=limit, search=search, next=next, previous=previous)
        print("The response of SubscriptionsApi->subscription_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscription_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Identifier of the customer resource | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 
 **limit** | **int**| The numbers of items to return, the maximum value is 250 | [optional] [default to 20]
 **search** | **str**| General order search, e.g. by mail, reference etc. | [optional] 
 **next** | **str**| next page | [optional] 
 **previous** | **str**| previous page | [optional] 

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  * Date - The date and time that the response was sent <br>  * Content-Type - The format of the response body <br>  * Content-Length - The length of the response body in bytes <br>  * Connection - The type of connection used to transfer the response <br>  * Conekta-Media-Type -  <br>  |
**401** | authentication error |  -  |
**404** | not found entity |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_pause**
> SubscriptionResponse subscription_pause(customer_id, id, accept_language=accept_language, x_child_company_id=x_child_company_id)

Pause Subscription

Pause a specific subscription

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.subscription_response import SubscriptionResponse
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
    api_instance = conekta.SubscriptionsApi(api_client)
    customer_id = 'cus_2tGzG1GxtDAZHEGPH' # str | Identifier of the customer resource
    id = 'sub_2tGzG1GxtDAZHEGPH' # str | Identifier of the subscription resource
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Pause Subscription
        api_response = api_instance.subscription_pause(customer_id, id, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of SubscriptionsApi->subscription_pause:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscription_pause: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Identifier of the customer resource | 
 **id** | **str**| Identifier of the subscription resource | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  * Date - The date and time that the response was sent <br>  * Content-Type - The format of the response body <br>  * Content-Length - The length of the response body in bytes <br>  * Connection - The type of connection used to transfer the response <br>  * Conekta-Media-Type -  <br>  |
**401** | authentication error |  -  |
**404** | not found entity |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_resume**
> SubscriptionResponse subscription_resume(customer_id, id, accept_language=accept_language, x_child_company_id=x_child_company_id)

Resume Subscription

Resume a specific paused subscription

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.subscription_response import SubscriptionResponse
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
    api_instance = conekta.SubscriptionsApi(api_client)
    customer_id = 'cus_2tGzG1GxtDAZHEGPH' # str | Identifier of the customer resource
    id = 'sub_2tGzG1GxtDAZHEGPH' # str | Identifier of the subscription resource
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Resume Subscription
        api_response = api_instance.subscription_resume(customer_id, id, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of SubscriptionsApi->subscription_resume:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscription_resume: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Identifier of the customer resource | 
 **id** | **str**| Identifier of the subscription resource | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  * Date - The date and time that the response was sent <br>  * Content-Type - The format of the response body <br>  * Content-Length - The length of the response body in bytes <br>  * Connection - The type of connection used to transfer the response <br>  * Conekta-Media-Type -  <br>  |
**401** | authentication error |  -  |
**404** | not found entity |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_update**
> SubscriptionResponse subscription_update(customer_id, id, subscription_update_request, accept_language=accept_language, x_child_company_id=x_child_company_id)

Update Subscription

Update a specific subscription

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.subscription_response import SubscriptionResponse
from conekta.models.subscription_update_request import SubscriptionUpdateRequest
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
    api_instance = conekta.SubscriptionsApi(api_client)
    customer_id = 'cus_2tGzG1GxtDAZHEGPH' # str | Identifier of the customer resource
    id = 'sub_2tGzG1GxtDAZHEGPH' # str | Identifier of the subscription resource
    subscription_update_request = conekta.SubscriptionUpdateRequest() # SubscriptionUpdateRequest | requested field for update a subscription
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Update Subscription
        api_response = api_instance.subscription_update(customer_id, id, subscription_update_request, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of SubscriptionsApi->subscription_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscription_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Identifier of the customer resource | 
 **id** | **str**| Identifier of the subscription resource | 
 **subscription_update_request** | [**SubscriptionUpdateRequest**](SubscriptionUpdateRequest.md)| requested field for update a subscription | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  * Date - The date and time that the response was sent <br>  * Content-Type - The format of the response body <br>  * Content-Length - The length of the response body in bytes <br>  * Connection - The type of connection used to transfer the response <br>  * Conekta-Media-Type -  <br>  |
**422** | parameter validation error |  -  |
**401** | authentication error |  -  |
**404** | not found entity |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_get**
> SubscriptionResponse subscriptions_get(customer_id, id, accept_language=accept_language, x_child_company_id=x_child_company_id)

Get Subscription

Retrieve a specific subscription

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.subscription_response import SubscriptionResponse
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
    api_instance = conekta.SubscriptionsApi(api_client)
    customer_id = 'cus_2tGzG1GxtDAZHEGPH' # str | Identifier of the customer resource
    id = 'sub_2tGzG1GxtDAZHEGPH' # str | Identifier of the subscription resource
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Get Subscription
        api_response = api_instance.subscriptions_get(customer_id, id, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of SubscriptionsApi->subscriptions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscriptions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Identifier of the customer resource | 
 **id** | **str**| Identifier of the subscription resource | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  * Date - The date and time that the response was sent <br>  * Content-Type - The format of the response body <br>  * Content-Length - The length of the response body in bytes <br>  * Connection - The type of connection used to transfer the response <br>  * Conekta-Media-Type -  <br>  |
**401** | authentication error |  -  |
**404** | not found entity |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_retry**
> SubscriptionResponse subscriptions_retry(customer_id, id, accept_language=accept_language, x_child_company_id=x_child_company_id)

Retry Failed Payment

Retry a failed payment for a specific subscription

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.subscription_response import SubscriptionResponse
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
    api_instance = conekta.SubscriptionsApi(api_client)
    customer_id = 'cus_2tGzG1GxtDAZHEGPH' # str | Identifier of the customer resource
    id = 'sub_2tGzG1GxtDAZHEGPH' # str | Identifier of the subscription resource
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Retry Failed Payment
        api_response = api_instance.subscriptions_retry(customer_id, id, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of SubscriptionsApi->subscriptions_retry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscriptions_retry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Identifier of the customer resource | 
 **id** | **str**| Identifier of the subscription resource | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  * Date - The date and time that the response was sent <br>  * Content-Type - The format of the response body <br>  * Content-Length - The length of the response body in bytes <br>  * Connection - The type of connection used to transfer the response <br>  * Conekta-Media-Type -  <br>  |
**401** | authentication error |  -  |
**404** | not found entity |  -  |
**422** | parameter validation error |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subscription**
> SubscriptionResponse update_subscription(id, subscription_update_request, accept_language=accept_language, x_child_company_id=x_child_company_id)

Update Subscription [Deprecated]

DEPRECATED: This endpoint will be removed in version 2.3.0. You can modify the subscription to change the plans that your customers consume

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.subscription_response import SubscriptionResponse
from conekta.models.subscription_update_request import SubscriptionUpdateRequest
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
    api_instance = conekta.SubscriptionsApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    subscription_update_request = conekta.SubscriptionUpdateRequest() # SubscriptionUpdateRequest | requested field for update a subscription
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Update Subscription [Deprecated]
        api_response = api_instance.update_subscription(id, subscription_update_request, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of SubscriptionsApi->update_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->update_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **subscription_update_request** | [**SubscriptionUpdateRequest**](SubscriptionUpdateRequest.md)| requested field for update a subscription | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  * Date - The date and time that the response was sent <br>  * Content-Type - The format of the response body <br>  * Content-Length - The length of the response body in bytes <br>  * Connection - The type of connection used to transfer the response <br>  * Conekta-Media-Type -  <br>  |
**422** | parameter validation error |  -  |
**401** | authentication error |  -  |
**404** | not found entity |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

