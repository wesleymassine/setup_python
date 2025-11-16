"""Tests for the calculadora module."""

import pytest

from src.calculadora import multiplicacao, saudacao, soma


class TestCalculadora:
    """Tests for calculation functions."""

    def test_soma_positivos(self):
        """Test sum of positive numbers."""
        assert soma(2, 3) == 5
        assert soma(10, 20) == 30

    def test_soma_negativos(self):
        """Test sum of negative numbers."""
        assert soma(-5, -3) == -8
        assert soma(-10, 5) == -5

    def test_multiplicacao(self):
        """Test multiplication."""
        assert multiplicacao(2, 3) == 6
        assert multiplicacao(5, 0) == 0
        assert multiplicacao(-2, 3) == -6

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (1, 1, 2),
            (0, 0, 0),
            (100, 200, 300),
            (-5, 5, 0),
        ],
    )
    def test_soma_parametrizada(self, a, b, expected):
        """Test sum with multiple cases."""
        assert soma(a, b) == expected


class TestSaudacao:
    """Tests for greeting function."""

    def test_saudacao_basica(self):
        """Test basic greeting."""
        assert saudacao("João") == "Olá, João!"
        assert saudacao("Maria") == "Olá, Maria!"

    def test_saudacao_vazia(self):
        """Test greeting with empty string."""
        assert saudacao("") == "Olá, !"
