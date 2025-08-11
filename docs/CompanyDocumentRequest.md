# CompanyDocumentRequest

Request body for uploading a company document.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_classification** | **str** | Classification of the document.  | Tipo de archivo              | Descripción                                               | | :--------------------------- | :-------------------------------------------------------- | | &#x60;id_legal_representative&#x60;      | identificación oficial frente                             | | &#x60;id_legal_representative_back&#x60; | identificación oficial atrás                              | | &#x60;cfdi&#x60;                         | Prueba de situación fiscal                                | | &#x60;constitutive_act_basic&#x60;       | Acta constitutiva                                         | | &#x60;proof_of_address&#x60;             | Comprobante de domicilio del negocio                      | | &#x60;power_of_attonery&#x60;            | Poderes de representación                                 | | &#x60;deposit_account_cover&#x60;        | Carátula de la cuenta de depósito                         | | &#x60;permit_casino&#x60;                | Permiso ante SEGOB                                        | | &#x60;license_sanitation&#x60;           | Licencia sanitaria de COFEPRIS                            | | &#x60;registration_tourism&#x60;         | Inscripción ante el Registro Nacional de Turismo (SECTUR) |  | 
**content_type** | **str** | MIME type of the file. Allowed values depend on the &#x60;file_classification&#x60;. - &#x60;image/jpeg&#x60; - &#x60;image/png&#x60; - &#x60;application/pdf&#x60;  | 
**international** | **bool** | Indicates if the document is international. Defaults to false. | [optional] 
**file_name** | **str** | Name of the file being uploaded. | 
**file_data** | **bytearray** | Base64 encoded content of the file. | 

## Example

```python
from conekta.models.company_document_request import CompanyDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyDocumentRequest from a JSON string
company_document_request_instance = CompanyDocumentRequest.from_json(json)
# print the JSON string representation of the object
print(CompanyDocumentRequest.to_json())

# convert the object into a dict
company_document_request_dict = company_document_request_instance.to_dict()
# create an instance of CompanyDocumentRequest from a dict
company_document_request_from_dict = CompanyDocumentRequest.from_dict(company_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


