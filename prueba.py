import pyepayco.epayco as epayco

apiKey = "f00e61cf4df600d10eac941bdd3ebaa3"
privateKey = "1bef359945403a3d741407832d5059b5"
lenguage = "ES"
test = False
options={"apiKey":apiKey,"privateKey":privateKey,"test":test,"language":lenguage}

objepayco=epayco.Epayco(options)


# print(objepayco.bank.pseBank())
'''
pse_info = {
  "bank": "1022",
  "invoice": "1472050778",
  "description": "pay test",
  "value": "10000",
  "tax": "0",
  "tax_base": "0",
  "currency": "COP",
  "type_person": "0",
  "doc_type": "CC",
  "doc_number": "10000000",
  "name": "testing",
  "last_name": "PAYCO",
  "email": "no-responder@payco.co",
  "country": "CO",
  "cell_phone": "3010000001",
  "ip": "186.116.10.133",
  "url_response": "http://127.0.0.1:8000/respuesta-pse",
  "url_confirmation": "http://127.0.0.1:8000/confirmacion-pse",
  "method_confirmation": "GET",
}
'''
pse_info = {
    "banco": "1022",
    "factura": "1472050778",
    "descripcion": "Pago pruebas",
    "valor": "10000",
    "iva": "0",
    "baseiva": "0",
    "moneda": "COP",
    "tipo_persona": "0",
    "tipo_doc": "CC",
    "documento": "10358519",
    "nombres": "PRUEBAS",
    "apellidos": "PAYCO",
    "email": "no-responder@payco.co",
    "pais": "CO",
    "depto": "Antioquia",
    "ciudad": "Medellin",
    "telefono": "0000000",
    "celular": "3010000001",
    "direccion": "Calle 10 # 40-30",
    "ip": "186.116.10.133",
    "url_respuesta": "https://secure.payco.co/restpagos/testRest/endpagopse.php",
    "url_confirmacion": "https://secure.payco.co/restpagos/testRest/endpagopse.php",
    "metodoconfirmacion": "GET",
}

pse = objepayco.bank.create(pse_info)
print(pse)
