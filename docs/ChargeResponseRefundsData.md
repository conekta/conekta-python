# ChargeResponseRefundsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** |  | 
**auth_code** | **str** |  | [optional] 
**created_at** | **int** |  | 
**expires_at** | **int** | refund expiration date | [optional] 
**id** | **str** |  | 
**object** | **str** |  | 
**status** | **str** | refund status | [optional] 

## Example

```python
from conekta.models.charge_response_refunds_data import ChargeResponseRefundsData

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeResponseRefundsData from a JSON string
charge_response_refunds_data_instance = ChargeResponseRefundsData.from_json(json)
# print the JSON string representation of the object
print(ChargeResponseRefundsData.to_json())

# convert the object into a dict
charge_response_refunds_data_dict = charge_response_refunds_data_instance.to_dict()
# create an instance of ChargeResponseRefundsData from a dict
charge_response_refunds_data_from_dict = ChargeResponseRefundsData.from_dict(charge_response_refunds_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


