# conekta.AntifraudApi

All URIs are relative to *https://api.conekta.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_rule_blacklist**](AntifraudApi.md#create_rule_blacklist) | **POST** /antifraud/blacklists | Create blacklisted rule
[**create_rule_whitelist**](AntifraudApi.md#create_rule_whitelist) | **POST** /antifraud/whitelists | Create whitelisted rule
[**delete_rule_blacklist**](AntifraudApi.md#delete_rule_blacklist) | **DELETE** /antifraud/blacklists/{id} | Delete blacklisted rule
[**delete_rule_whitelist**](AntifraudApi.md#delete_rule_whitelist) | **DELETE** /antifraud/whitelists/{id} | Delete whitelisted rule
[**get_rule_blacklist**](AntifraudApi.md#get_rule_blacklist) | **GET** /antifraud/blacklists | Get list of blacklisted rules
[**get_rule_whitelist**](AntifraudApi.md#get_rule_whitelist) | **GET** /antifraud/whitelists | Get a list of whitelisted rules


# **create_rule_blacklist**
> BlacklistRuleResponse create_rule_blacklist(create_risk_rules_data, accept_language=accept_language)

Create blacklisted rule

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.blacklist_rule_response import BlacklistRuleResponse
from conekta.models.create_risk_rules_data import CreateRiskRulesData
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
    api_instance = conekta.AntifraudApi(api_client)
    create_risk_rules_data = conekta.CreateRiskRulesData() # CreateRiskRulesData | requested field for blacklist rule
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)

    try:
        # Create blacklisted rule
        api_response = api_instance.create_rule_blacklist(create_risk_rules_data, accept_language=accept_language)
        print("The response of AntifraudApi->create_rule_blacklist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AntifraudApi->create_rule_blacklist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_risk_rules_data** | [**CreateRiskRulesData**](CreateRiskRulesData.md)| requested field for blacklist rule | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]

### Return type

[**BlacklistRuleResponse**](BlacklistRuleResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully registered rule |  -  |
**401** | authentication error |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_rule_whitelist**
> WhitelistlistRuleResponse create_rule_whitelist(accept_language=accept_language, create_risk_rules_data=create_risk_rules_data)

Create whitelisted rule

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.create_risk_rules_data import CreateRiskRulesData
from conekta.models.whitelistlist_rule_response import WhitelistlistRuleResponse
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
    api_instance = conekta.AntifraudApi(api_client)
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)
    create_risk_rules_data = conekta.CreateRiskRulesData() # CreateRiskRulesData |  (optional)

    try:
        # Create whitelisted rule
        api_response = api_instance.create_rule_whitelist(accept_language=accept_language, create_risk_rules_data=create_risk_rules_data)
        print("The response of AntifraudApi->create_rule_whitelist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AntifraudApi->create_rule_whitelist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]
 **create_risk_rules_data** | [**CreateRiskRulesData**](CreateRiskRulesData.md)|  | [optional] 

### Return type

[**WhitelistlistRuleResponse**](WhitelistlistRuleResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully registered rule |  -  |
**401** | authentication error |  -  |
**403** | forbidden error |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rule_blacklist**
> DeletedBlacklistRuleResponse delete_rule_blacklist(id, accept_language=accept_language, x_child_company_id=x_child_company_id)

Delete blacklisted rule

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.deleted_blacklist_rule_response import DeletedBlacklistRuleResponse
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
    api_instance = conekta.AntifraudApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Delete blacklisted rule
        api_response = api_instance.delete_rule_blacklist(id, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of AntifraudApi->delete_rule_blacklist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AntifraudApi->delete_rule_blacklist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**DeletedBlacklistRuleResponse**](DeletedBlacklistRuleResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully deleted rule |  -  |
**401** | authentication error |  -  |
**404** | not found entity |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rule_whitelist**
> DeletedWhitelistRuleResponse delete_rule_whitelist(id, accept_language=accept_language, x_child_company_id=x_child_company_id)

Delete whitelisted rule

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.deleted_whitelist_rule_response import DeletedWhitelistRuleResponse
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
    api_instance = conekta.AntifraudApi(api_client)
    id = '6307a60c41de27127515a575' # str | Identifier of the resource
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)
    x_child_company_id = '6441b6376b60c3a638da80af' # str | In the case of a holding company, the company id of the child company to which will process the request. (optional)

    try:
        # Delete whitelisted rule
        api_response = api_instance.delete_rule_whitelist(id, accept_language=accept_language, x_child_company_id=x_child_company_id)
        print("The response of AntifraudApi->delete_rule_whitelist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AntifraudApi->delete_rule_whitelist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource | 
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]
 **x_child_company_id** | **str**| In the case of a holding company, the company id of the child company to which will process the request. | [optional] 

### Return type

[**DeletedWhitelistRuleResponse**](DeletedWhitelistRuleResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully deleted rule |  -  |
**401** | authentication error |  -  |
**403** | forbidden error |  -  |
**404** | not found entity |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule_blacklist**
> RiskRulesList get_rule_blacklist(accept_language=accept_language)

Get list of blacklisted rules

Return all rules

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.risk_rules_list import RiskRulesList
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
    api_instance = conekta.AntifraudApi(api_client)
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)

    try:
        # Get list of blacklisted rules
        api_response = api_instance.get_rule_blacklist(accept_language=accept_language)
        print("The response of AntifraudApi->get_rule_blacklist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AntifraudApi->get_rule_blacklist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]

### Return type

[**RiskRulesList**](RiskRulesList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All the rules |  -  |
**401** | authentication error |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule_whitelist**
> RiskRulesList get_rule_whitelist(accept_language=accept_language)

Get a list of whitelisted rules

Return all rules

### Example

* Bearer Authentication (bearerAuth):

```python
import conekta
from conekta.models.risk_rules_list import RiskRulesList
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
    api_instance = conekta.AntifraudApi(api_client)
    accept_language = es # str | Use for knowing which language to use (optional) (default to es)

    try:
        # Get a list of whitelisted rules
        api_response = api_instance.get_rule_whitelist(accept_language=accept_language)
        print("The response of AntifraudApi->get_rule_whitelist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AntifraudApi->get_rule_whitelist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Use for knowing which language to use | [optional] [default to es]

### Return type

[**RiskRulesList**](RiskRulesList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.conekta-v2.2.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All the rules |  -  |
**401** | authentication error |  -  |
**403** | forbidden error |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

