import pyepayco.epayco as epayco
import unittest


class EpaycoTest(unittest.TestCase):

    def __init__(self):
        self.apiKey = "491d6a0b6e992cf924edd8d3d088aff1"
        self.privateKey = "268c8e0162990cf2ce97fa7ade2eff5a"
        self.language = "ES"
        self.test = True
        self.options = {"apiKey": self.apiKey, "privateKey": self.privateKey, "test": self.test,
                        "language": self.language}
        self.switch = False
        self.epayco = epayco.Epayco(self.options)

    def test_createplan(self):
        dataplan = {
            "id_plan": "plangold",
            "name": "Plan Gold",
            "description": "Plan gold gym",
            "amount": 80000,
            "currency": "cop",
            "interval": "month",
            "interval_count": 1,
            "trial_days": 30,
            "public_key": self.apiKey
        }

        plan = self.epayco.plan.create(dataplan)

        self.assertTrue(len(plan['data']['id']) > 0)

    def test_pse(self):
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

        pse = self.epayco.bank.create(pse_info)

        self.assertTrue(len(pse['data']['transactionID']) > 0)

    '''
    def test_cash_baloto(self):
        cash_info = {
            "invoice": "1472050778",
            "description": "pay test",
            "value": "20000",
            "tax": "0",
            "tax_base": "0",
            "currency": "COP",
            "type_person": "0",
            "doc_type": "CC",
            "doc_number": "100000",
            "name": "testing",
            "last_name": "PAYCO",
            "email": "test@mailinator.com",
            "cell_phone": "3010000001",
            "end_date": "2017-12-05",
            "ip": "186.116.10.133",
            "url_response": "https://tudominio.com/respuesta.php",
            "url_confirmation": "https://tudominio.com/confirmacion.php",
            "method_confirmation": "GET",

        }

        cash = self.epayco.cash.create('baloto', cash_info)

        self.assertTrue(cash['data']['success'])
    '''

    if __name__ == "__main__":
        unittest.main()
