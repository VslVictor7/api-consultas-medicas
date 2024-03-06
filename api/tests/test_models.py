from django.test import TestCase
from api.models import Profissional, Consulta

class ProfissionalTestCase(TestCase):
    def setUp(self):
        Profissional.objects.create(
            nome_completo='Fulano de Tal',
            nome_social='Fulano',
            profissao='Médico',
            endereco='Rua A, 123',
            contato=123456789
        )

    def test_profissional_creation(self):
        profissional = Profissional.objects.get(nome_completo='Fulano de Tal')
        self.assertEqual(profissional.nome_social, 'Fulano')
        self.assertEqual(profissional.profissao, 'Médico')
        self.assertEqual(profissional.endereco, 'Rua A, 123')
        self.assertEqual(profissional.contato, 123456789)


class ConsultaTestCase(TestCase):
    def setUp(self):
        profissional = Profissional.objects.create(
            nome_completo='Fulano de Tal',
            nome_social='Fulano',
            profissao='Médico',
            endereco='Rua A, 123',
            contato=123456789
        )
        Consulta.objects.create(
            id_prof=profissional,
            data_consulta='2024-03-05'
        )

    def test_consulta_creation(self):
        consulta = Consulta.objects.get(data_consulta='2024-03-05')
        self.assertEqual(consulta.id_prof.nome_completo, 'Fulano de Tal')
        self.assertEqual(consulta.id_prof.profissao, 'Médico')