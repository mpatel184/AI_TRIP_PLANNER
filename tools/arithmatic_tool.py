import os
from dotenv import load_dotenv
from langchain.tools import tool
from langchain_community.utilities.alpha_vantage import AlphaVantageAPIWrapper

load_dotenv()

@tool
def multiply(a: int, b: int) -> int:
    """
    Multiply two numbers.
    Args:
        a (int): First number.
        b (int): Second number.
    Returns:
        int: The product of a and b.    
    """
    return a * b

@tool
def add(a: int, b: int) -> int:
    """
    Add two numbers.
    Args:
        a (int): First number.
        b (int): Second number.
    Returns:
        int: The sum of a and b.
    """
    return a + b 
