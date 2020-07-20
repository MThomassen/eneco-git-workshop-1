from lib import logic


def add(a, b):
    """Adds numbers a and b"""
    pass


def main():
    name = logic.name_from_cli()
    print(f"Hello, {name}")

    result = add(1, 2)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()