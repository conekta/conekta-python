# conekta.TransactionsApi

All URIs are relative to *https://api.conekta.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transaction**](TransactionsApi.md#get_transaction) | **GET** /transactions/{id} | Get transaction
[**get_transactions**](TransactionsApi.md#get_transactions) | **GET** /transactions | Get List transactions


# **get_transaction**
> TransactionResponse get_transaction(id, accept_language=accept_language, x_child_company_id=x_child_company_id)

Get transaction

Get the details of a transaction

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import conekta
from conekta.models.transaction_response import TransactionResponse
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
    api_instance = conekta.TransactionsApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    accept_language = 'es' # str | Use for knowing which language to use (optional) (default to 'es')
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Get transaction
        api_response = api_instance.get_transaction(id, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of TransactionsApi->get_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->get_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to &#39;es&#39;]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.conekta-v2.1.0+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  * Date - The date and time that the response was sent <br>  * Content-Type - The format of the response body <br>  * Content-Length - The length of the response body in bytes <br>  * Connection - The type of connection used to transfer the response <br>  * Conekta-Media-Type -  <br>  |
**401** | authentication error |  -  |
**404** | authentication error |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions**
> GetTransactionsResponse get_transactions(accept_language=accept_language, x_child_company_id=x_child_company_id, limit=limit, search=search, next=next, previous=previous)

Get List transactions

Get transaction details in the form of a list

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import conekta
from conekta.models.get_transactions_response import GetTransactionsResponse
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
    api_instance = conekta.TransactionsApi(api_client)
    accept_language = 'es' # str | Use for knowing which language to use (optional) (default to 'es')
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)
    limit = 20 # int | The numbers of items to return, the maximum value is 250 (optional) (default to 20)
    search = 'search_example' # str | General order search, e.g. by mail, reference etc. (optional)
    next = 'next_example' # str | next page (optional)
    previous = 'previous_example' # str | previous page (optional)

    try:
        # Get List transactions
        api_response = api_instance.get_transactions(accept_language=accept_language, x_child_company_id=x_child_company_id, limit=limit, search=search, next=next, previous=previous)
        print("The response of TransactionsApi->get_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->get_transactions: %s\n" % e)
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

[**GetTransactionsResponse**](GetTransactionsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.conekta-v2.1.0+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  * Date - The date and time that the response was sent <br>  * Content-Type - The format of the response body <br>  * Content-Length - The length of the response body in bytes <br>  * Connection - The type of connection used to transfer the response <br>  * Conekta-Media-Type -  <br>  |
**401** | authentication error |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

