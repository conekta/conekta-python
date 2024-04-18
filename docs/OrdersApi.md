# conekta.OrdersApi

All URIs are relative to *https://api.conekta.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_order**](OrdersApi.md#cancel_order) | **POST** /orders/{id}/cancel | Cancel Order
[**create_order**](OrdersApi.md#create_order) | **POST** /orders | Create order
[**get_order_by_id**](OrdersApi.md#get_order_by_id) | **GET** /orders/{id} | Get Order
[**get_orders**](OrdersApi.md#get_orders) | **GET** /orders | Get a list of Orders
[**order_cancel_refund**](OrdersApi.md#order_cancel_refund) | **DELETE** /orders/{id}/refunds/{refund_id} | Cancel Refund
[**order_refund**](OrdersApi.md#order_refund) | **POST** /orders/{id}/refunds | Refund Order
[**orders_create_capture**](OrdersApi.md#orders_create_capture) | **POST** /orders/{id}/capture | Capture Order
[**update_order**](OrdersApi.md#update_order) | **PUT** /orders/{id} | Update Order


# **cancel_order**
> OrderResponse cancel_order(id, accept_language=accept_language, x_child_company_id=x_child_company_id)

Cancel Order

Cancel an order that has been previously created.

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.order_response import OrderResponse
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
    api_instance = conekta.OrdersApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    accept_language = 'es' # str | Use for knowing which language to use (optional) (default to 'es')
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Cancel Order
        api_response = api_instance.cancel_order(id, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of OrdersApi->cancel_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->cancel_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to &#39;es&#39;]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**OrderResponse**](OrderResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.conekta-v2.1.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  -  |
**401** | authentication error |  -  |
**402** | payment required error |  -  |
**404** | not found entity |  -  |
**428** | Precondition Required |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order**
> OrderResponse create_order(order_request, accept_language=accept_language, x_child_company_id=x_child_company_id)

Create order

Create a new order.

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.order_request import OrderRequest
from conekta.models.order_response import OrderResponse
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
    api_instance = conekta.OrdersApi(api_client)
    order_request = conekta.OrderRequest() # OrderRequest | requested field for order
    accept_language = 'es' # str | Use for knowing which language to use (optional) (default to 'es')
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Create order
        api_response = api_instance.create_order(order_request, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of OrdersApi->create_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->create_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_request** | [**OrderRequest**](OrderRequest.md)| requested field for order | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to &#39;es&#39;]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**OrderResponse**](OrderResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.conekta-v2.1.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**422** | parameter validation error |  -  |
**401** | authentication error |  -  |
**402** | payment required error |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_by_id**
> OrderResponse get_order_by_id(id, accept_language=accept_language, x_child_company_id=x_child_company_id)

Get Order

Info for a specific order

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.order_response import OrderResponse
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
    api_instance = conekta.OrdersApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    accept_language = 'es' # str | Use for knowing which language to use (optional) (default to 'es')
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Get Order
        api_response = api_instance.get_order_by_id(id, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of OrdersApi->get_order_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to &#39;es&#39;]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**OrderResponse**](OrderResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.conekta-v2.1.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  -  |
**401** | authentication error |  -  |
**404** | not found entity |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders**
> GetOrdersResponse get_orders(accept_language=accept_language, x_child_company_id=x_child_company_id, limit=limit, search=search, next=next, previous=previous)

Get a list of Orders

Get order details in the form of a list

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.get_orders_response import GetOrdersResponse
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
    api_instance = conekta.OrdersApi(api_client)
    accept_language = 'es' # str | Use for knowing which language to use (optional) (default to 'es')
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)
    limit = 20 # int | The numbers of items to return, the maximum value is 250 (optional) (default to 20)
    search = 'search_example' # str | General order search, e.g. by mail, reference etc. (optional)
    next = 'next_example' # str | next page (optional)
    previous = 'previous_example' # str | previous page (optional)

    try:
        # Get a list of Orders
        api_response = api_instance.get_orders(accept_language=accept_language, x_child_company_id=x_child_company_id, limit=limit, search=search, next=next, previous=previous)
        print("The response of OrdersApi->get_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to &#39;es&#39;]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 
 **limit** | **int**| The numbers of items to return, the maximum value is 250 | [optional] [default to 20]
 **search** | **str**| General order search, e.g. by mail, reference etc. | [optional] 
 **next** | **str**| next page | [optional] 
 **previous** | **str**| previous page | [optional] 

### Return type

[**GetOrdersResponse**](GetOrdersResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.conekta-v2.1.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**401** | authentication error |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_cancel_refund**
> OrderResponse order_cancel_refund(id, refund_id, accept_language=accept_language, x_child_company_id=x_child_company_id)

Cancel Refund

A refunded order describes the items, amount, and reason an order is being refunded.

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.order_response import OrderResponse
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
    api_instance = conekta.OrdersApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    refund_id = '6407b5bee1329a000175ba11' # str | refund identifier
    accept_language = 'es' # str | Use for knowing which language to use (optional) (default to 'es')
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Cancel Refund
        api_response = api_instance.order_cancel_refund(id, refund_id, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of OrdersApi->order_cancel_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->order_cancel_refund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **refund_id** | **str**| refund identifier | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to &#39;es&#39;]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**OrderResponse**](OrderResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.conekta-v2.1.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  -  |
**401** | authentication error |  -  |
**402** | payment required error |  -  |
**404** | not found entity |  -  |
**422** | parameter validation error |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_refund**
> OrderResponse order_refund(id, order_refund_request, accept_language=accept_language, x_child_company_id=x_child_company_id)

Refund Order

A refunded order describes the items, amount, and reason an order is being refunded.

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.order_refund_request import OrderRefundRequest
from conekta.models.order_response import OrderResponse
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
    api_instance = conekta.OrdersApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    order_refund_request = conekta.OrderRefundRequest() # OrderRefundRequest | requested field for a refund
    accept_language = 'es' # str | Use for knowing which language to use (optional) (default to 'es')
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Refund Order
        api_response = api_instance.order_refund(id, order_refund_request, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of OrdersApi->order_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->order_refund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **order_refund_request** | [**OrderRefundRequest**](OrderRefundRequest.md)| requested field for a refund | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to &#39;es&#39;]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**OrderResponse**](OrderResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.conekta-v2.1.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  -  |
**401** | authentication error |  -  |
**402** | payment required error |  -  |
**404** | not found entity |  -  |
**422** | parameter validation error |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_create_capture**
> OrderResponse orders_create_capture(id, accept_language=accept_language, x_child_company_id=x_child_company_id, order_capture_request=order_capture_request)

Capture Order

Processes an order that has been previously authorized.

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.order_capture_request import OrderCaptureRequest
from conekta.models.order_response import OrderResponse
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
    api_instance = conekta.OrdersApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    accept_language = 'es' # str | Use for knowing which language to use (optional) (default to 'es')
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)
    order_capture_request = conekta.OrderCaptureRequest() # OrderCaptureRequest | requested fields for capture order (optional)

    try:
        # Capture Order
        api_response = api_instance.orders_create_capture(id, accept_language=accept_language, x_child_company_id=x_child_company_id, order_capture_request=order_capture_request)
        print("The response of OrdersApi->orders_create_capture:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_create_capture: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to &#39;es&#39;]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 
 **order_capture_request** | [**OrderCaptureRequest**](OrderCaptureRequest.md)| requested fields for capture order | [optional] 

### Return type

[**OrderResponse**](OrderResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.conekta-v2.1.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  -  |
**401** | authentication error |  -  |
**404** | not found entity |  -  |
**428** | Precondition Required |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_order**
> OrderResponse update_order(id, order_update_request, accept_language=accept_language)

Update Order

Update an existing Order.

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.order_response import OrderResponse
from conekta.models.order_update_request import OrderUpdateRequest
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
    api_instance = conekta.OrdersApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    order_update_request = conekta.OrderUpdateRequest() # OrderUpdateRequest | requested field for an order
    accept_language = 'es' # str | Use for knowing which language to use (optional) (default to 'es')

    try:
        # Update Order
        api_response = api_instance.update_order(id, order_update_request, accept_language=accept_language)
        print("The response of OrdersApi->update_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->update_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **order_update_request** | [**OrderUpdateRequest**](OrderUpdateRequest.md)| requested field for an order | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to &#39;es&#39;]

### Return type

[**OrderResponse**](OrderResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.conekta-v2.1.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  -  |
**401** | authentication error |  -  |
**404** | not found entity |  -  |
**422** | parameter validation error |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

