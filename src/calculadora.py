"""Example module with functions to demonstrate testing."""


def soma(a: int, b: int) -> int:
    """
    Return the sum of two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        The sum of a and b

    Examples:
        >>> soma(2, 3)
        5
    """
    return a + b


def multiplicacao(a: int, b: int) -> int:
    """
    Return the multiplication of two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        The product of a and b
    """
    return a * b


def saudacao(nome: str) -> str:
    """
    Return a personalized greeting.

    Args:
        nome: Person's name

    Returns:
        Greeting message
    """
    return f"Olá, {nome}!"
