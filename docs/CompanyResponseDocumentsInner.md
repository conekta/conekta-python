# CompanyResponseDocumentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_classification** | **str** | Classification of the document.  | Tipo de archivo              | Descripción                                               | | :--------------------------- | :-------------------------------------------------------- | | &#x60;id_legal_representative&#x60;      | identificación oficial frente                             | | &#x60;id_legal_representative_back&#x60; | identificación oficial atrás                              | | &#x60;cfdi&#x60;                         | Prueba de situación fiscal                                | | &#x60;constitutive_act_basic&#x60;       | Acta constitutiva                                         | | &#x60;proof_of_address&#x60;             | Comprobante de domicilio del negocio                      | | &#x60;power_of_attonery&#x60;            | Poderes de representación                                 | | &#x60;deposit_account_cover&#x60;        | Carátula de la cuenta de depósito                         | | &#x60;permit_casino&#x60;                | Permiso ante SEGOB                                        | | &#x60;license_sanitation&#x60;           | Licencia sanitaria de COFEPRIS                            | | &#x60;registration_tourism&#x60;         | Inscripción ante el Registro Nacional de Turismo (SECTUR) |  | [optional] 
**status** | **str** | The status of the document. | [optional] 
**file_name** | **str** | The name of the file. | [optional] 

## Example

```python
from conekta.models.company_response_documents_inner import CompanyResponseDocumentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyResponseDocumentsInner from a JSON string
company_response_documents_inner_instance = CompanyResponseDocumentsInner.from_json(json)
# print the JSON string representation of the object
print(CompanyResponseDocumentsInner.to_json())

# convert the object into a dict
company_response_documents_inner_dict = company_response_documents_inner_instance.to_dict()
# create an instance of CompanyResponseDocumentsInner from a dict
company_response_documents_inner_from_dict = CompanyResponseDocumentsInner.from_dict(company_response_documents_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


