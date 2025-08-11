# conekta.CompaniesApi

All URIs are relative to *https://api.conekta.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_company**](CompaniesApi.md#create_company) | **POST** /companies | Create Company
[**get_companies**](CompaniesApi.md#get_companies) | **GET** /companies | Get List of Companies
[**get_company**](CompaniesApi.md#get_company) | **GET** /companies/{id} | Get Company
[**get_company_documents**](CompaniesApi.md#get_company_documents) | **GET** /companies/{company_id}/documents | Get Company Documents
[**update_company_document**](CompaniesApi.md#update_company_document) | **PATCH** /companies/{company_id}/document | Update Company Document
[**upload_company_document**](CompaniesApi.md#upload_company_document) | **POST** /companies/{company_id}/document | Upload Company Document


# **create_company**
> CompanyResponse create_company(create_company_request)

Create Company

Create a new company.

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.company_response import CompanyResponse
from conekta.models.create_company_request import CreateCompanyRequest
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
    api_instance = conekta.CompaniesApi(api_client)
    create_company_request = conekta.CreateCompanyRequest() # CreateCompanyRequest | Company data

    try:
        # Create Company
        api_response = api_instance.create_company(create_company_request)
        print("The response of CompaniesApi->create_company:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->create_company: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_company_request** | [**CreateCompanyRequest**](CreateCompanyRequest.md)| Company data | 

### Return type

[**CompanyResponse**](CompanyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Company created successfully |  * Date - The date and time that the response was sent <br>  * Content-Type - The format of the response body <br>  * Content-Length - The length of the response body in bytes <br>  * Connection - The type of connection used to transfer the response <br>  * Conekta-Media-Type -  <br>  |
**401** | authentication error |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_companies**
> GetCompaniesResponse get_companies(accept_language=accept_language, limit=limit, search=search, next=next, previous=previous)

Get List of Companies

Consume the list of child companies.  This is used for holding companies with several child entities.

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.get_companies_response import GetCompaniesResponse
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
    api_instance = conekta.CompaniesApi(api_client)
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)
    limit = 20 # int | The numbers of items to return, the maximum value is 250 (optional) (default to 20)
    search = 'search_example' # str | General order search, e.g. by mail, reference etc. (optional)
    next = 'next_example' # str | next page (optional)
    previous = 'previous_example' # str | previous page (optional)

    try:
        # Get List of Companies
        api_response = api_instance.get_companies(accept_language=accept_language, limit=limit, search=search, next=next, previous=previous)
        print("The response of CompaniesApi->get_companies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->get_companies: %s\n" % e)
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

[**GetCompaniesResponse**](GetCompaniesResponse.md)

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
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company**
> CompanyResponse get_company(id, accept_language=accept_language)

Get Company

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.company_response import CompanyResponse
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
    api_instance = conekta.CompaniesApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)

    try:
        # Get Company
        api_response = api_instance.get_company(id, accept_language=accept_language)
        print("The response of CompaniesApi->get_company:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->get_company: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]

### Return type

[**CompanyResponse**](CompanyResponse.md)

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

# **get_company_documents**
> List[CompanyDocumentResponse] get_company_documents(company_id, accept_language=accept_language)

Get Company Documents

Retrieve a list of documents associated with a specific company.

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.company_document_response import CompanyDocumentResponse
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
    api_instance = conekta.CompaniesApi(api_client)
    company_id = '6307a60c41de27127515a575' # str | The unique identifier of the company.
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)

    try:
        # Get Company Documents
        api_response = api_instance.get_company_documents(company_id, accept_language=accept_language)
        print("The response of CompaniesApi->get_company_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->get_company_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company. | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]

### Return type

[**List[CompanyDocumentResponse]**](CompanyDocumentResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of documents for the company. |  * Date - The date and time that the response was sent <br>  * Content-Type - The format of the response body <br>  * Content-Length - The length of the response body in bytes <br>  * Connection - The type of connection used to transfer the response <br>  * Conekta-Media-Type -  <br>  |
**401** | authentication error |  -  |
**404** | not found entity |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_company_document**
> CompanyDocumentResponse update_company_document(company_id, company_document_request, accept_language=accept_language)

Update Company Document

Updates an existing document associated with a specific company.

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.company_document_request import CompanyDocumentRequest
from conekta.models.company_document_response import CompanyDocumentResponse
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
    api_instance = conekta.CompaniesApi(api_client)
    company_id = '6827206b1ec60400015eb09a' # str | The unique identifier of the company.
    company_document_request = conekta.CompanyDocumentRequest() # CompanyDocumentRequest | Document information to update.
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)

    try:
        # Update Company Document
        api_response = api_instance.update_company_document(company_id, company_document_request, accept_language=accept_language)
        print("The response of CompaniesApi->update_company_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->update_company_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company. | 
 **company_document_request** | [**CompanyDocumentRequest**](CompanyDocumentRequest.md)| Document information to update. | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]

### Return type

[**CompanyDocumentResponse**](CompanyDocumentResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document updated successfully. |  * Date - The date and time that the response was sent <br>  * Content-Type - The format of the response body <br>  * Content-Length - The length of the response body in bytes <br>  * Connection - The type of connection used to transfer the response <br>  * Conekta-Media-Type -  <br>  |
**401** | authentication error |  -  |
**404** | not found entity |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_company_document**
> CompanyDocumentResponse upload_company_document(company_id, company_document_request, accept_language=accept_language)

Upload Company Document

Uploads a document associated with a specific company.

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.company_document_request import CompanyDocumentRequest
from conekta.models.company_document_response import CompanyDocumentResponse
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
    api_instance = conekta.CompaniesApi(api_client)
    company_id = '6827206b1ec60400015eb09a' # str | The unique identifier of the company.
    company_document_request = conekta.CompanyDocumentRequest() # CompanyDocumentRequest | Document information to upload.
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)

    try:
        # Upload Company Document
        api_response = api_instance.upload_company_document(company_id, company_document_request, accept_language=accept_language)
        print("The response of CompaniesApi->upload_company_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->upload_company_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company. | 
 **company_document_request** | [**CompanyDocumentRequest**](CompanyDocumentRequest.md)| Document information to upload. | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]

### Return type

[**CompanyDocumentResponse**](CompanyDocumentResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Document uploaded successfully. |  * Date - The date and time that the response was sent <br>  * Content-Type - The format of the response body <br>  * Content-Length - The length of the response body in bytes <br>  * Connection - The type of connection used to transfer the response <br>  * Conekta-Media-Type -  <br>  |
**401** | authentication error |  -  |
**404** | not found entity |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

