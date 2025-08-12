
import time
import os
import conekta
from conekta.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = conekta.Configuration(
    access_token = os.environ["CONEKTA_PRIVATE_API_KEY"]
)


# Enter a context with an instance of the API client
with conekta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conekta.OrdersApi(api_client)
    order = conekta.OrderRequest(
        line_items=[
            conekta.Product(
                name='Test Product',
                quantity=1,
                unit_price=10000
            )
        ],
        customer_info=conekta.OrderRequestCustomerInfo(
           conekta.CustomerInfo(
               name='John Doe',
               email='john.doe@example.com',
               phone='555-555-5555'
           )
        ),
        currency='MXN',
        charges=[ 
            conekta.ChargeRequest(
                payment_method=conekta.ChargeRequestPaymentMethod(
                    oneof_schema_1_validator=conekta.PaymentMethodBnplRequest(
                        product_type='aplazo_bnpl',
                        type= 'bnpl',
                        success_url= 'https://www.example.com/success',
                        failure_url= 'https://www.example.com/failure',
                        cancel_url= 'https://www.example.com/cancel',
                    )
                )
            )
        ]

    ) 
    accept_language = 'es' # str | Use for knowing which language to use (optional) (default to 'es')

    try:
        # Create order
        api_response = api_instance.create_order(order, accept_language=accept_language)
        print("The response of OrdersApi->create_order:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrdersApi->create_order: %s\n" % e)
