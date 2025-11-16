"""Exemplo de módulo com funções para demonstrar testes."""


def soma(a: int, b: int) -> int:
    """
    Retorna a soma de dois números.

    Args:
        a: Primeiro número
        b: Segundo número

    Returns:
        A soma de a e b

    Examples:
        >>> soma(2, 3)
        5
    """
    return a + b


def multiplicacao(a: int, b: int) -> int:
    """
    Retorna a multiplicação de dois números.

    Args:
        a: Primeiro número
        b: Segundo número

    Returns:
        O produto de a e b
    """
    return a * b


def saudacao(nome: str) -> str:
    """
    Retorna uma saudação personalizada.

    Args:
        nome: Nome da pessoa

    Returns:
        Mensagem de saudação
    """
    return f"Olá, {nome}!"
