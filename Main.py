
def main():
    a = True
    b = False

    print("Operadores lógicos:")

    print(f"a ({a}) y b ({b}) es True?", a and b)  # False

    print(f"a ({a}) o b ({b}) es True?", a or b)  # True

    print(f"no a ({a}) es False?", not a)  # False
    print(f"no b ({b}) es True?", not b)  # True

    print("Combinaciones de operadores:")
    print(f"a ({a}) y (b ({b}) o no a ({a})) es True?", a and (b or not a))  # False


if __name__ == "__main__":
    main()
