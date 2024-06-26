# ---------------------------- CONSTANTS ------------------------------- #

LOGO = """
 __  __             _                                        
|  \/  | ___  _ __ | |_ __ _  ___  _ __ ___   ___ _ __ _   _ 
| |\/| |/ _ \| '_ \| __/ _` |/ _ \| '_ ` _ \ / _ \ '__| | | |
| |  | | (_) | | | | || (_| | (_) | | | | | |  __/ |  | |_| |
|_|  |_|\___/|_|_|_|\__\__, |\___/|_| |_| |_|\___|_|   \__, |
| |    __ _  __| | __| |___/ _ __                      |___/ 
| |   / _` |/ _` |/ _` |/ _ \ '__|                           
| |__| (_| | (_| | (_| |  __/ |                              
|_____\__,_|\__,_|\__,_|\___|_|                              
"""


# ---------------------------- Functions ------------------------------- #

def print_logo():
    """
    Print the logo of the program to the console.
    :return: None
    """

    print()
    print(LOGO)
    print()


def validate_user_input(prompt: str) -> int:
    """
    Validate the user input.
    :param str prompt: The prompt message to display to the user.
    :return: The validated integer input from the user.
    """

    while True:
        user_input = input(prompt)

        try:
            value = int(user_input)

            if value <= 0:
                raise ValueError("Invalid Input: Please enter a positive number.")
            break

        except ValueError:
            print("Invalid Input: Please enter a positiv number.")

    return value


def montgomery_ladder(base: int, exponent: int, modulo: int) -> int:
    """
    Perform the Montgomery Ladder algorithm.
    :param int base: The base number for the calculation.
    :param int exponent: The exponent for the calculation.
    :param int modulo: The modulo for the calculation.
    :return: The result of the Montgomery Ladder calculation.
    """

    x = 1
    y = base % modulo
    exponent_in_bit = bin(exponent)[2:]

    for bit in exponent_in_bit:
        if bit == "1":
            x = (x * y) % modulo
            y = (y ** 2) % modulo
        else:
            y = (x * y) % modulo
            x = (x ** 2) % modulo

    return x


def main():
    """
    Main function of the program.
    :return: None
    """

    print_logo()

    # Variables
    base = validate_user_input("Base: ")
    exponent = validate_user_input("Exponent: ")
    modulo = validate_user_input("Modulo: ")

    # Body
    print(10 * "-")
    print(f"Result: {montgomery_ladder(base, exponent, modulo)}")


# ------------------------------ Main ---------------------------------- #

if __name__ == "__main__":
    main()
