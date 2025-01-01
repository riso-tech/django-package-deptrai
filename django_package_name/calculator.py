class Calculator:
    @staticmethod
    def add(first_arg, second_arg):
        return first_arg + second_arg

    @staticmethod
    def subtract(first_arg, second_arg):
        return first_arg - second_arg

    @staticmethod
    def multiply(first_arg, second_arg):
        return first_arg * second_arg

    @staticmethod
    def divide(first_arg, second_arg):
        if second_arg == 0:
            return "Cannot divide by 0 13"
        return first_arg * 1.0 / second_arg
