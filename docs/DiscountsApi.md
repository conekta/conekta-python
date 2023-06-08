# conekta.DiscountsApi

All URIs are relative to *https://api.conekta.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orders_create_discount_line**](DiscountsApi.md#orders_create_discount_line) | **POST** /orders/{id}/discount_lines | Create Discount
[**orders_delete_discount_lines**](DiscountsApi.md#orders_delete_discount_lines) | **DELETE** /orders/{id}/discount_lines/{discount_lines_id} | Delete Discount
[**orders_update_discount_lines**](DiscountsApi.md#orders_update_discount_lines) | **PUT** /orders/{id}/discount_lines/{discount_lines_id} | Update Discount


# **orders_create_discount_line**
> DiscountLinesResponse orders_create_discount_line(id, order_discount_lines_request, accept_language=accept_language, x_child_company_id=x_child_company_id)

Create Discount

Create discount lines for an existing orden

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import conekta
from conekta.models.discount_lines_response import DiscountLinesResponse
from conekta.models.order_discount_lines_request import OrderDiscountLinesRequest
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
    api_instance = conekta.DiscountsApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    order_discount_lines_request = conekta.OrderDiscountLinesRequest() # OrderDiscountLinesRequest | requested field for a discount lines
    accept_language = 'es' # str | Use for knowing which language to use (optional) (default to 'es')
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Create Discount
        api_response = api_instance.orders_create_discount_line(id, order_discount_lines_request, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of DiscountsApi->orders_create_discount_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsApi->orders_create_discount_line: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **order_discount_lines_request** | [**OrderDiscountLinesRequest**](OrderDiscountLinesRequest.md)| requested field for a discount lines | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to &#39;es&#39;]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**DiscountLinesResponse**](DiscountLinesResponse.md)

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

# **orders_delete_discount_lines**
> DiscountLinesResponse orders_delete_discount_lines(id, discount_lines_id, accept_language=accept_language, x_child_company_id=x_child_company_id)

Delete Discount

Delete an existing discount lines for an existing orden

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import conekta
from conekta.models.discount_lines_response import DiscountLinesResponse
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
    api_instance = conekta.DiscountsApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    discount_lines_id = 'dis_lin_2tQ974hSHcsdeSZHG' # str | identifier
    accept_language = 'es' # str | Use for knowing which language to use (optional) (default to 'es')
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Delete Discount
        api_response = api_instance.orders_delete_discount_lines(id, discount_lines_id, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of DiscountsApi->orders_delete_discount_lines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsApi->orders_delete_discount_lines: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **discount_lines_id** | **str**| identifier | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to &#39;es&#39;]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**DiscountLinesResponse**](DiscountLinesResponse.md)

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
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_update_discount_lines**
> DiscountLinesResponse orders_update_discount_lines(id, discount_lines_id, update_order_discount_lines_request, accept_language=accept_language, x_child_company_id=x_child_company_id)

Update Discount

Update an existing discount lines for an existing orden

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import conekta
from conekta.models.discount_lines_response import DiscountLinesResponse
from conekta.models.update_order_discount_lines_request import UpdateOrderDiscountLinesRequest
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
    api_instance = conekta.DiscountsApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    discount_lines_id = 'dis_lin_2tQ974hSHcsdeSZHG' # str | identifier
    update_order_discount_lines_request = conekta.UpdateOrderDiscountLinesRequest() # UpdateOrderDiscountLinesRequest | requested field for a discount lines
    accept_language = 'es' # str | Use for knowing which language to use (optional) (default to 'es')
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Update Discount
        api_response = api_instance.orders_update_discount_lines(id, discount_lines_id, update_order_discount_lines_request, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of DiscountsApi->orders_update_discount_lines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsApi->orders_update_discount_lines: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **discount_lines_id** | **str**| identifier | 
 **update_order_discount_lines_request** | [**UpdateOrderDiscountLinesRequest**](UpdateOrderDiscountLinesRequest.md)| requested field for a discount lines | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to &#39;es&#39;]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**DiscountLinesResponse**](DiscountLinesResponse.md)

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

