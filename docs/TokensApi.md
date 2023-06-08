# conekta.TokensApi

All URIs are relative to *https://api.conekta.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token**](TokensApi.md#create_token) | **POST** /tokens | Create Token


# **create_token**
> TokenResponse create_token(token, accept_language=accept_language)

Create Token

Generate a payment token, to associate it with a card 

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import conekta
from conekta.models.token import Token
from conekta.models.token_response import TokenResponse
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
    api_instance = conekta.TokensApi(api_client)
    token = conekta.Token() # Token | requested field for token
    accept_language = 'es' # str | Use for knowing which language to use (optional) (default to 'es')

    try:
        # Create Token
        api_response = api_instance.create_token(token, accept_language=accept_language)
        print("The response of TokensApi->create_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokensApi->create_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | [**Token**](Token.md)| requested field for token | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to &#39;es&#39;]

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.conekta-v2.1.0+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  * Date - The date and time that the response was sent <br>  * Content-Type - The format of the response body <br>  * Content-Length - The length of the response body in bytes <br>  * Connection - The type of connection used to transfer the response <br>  * Conekta-Media-Type -  <br>  |
**401** | authentication error |  -  |
**422** | parameter validation error |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

