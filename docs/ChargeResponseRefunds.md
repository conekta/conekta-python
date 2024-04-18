# ChargeResponseRefunds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** | Indicates if there are more pages to be requested | 
**object** | **str** | Object type, in this case is list | 
**next_page_url** | **str** | URL of the next page. | [optional] 
**previous_page_url** | **str** | Url of the previous page. | [optional] 
**data** | [**List[ChargeResponseRefundsData]**](ChargeResponseRefundsData.md) | refunds | [optional] 

## Example

```python
from conekta.models.charge_response_refunds import ChargeResponseRefunds

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeResponseRefunds from a JSON string
charge_response_refunds_instance = ChargeResponseRefunds.from_json(json)
# print the JSON string representation of the object
print(ChargeResponseRefunds.to_json())

# convert the object into a dict
charge_response_refunds_dict = charge_response_refunds_instance.to_dict()
# create an instance of ChargeResponseRefunds from a dict
charge_response_refunds_from_dict = ChargeResponseRefunds.from_dict(charge_response_refunds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


