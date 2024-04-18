# conekta.TaxesApi

All URIs are relative to *https://api.conekta.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orders_create_taxes**](TaxesApi.md#orders_create_taxes) | **POST** /orders/{id}/tax_lines | Create Tax
[**orders_delete_taxes**](TaxesApi.md#orders_delete_taxes) | **DELETE** /orders/{id}/tax_lines/{tax_id} | Delete Tax
[**orders_update_taxes**](TaxesApi.md#orders_update_taxes) | **PUT** /orders/{id}/tax_lines/{tax_id} | Update Tax


# **orders_create_taxes**
> UpdateOrderTaxResponse orders_create_taxes(id, order_tax_request, accept_language=accept_language, x_child_company_id=x_child_company_id)

Create Tax

Create new taxes for an existing orden

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.order_tax_request import OrderTaxRequest
from conekta.models.update_order_tax_response import UpdateOrderTaxResponse
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
    api_instance = conekta.TaxesApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    order_tax_request = conekta.OrderTaxRequest() # OrderTaxRequest | requested field for a taxes
    accept_language = 'es' # str | Use for knowing which language to use (optional) (default to 'es')
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Create Tax
        api_response = api_instance.orders_create_taxes(id, order_tax_request, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of TaxesApi->orders_create_taxes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxesApi->orders_create_taxes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **order_tax_request** | [**OrderTaxRequest**](OrderTaxRequest.md)| requested field for a taxes | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to &#39;es&#39;]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**UpdateOrderTaxResponse**](UpdateOrderTaxResponse.md)

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

# **orders_delete_taxes**
> UpdateOrderTaxResponse orders_delete_taxes(id, tax_id, accept_language=accept_language, x_child_company_id=x_child_company_id)

Delete Tax

Delete taxes for an existing orden

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.update_order_tax_response import UpdateOrderTaxResponse
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
    api_instance = conekta.TaxesApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    tax_id = 'tax_lin_2tQ974hSHcsdeSZHG' # str | identifier
    accept_language = 'es' # str | Use for knowing which language to use (optional) (default to 'es')
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Delete Tax
        api_response = api_instance.orders_delete_taxes(id, tax_id, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of TaxesApi->orders_delete_taxes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxesApi->orders_delete_taxes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **tax_id** | **str**| identifier | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to &#39;es&#39;]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**UpdateOrderTaxResponse**](UpdateOrderTaxResponse.md)

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
**422** | parameter validation error |  -  |
**404** | not found entity |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_update_taxes**
> UpdateOrderTaxResponse orders_update_taxes(id, tax_id, update_order_tax_request, accept_language=accept_language, x_child_company_id=x_child_company_id)

Update Tax

Update taxes for an existing orden

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.update_order_tax_request import UpdateOrderTaxRequest
from conekta.models.update_order_tax_response import UpdateOrderTaxResponse
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
    api_instance = conekta.TaxesApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    tax_id = 'tax_lin_2tQ974hSHcsdeSZHG' # str | identifier
    update_order_tax_request = conekta.UpdateOrderTaxRequest() # UpdateOrderTaxRequest | requested field for taxes
    accept_language = 'es' # str | Use for knowing which language to use (optional) (default to 'es')
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Update Tax
        api_response = api_instance.orders_update_taxes(id, tax_id, update_order_tax_request, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of TaxesApi->orders_update_taxes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxesApi->orders_update_taxes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **tax_id** | **str**| identifier | 
 **update_order_tax_request** | [**UpdateOrderTaxRequest**](UpdateOrderTaxRequest.md)| requested field for taxes | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to &#39;es&#39;]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**UpdateOrderTaxResponse**](UpdateOrderTaxResponse.md)

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
**422** | parameter validation error |  -  |
**404** | not found entity |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

