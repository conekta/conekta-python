# conekta.PaymentMethodsApi

All URIs are relative to *https://api.conekta.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customer_payment_methods**](PaymentMethodsApi.md#create_customer_payment_methods) | **POST** /customers/{id}/payment_sources | Create Payment Method
[**delete_customer_payment_methods**](PaymentMethodsApi.md#delete_customer_payment_methods) | **DELETE** /customers/{id}/payment_sources/{payment_method_id} | Delete Payment Method
[**get_customer_payment_methods**](PaymentMethodsApi.md#get_customer_payment_methods) | **GET** /customers/{id}/payment_sources | Get Payment Methods
[**update_customer_payment_methods**](PaymentMethodsApi.md#update_customer_payment_methods) | **PUT** /customers/{id}/payment_sources/{payment_method_id} | Update Payment Method


# **create_customer_payment_methods**
> CreateCustomerPaymentMethodsResponse create_customer_payment_methods(id, create_customer_payment_methods_request, accept_language=accept_language, x_child_company_id=x_child_company_id)

Create Payment Method

Create a payment method for a customer.

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.create_customer_payment_methods_request import CreateCustomerPaymentMethodsRequest
from conekta.models.create_customer_payment_methods_response import CreateCustomerPaymentMethodsResponse
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
    api_instance = conekta.PaymentMethodsApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    create_customer_payment_methods_request = {"type":"card","token_id":"tok_test_visa_4242"} # CreateCustomerPaymentMethodsRequest | requested field for customer payment methods
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Create Payment Method
        api_response = api_instance.create_customer_payment_methods(id, create_customer_payment_methods_request, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of PaymentMethodsApi->create_customer_payment_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsApi->create_customer_payment_methods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **create_customer_payment_methods_request** | [**CreateCustomerPaymentMethodsRequest**](CreateCustomerPaymentMethodsRequest.md)| requested field for customer payment methods | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**CreateCustomerPaymentMethodsResponse**](CreateCustomerPaymentMethodsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.conekta-v2.1.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**401** | authentication error |  -  |
**404** | not found entity |  -  |
**422** | parameter validation error |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer_payment_methods**
> UpdateCustomerPaymentMethodsResponse delete_customer_payment_methods(id, payment_method_id, accept_language=accept_language, x_child_company_id=x_child_company_id)

Delete Payment Method

Delete an existing payment method

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.update_customer_payment_methods_response import UpdateCustomerPaymentMethodsResponse
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
    api_instance = conekta.PaymentMethodsApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    payment_method_id = 'src_2tQ974hSHcsdeSZHG' # str | Identifier of the payment method
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Delete Payment Method
        api_response = api_instance.delete_customer_payment_methods(id, payment_method_id, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of PaymentMethodsApi->delete_customer_payment_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsApi->delete_customer_payment_methods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **payment_method_id** | **str**| Identifier of the payment method | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**UpdateCustomerPaymentMethodsResponse**](UpdateCustomerPaymentMethodsResponse.md)

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
**404** | not found entity |  -  |
**422** | parameter validation error |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_payment_methods**
> GetPaymentMethodResponse get_customer_payment_methods(id, accept_language=accept_language, x_child_company_id=x_child_company_id, limit=limit, next=next, previous=previous, search=search)

Get Payment Methods

Get a list of Payment Methods

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.get_payment_method_response import GetPaymentMethodResponse
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
    api_instance = conekta.PaymentMethodsApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)
    limit = 20 # int | The numbers of items to return, the maximum value is 250 (optional) (default to 20)
    next = 'next_example' # str | next page (optional)
    previous = 'previous_example' # str | previous page (optional)
    search = 'search_example' # str | General order search, e.g. by mail, reference etc. (optional)

    try:
        # Get Payment Methods
        api_response = api_instance.get_customer_payment_methods(id, accept_language=accept_language, x_child_company_id=x_child_company_id, limit=limit, next=next, previous=previous, search=search)
        print("The response of PaymentMethodsApi->get_customer_payment_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsApi->get_customer_payment_methods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 
 **limit** | **int**| The numbers of items to return, the maximum value is 250 | [optional] [default to 20]
 **next** | **str**| next page | [optional] 
 **previous** | **str**| previous page | [optional] 
 **search** | **str**| General order search, e.g. by mail, reference etc. | [optional] 

### Return type

[**GetPaymentMethodResponse**](GetPaymentMethodResponse.md)

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
**404** | not found entity |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer_payment_methods**
> UpdateCustomerPaymentMethodsResponse update_customer_payment_methods(id, payment_method_id, update_payment_methods, accept_language=accept_language, x_child_company_id=x_child_company_id)

Update Payment Method

Gets a payment Method that corresponds to a customer ID.

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.update_customer_payment_methods_response import UpdateCustomerPaymentMethodsResponse
from conekta.models.update_payment_methods import UpdatePaymentMethods
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
    api_instance = conekta.PaymentMethodsApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    payment_method_id = 'src_2tQ974hSHcsdeSZHG' # str | Identifier of the payment method
    update_payment_methods = conekta.UpdatePaymentMethods() # UpdatePaymentMethods | requested field for customer payment methods
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Update Payment Method
        api_response = api_instance.update_customer_payment_methods(id, payment_method_id, update_payment_methods, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of PaymentMethodsApi->update_customer_payment_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsApi->update_customer_payment_methods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **payment_method_id** | **str**| Identifier of the payment method | 
 **update_payment_methods** | [**UpdatePaymentMethods**](UpdatePaymentMethods.md)| requested field for customer payment methods | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**UpdateCustomerPaymentMethodsResponse**](UpdateCustomerPaymentMethodsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.conekta-v2.1.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**401** | authentication error |  -  |
**404** | not found entity |  -  |
**422** | parameter validation error |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

