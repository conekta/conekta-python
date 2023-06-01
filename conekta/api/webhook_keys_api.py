# coding: utf-8

"""
    Conekta API

    Conekta sdk  # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Contact: engineering@conekta.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictStr, conint

from typing import Optional

from conekta.models.get_webhook_keys_response import GetWebhookKeysResponse
from conekta.models.webhook_key_create_response import WebhookKeyCreateResponse
from conekta.models.webhook_key_delete_response import WebhookKeyDeleteResponse
from conekta.models.webhook_key_request import WebhookKeyRequest
from conekta.models.webhook_key_response import WebhookKeyResponse
from conekta.models.webhook_key_update_request import WebhookKeyUpdateRequest

from conekta.api_client import ApiClient
from conekta.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class WebhookKeysApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def create_webhook_key(self, accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, webhook_key_request : Optional[WebhookKeyRequest] = None, **kwargs) -> WebhookKeyCreateResponse:  # noqa: E501
        """Create Webhook Key  # noqa: E501

        Create a webhook key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_webhook_key(accept_language, webhook_key_request, async_req=True)
        >>> result = thread.get()

        :param accept_language: Use for knowing which language to use
        :type accept_language: str
        :param webhook_key_request:
        :type webhook_key_request: WebhookKeyRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: WebhookKeyCreateResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.create_webhook_key_with_http_info(accept_language, webhook_key_request, **kwargs)  # noqa: E501

    @validate_arguments
    def create_webhook_key_with_http_info(self, accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, webhook_key_request : Optional[WebhookKeyRequest] = None, **kwargs):  # noqa: E501
        """Create Webhook Key  # noqa: E501

        Create a webhook key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_webhook_key_with_http_info(accept_language, webhook_key_request, async_req=True)
        >>> result = thread.get()

        :param accept_language: Use for knowing which language to use
        :type accept_language: str
        :param webhook_key_request:
        :type webhook_key_request: WebhookKeyRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(WebhookKeyCreateResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'accept_language',
            'webhook_key_request'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_webhook_key" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['accept_language']:
            _header_params['Accept-Language'] = _params['accept_language']

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None
        if _params['webhook_key_request']:
            _body_params = _params['webhook_key_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.conekta-v2.1.0+json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['bearerAuth']  # noqa: E501

        _response_types_map = {
            '200': "WebhookKeyCreateResponse",
            '401': "Error",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/webhook_keys', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def delete_webhook_key(self, id : Annotated[StrictStr, Field(..., description="Identifier of the resource")], accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, **kwargs) -> WebhookKeyDeleteResponse:  # noqa: E501
        """Delete Webhook key  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_webhook_key(id, accept_language, async_req=True)
        >>> result = thread.get()

        :param id: Identifier of the resource (required)
        :type id: str
        :param accept_language: Use for knowing which language to use
        :type accept_language: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: WebhookKeyDeleteResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_webhook_key_with_http_info(id, accept_language, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_webhook_key_with_http_info(self, id : Annotated[StrictStr, Field(..., description="Identifier of the resource")], accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, **kwargs):  # noqa: E501
        """Delete Webhook key  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_webhook_key_with_http_info(id, accept_language, async_req=True)
        >>> result = thread.get()

        :param id: Identifier of the resource (required)
        :type id: str
        :param accept_language: Use for knowing which language to use
        :type accept_language: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(WebhookKeyDeleteResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'accept_language'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_webhook_key" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['accept_language']:
            _header_params['Accept-Language'] = _params['accept_language']

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.conekta-v2.1.0+json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['bearerAuth']  # noqa: E501

        _response_types_map = {
            '200': "WebhookKeyDeleteResponse",
            '401': "Error",
            '404': "Error",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/webhook_keys/{id}', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_webhook_key(self, id : Annotated[StrictStr, Field(..., description="Identifier of the resource")], accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, x_child_company_id : Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None, **kwargs) -> WebhookKeyResponse:  # noqa: E501
        """Get Webhook Key  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_webhook_key(id, accept_language, x_child_company_id, async_req=True)
        >>> result = thread.get()

        :param id: Identifier of the resource (required)
        :type id: str
        :param accept_language: Use for knowing which language to use
        :type accept_language: str
        :param x_child_company_id: In the case of a holding company, the company id of the child company to which will process the request.
        :type x_child_company_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: WebhookKeyResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_webhook_key_with_http_info(id, accept_language, x_child_company_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_webhook_key_with_http_info(self, id : Annotated[StrictStr, Field(..., description="Identifier of the resource")], accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, x_child_company_id : Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None, **kwargs):  # noqa: E501
        """Get Webhook Key  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_webhook_key_with_http_info(id, accept_language, x_child_company_id, async_req=True)
        >>> result = thread.get()

        :param id: Identifier of the resource (required)
        :type id: str
        :param accept_language: Use for knowing which language to use
        :type accept_language: str
        :param x_child_company_id: In the case of a holding company, the company id of the child company to which will process the request.
        :type x_child_company_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(WebhookKeyResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'accept_language',
            'x_child_company_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_webhook_key" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['accept_language']:
            _header_params['Accept-Language'] = _params['accept_language']
        if _params['x_child_company_id']:
            _header_params['X-Child-Company-Id'] = _params['x_child_company_id']

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.conekta-v2.1.0+json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['bearerAuth']  # noqa: E501

        _response_types_map = {
            '200': "WebhookKeyResponse",
            '401': "Error",
            '404': "Error",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/webhook_keys/{id}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_webhook_keys(self, accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, x_child_company_id : Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None, limit : Annotated[Optional[conint(strict=True, le=250, ge=1)], Field(description="The numbers of items to return, the maximum value is 250")] = None, search : Annotated[Optional[StrictStr], Field(description="General order search, e.g. by mail, reference etc.")] = None, next : Annotated[Optional[StrictStr], Field(description="next page")] = None, previous : Annotated[Optional[StrictStr], Field(description="previous page")] = None, **kwargs) -> GetWebhookKeysResponse:  # noqa: E501
        """Get List of Webhook Keys  # noqa: E501

        Consume the list of webhook keys you have  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_webhook_keys(accept_language, x_child_company_id, limit, search, next, previous, async_req=True)
        >>> result = thread.get()

        :param accept_language: Use for knowing which language to use
        :type accept_language: str
        :param x_child_company_id: In the case of a holding company, the company id of the child company to which will process the request.
        :type x_child_company_id: str
        :param limit: The numbers of items to return, the maximum value is 250
        :type limit: int
        :param search: General order search, e.g. by mail, reference etc.
        :type search: str
        :param next: next page
        :type next: str
        :param previous: previous page
        :type previous: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetWebhookKeysResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_webhook_keys_with_http_info(accept_language, x_child_company_id, limit, search, next, previous, **kwargs)  # noqa: E501

    @validate_arguments
    def get_webhook_keys_with_http_info(self, accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, x_child_company_id : Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None, limit : Annotated[Optional[conint(strict=True, le=250, ge=1)], Field(description="The numbers of items to return, the maximum value is 250")] = None, search : Annotated[Optional[StrictStr], Field(description="General order search, e.g. by mail, reference etc.")] = None, next : Annotated[Optional[StrictStr], Field(description="next page")] = None, previous : Annotated[Optional[StrictStr], Field(description="previous page")] = None, **kwargs):  # noqa: E501
        """Get List of Webhook Keys  # noqa: E501

        Consume the list of webhook keys you have  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_webhook_keys_with_http_info(accept_language, x_child_company_id, limit, search, next, previous, async_req=True)
        >>> result = thread.get()

        :param accept_language: Use for knowing which language to use
        :type accept_language: str
        :param x_child_company_id: In the case of a holding company, the company id of the child company to which will process the request.
        :type x_child_company_id: str
        :param limit: The numbers of items to return, the maximum value is 250
        :type limit: int
        :param search: General order search, e.g. by mail, reference etc.
        :type search: str
        :param next: next page
        :type next: str
        :param previous: previous page
        :type previous: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetWebhookKeysResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'accept_language',
            'x_child_company_id',
            'limit',
            'search',
            'next',
            'previous'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_webhook_keys" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))
        if _params.get('search') is not None:  # noqa: E501
            _query_params.append(('search', _params['search']))
        if _params.get('next') is not None:  # noqa: E501
            _query_params.append(('next', _params['next']))
        if _params.get('previous') is not None:  # noqa: E501
            _query_params.append(('previous', _params['previous']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['accept_language']:
            _header_params['Accept-Language'] = _params['accept_language']
        if _params['x_child_company_id']:
            _header_params['X-Child-Company-Id'] = _params['x_child_company_id']

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.conekta-v2.1.0+json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['bearerAuth']  # noqa: E501

        _response_types_map = {
            '200': "GetWebhookKeysResponse",
            '401': "Error",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/webhook_keys', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def update_webhook_key(self, id : Annotated[StrictStr, Field(..., description="Identifier of the resource")], accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, webhook_key_update_request : Optional[WebhookKeyUpdateRequest] = None, **kwargs) -> WebhookKeyResponse:  # noqa: E501
        """Update Webhook Key  # noqa: E501

        updates an existing webhook key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_webhook_key(id, accept_language, webhook_key_update_request, async_req=True)
        >>> result = thread.get()

        :param id: Identifier of the resource (required)
        :type id: str
        :param accept_language: Use for knowing which language to use
        :type accept_language: str
        :param webhook_key_update_request:
        :type webhook_key_update_request: WebhookKeyUpdateRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: WebhookKeyResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.update_webhook_key_with_http_info(id, accept_language, webhook_key_update_request, **kwargs)  # noqa: E501

    @validate_arguments
    def update_webhook_key_with_http_info(self, id : Annotated[StrictStr, Field(..., description="Identifier of the resource")], accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, webhook_key_update_request : Optional[WebhookKeyUpdateRequest] = None, **kwargs):  # noqa: E501
        """Update Webhook Key  # noqa: E501

        updates an existing webhook key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_webhook_key_with_http_info(id, accept_language, webhook_key_update_request, async_req=True)
        >>> result = thread.get()

        :param id: Identifier of the resource (required)
        :type id: str
        :param accept_language: Use for knowing which language to use
        :type accept_language: str
        :param webhook_key_update_request:
        :type webhook_key_update_request: WebhookKeyUpdateRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(WebhookKeyResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'accept_language',
            'webhook_key_update_request'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_webhook_key" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['accept_language']:
            _header_params['Accept-Language'] = _params['accept_language']

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None
        if _params['webhook_key_update_request']:
            _body_params = _params['webhook_key_update_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.conekta-v2.1.0+json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['bearerAuth']  # noqa: E501

        _response_types_map = {
            '200': "WebhookKeyResponse",
            '404': "Error",
            '401': "Error",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/webhook_keys/{id}', 'PUT',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
