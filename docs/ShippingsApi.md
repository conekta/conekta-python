# conekta.ShippingsApi

All URIs are relative to *https://api.conekta.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orders_create_shipping**](ShippingsApi.md#orders_create_shipping) | **POST** /orders/{id}/shipping_lines | Create Shipping
[**orders_delete_shipping**](ShippingsApi.md#orders_delete_shipping) | **DELETE** /orders/{id}/shipping_lines/{shipping_id} | Delete Shipping
[**orders_update_shipping**](ShippingsApi.md#orders_update_shipping) | **PUT** /orders/{id}/shipping_lines/{shipping_id} | Update Shipping


# **orders_create_shipping**
> ShippingOrderResponse orders_create_shipping(id, shipping_request, accept_language=accept_language, x_child_company_id=x_child_company_id)

Create Shipping

Create new shipping for an existing orden

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.shipping_order_response import ShippingOrderResponse
from conekta.models.shipping_request import ShippingRequest
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
    api_instance = conekta.ShippingsApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    shipping_request = conekta.ShippingRequest() # ShippingRequest | requested field for a shipping
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Create Shipping
        api_response = api_instance.orders_create_shipping(id, shipping_request, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of ShippingsApi->orders_create_shipping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingsApi->orders_create_shipping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **shipping_request** | [**ShippingRequest**](ShippingRequest.md)| requested field for a shipping | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**ShippingOrderResponse**](ShippingOrderResponse.md)

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
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_delete_shipping**
> ShippingOrderResponse orders_delete_shipping(id, shipping_id, accept_language=accept_language, x_child_company_id=x_child_company_id)

Delete Shipping

Delete shipping

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.shipping_order_response import ShippingOrderResponse
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
    api_instance = conekta.ShippingsApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    shipping_id = 'ship_lin_2tQ974hSHcsdeSZHG' # str | identifier
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Delete Shipping
        api_response = api_instance.orders_delete_shipping(id, shipping_id, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of ShippingsApi->orders_delete_shipping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingsApi->orders_delete_shipping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **shipping_id** | **str**| identifier | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**ShippingOrderResponse**](ShippingOrderResponse.md)

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
**422** | parameter validation error |  -  |
**428** | Precondition Required |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_update_shipping**
> ShippingOrderResponse orders_update_shipping(id, shipping_id, shipping_request, accept_language=accept_language, x_child_company_id=x_child_company_id)

Update Shipping

Update existing shipping for an existing orden

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.shipping_order_response import ShippingOrderResponse
from conekta.models.shipping_request import ShippingRequest
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
    api_instance = conekta.ShippingsApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    shipping_id = 'ship_lin_2tQ974hSHcsdeSZHG' # str | identifier
    shipping_request = conekta.ShippingRequest() # ShippingRequest | requested field for a shipping
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Update Shipping
        api_response = api_instance.orders_update_shipping(id, shipping_id, shipping_request, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of ShippingsApi->orders_update_shipping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingsApi->orders_update_shipping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **shipping_id** | **str**| identifier | 
 **shipping_request** | [**ShippingRequest**](ShippingRequest.md)| requested field for a shipping | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**ShippingOrderResponse**](ShippingOrderResponse.md)

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

