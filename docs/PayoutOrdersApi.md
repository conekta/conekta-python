# conekta.PayoutOrdersApi

All URIs are relative to *https://api.conekta.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_payout_order_by_id**](PayoutOrdersApi.md#cancel_payout_order_by_id) | **PUT** /payout_orders/{id}/cancel | Cancel Payout Order
[**create_payout_order**](PayoutOrdersApi.md#create_payout_order) | **POST** /payout_orders | Create payout order
[**get_payout_order_by_id**](PayoutOrdersApi.md#get_payout_order_by_id) | **GET** /payout_orders/{id} | Get Payout Order
[**get_payout_orders**](PayoutOrdersApi.md#get_payout_orders) | **GET** /payout_orders | Get a list of Payout Orders


# **cancel_payout_order_by_id**
> PayoutOrderResponse cancel_payout_order_by_id(id, accept_language=accept_language)

Cancel Payout Order

Cancel a payout Order resource that corresponds to a payout order ID.

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.payout_order_response import PayoutOrderResponse
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
    api_instance = conekta.PayoutOrdersApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)

    try:
        # Cancel Payout Order
        api_response = api_instance.cancel_payout_order_by_id(id, accept_language=accept_language)
        print("The response of PayoutOrdersApi->cancel_payout_order_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutOrdersApi->cancel_payout_order_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]

### Return type

[**PayoutOrderResponse**](PayoutOrderResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**401** | authentication error |  -  |
**404** | not found entity |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payout_order**
> PayoutOrderResponse create_payout_order(payout_order, accept_language=accept_language)

Create payout order

Create a new payout order.

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.payout_order import PayoutOrder
from conekta.models.payout_order_response import PayoutOrderResponse
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
    api_instance = conekta.PayoutOrdersApi(api_client)
    payout_order = conekta.PayoutOrder() # PayoutOrder | requested field for payout order
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)

    try:
        # Create payout order
        api_response = api_instance.create_payout_order(payout_order, accept_language=accept_language)
        print("The response of PayoutOrdersApi->create_payout_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutOrdersApi->create_payout_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_order** | [**PayoutOrder**](PayoutOrder.md)| requested field for payout order | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]

### Return type

[**PayoutOrderResponse**](PayoutOrderResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**422** | parameter validation error |  -  |
**401** | authentication error |  -  |
**402** | payment required error |  -  |
**404** | not found entity |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payout_order_by_id**
> PayoutOrderResponse get_payout_order_by_id(id, accept_language=accept_language)

Get Payout Order

Gets a payout Order resource that corresponds to a payout order ID.

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.payout_order_response import PayoutOrderResponse
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
    api_instance = conekta.PayoutOrdersApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)

    try:
        # Get Payout Order
        api_response = api_instance.get_payout_order_by_id(id, accept_language=accept_language)
        print("The response of PayoutOrdersApi->get_payout_order_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutOrdersApi->get_payout_order_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]

### Return type

[**PayoutOrderResponse**](PayoutOrderResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**401** | authentication error |  -  |
**404** | not found entity |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payout_orders**
> PayoutOrdersResponse get_payout_orders(accept_language=accept_language, limit=limit, search=search, next=next, previous=previous)

Get a list of Payout Orders

Get Payout order details in the form of a list

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.payout_orders_response import PayoutOrdersResponse
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
    api_instance = conekta.PayoutOrdersApi(api_client)
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)
    limit = 20 # int | The numbers of items to return, the maximum value is 250 (optional) (default to 20)
    search = 'search_example' # str | General order search, e.g. by mail, reference etc. (optional)
    next = 'next_example' # str | next page (optional)
    previous = 'previous_example' # str | previous page (optional)

    try:
        # Get a list of Payout Orders
        api_response = api_instance.get_payout_orders(accept_language=accept_language, limit=limit, search=search, next=next, previous=previous)
        print("The response of PayoutOrdersApi->get_payout_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutOrdersApi->get_payout_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]
 **limit** | **int**| The numbers of items to return, the maximum value is 250 | [optional] [default to 20]
 **search** | **str**| General order search, e.g. by mail, reference etc. | [optional] 
 **next** | **str**| next page | [optional] 
 **previous** | **str**| previous page | [optional] 

### Return type

[**PayoutOrdersResponse**](PayoutOrdersResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**401** | authentication error |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

