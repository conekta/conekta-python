# conekta.ProductsApi

All URIs are relative to *https://api.conekta.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orders_create_product**](ProductsApi.md#orders_create_product) | **POST** /orders/{id}/line_items | Create Product
[**orders_delete_product**](ProductsApi.md#orders_delete_product) | **DELETE** /orders/{id}/line_items/{line_item_id} | Delete Product
[**orders_update_product**](ProductsApi.md#orders_update_product) | **PUT** /orders/{id}/line_items/{line_item_id} | Update Product


# **orders_create_product**
> ProductOrderResponse orders_create_product(id, product, accept_language=accept_language, x_child_company_id=x_child_company_id)

Create Product

Create a new product for an existing order.

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.product import Product
from conekta.models.product_order_response import ProductOrderResponse
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
    api_instance = conekta.ProductsApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    product = conekta.Product() # Product | requested field for a product
    accept_language = 'es' # str | Use for knowing which language to use (optional) (default to 'es')
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Create Product
        api_response = api_instance.orders_create_product(id, product, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of ProductsApi->orders_create_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->orders_create_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **product** | [**Product**](Product.md)| requested field for a product | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to &#39;es&#39;]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**ProductOrderResponse**](ProductOrderResponse.md)

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

# **orders_delete_product**
> ProductOrderResponse orders_delete_product(id, line_item_id, accept_language=accept_language, x_child_company_id=x_child_company_id)

Delete Product

Delete product for an existing orden

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.product_order_response import ProductOrderResponse
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
    api_instance = conekta.ProductsApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    line_item_id = 'line_item_2tQ8HkkfbauaKP9Ho' # str | identifier
    accept_language = 'es' # str | Use for knowing which language to use (optional) (default to 'es')
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Delete Product
        api_response = api_instance.orders_delete_product(id, line_item_id, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of ProductsApi->orders_delete_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->orders_delete_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **line_item_id** | **str**| identifier | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to &#39;es&#39;]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**ProductOrderResponse**](ProductOrderResponse.md)

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

# **orders_update_product**
> ProductOrderResponse orders_update_product(id, line_item_id, update_product, accept_language=accept_language, x_child_company_id=x_child_company_id)

Update Product

Update an existing product for an existing orden

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.product_order_response import ProductOrderResponse
from conekta.models.update_product import UpdateProduct
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
    api_instance = conekta.ProductsApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    line_item_id = 'line_item_2tQ8HkkfbauaKP9Ho' # str | identifier
    update_product = conekta.UpdateProduct() # UpdateProduct | requested field for products
    accept_language = 'es' # str | Use for knowing which language to use (optional) (default to 'es')
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Update Product
        api_response = api_instance.orders_update_product(id, line_item_id, update_product, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of ProductsApi->orders_update_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->orders_update_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **line_item_id** | **str**| identifier | 
 **update_product** | [**UpdateProduct**](UpdateProduct.md)| requested field for products | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to &#39;es&#39;]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**ProductOrderResponse**](ProductOrderResponse.md)

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

