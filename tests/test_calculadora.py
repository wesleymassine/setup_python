"""Testes para o módulo calculadora."""

import pytest

from src.calculadora import multiplicacao, saudacao, soma


class TestCalculadora:
    """Testes para funções de cálculo."""

    def test_soma_positivos(self):
        """Testa soma de números positivos."""
        assert soma(2, 3) == 5
        assert soma(10, 20) == 30

    def test_soma_negativos(self):
        """Testa soma de números negativos."""
        assert soma(-5, -3) == -8
        assert soma(-10, 5) == -5

    def test_multiplicacao(self):
        """Testa multiplicação."""
        assert multiplicacao(2, 3) == 6
        assert multiplicacao(5, 0) == 0
        assert multiplicacao(-2, 3) == -6

    @pytest.mark.parametrize(
        "a,b,esperado",
        [
            (1, 1, 2),
            (0, 0, 0),
            (100, 200, 300),
            (-5, 5, 0),
        ],
    )
    def test_soma_parametrizada(self, a, b, esperado):
        """Testa soma com múltiplos casos."""
        assert soma(a, b) == esperado


class TestSaudacao:
    """Testes para função de saudação."""

    def test_saudacao_basica(self):
        """Testa saudação básica."""
        assert saudacao("João") == "Olá, João!"
        assert saudacao("Maria") == "Olá, Maria!"

    def test_saudacao_vazia(self):
        """Testa saudação com string vazia."""
        assert saudacao("") == "Olá, !"
