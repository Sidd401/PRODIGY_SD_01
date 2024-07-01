def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    return kelvin

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return fahrenheit

def main():
    print("Temperature Conversion Program")
    print("-------------------------------")
    print("Available units:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    print()

    try:
        temperature = float(input("Enter the temperature value: "))
        original_unit = int(input("Enter the original unit of temperature (1/2/3): "))

        if original_unit == 1:  # Celsius
            celsius = temperature
            fahrenheit = celsius_to_fahrenheit(celsius)
            kelvin = celsius_to_kelvin(celsius)

            print(f"{celsius} degrees Celsius is equal to:")
            print(f"{fahrenheit} degrees Fahrenheit")
            print(f"{kelvin} Kelvin")

        elif original_unit == 2:  # Fahrenheit
            fahrenheit = temperature
            celsius = fahrenheit_to_celsius(fahrenheit)
            kelvin = fahrenheit_to_kelvin(fahrenheit)

            print(f"{fahrenheit} degrees Fahrenheit is equal to:")
            print(f"{celsius} degrees Celsius")
            print(f"{kelvin} Kelvin")

        elif original_unit == 3:  # Kelvin
            kelvin = temperature
            celsius = kelvin_to_celsius(kelvin)
            fahrenheit = kelvin_to_fahrenheit(kelvin)

            print(f"{kelvin} Kelvin is equal to:")
            print(f"{celsius} degrees Celsius")
            print(f"{fahrenheit} degrees Fahrenheit")

        else:
            print("Invalid input. Please enter 1, 2, or 3.")

    except ValueError:
        print("Invalid input. Please enter a numeric temperature value.")

if __name__ == "__main__":
    main()
