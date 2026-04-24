a= input("Enter a value: ")
choice = input("Convert to (int, float, str): ")

# mapping user choice to actual functions
conversions = {
    "int": int,
    "float": float,
    "str": str
}

try:
    result = conversions[choice](a)
    print("Converted value:", result)
    print("Type:", type(result))
except KeyError:
    print("Invalid conversion type selected!")
except ValueError:
    print("Conversion failed! Invalid input.")