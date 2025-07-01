class Calculator:
    @staticmethod
    def multiply(a: int, b: int) -> int:
        """Multiplies two numbers."""
        return a * b

    @staticmethod
    def calculate_total(*a: float) -> float:
        """Adds two or more numbers."""
        return sum(a)

    @staticmethod
    def calculate_daily_expense(total: float, day: int) -> float:
        """Calculates the total daily expense."""
        return total / day if day > 0 else 0