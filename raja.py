def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    print("Welcome to the Temperature Conversion Calculator!\n")
    print("Select the conversion you want to perform:")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")
    
    choice = int(input("\nEnter your choice (1-6): "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C is equal to {celsius_to_fahrenheit(celsius):.2f}°F")
    elif choice == 2:
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C is equal to {celsius_to_kelvin(celsius):.2f}K")
    elif choice == 3:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F is equal to {fahrenheit_to_celsius(fahrenheit):.2f}°C")
    elif choice == 4:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F is equal to {fahrenheit_to_kelvin(fahrenheit):.2f}K")
    elif choice == 5:
        kelvin = float(input("Enter temperature in Kelvin: "))
        print(f"{kelvin}K is equal to {kelvin_to_celsius(kelvin):.2f}°C")
    elif choice == 6:
        kelvin = float(input("Enter temperature in Kelvin: "))
        print(f"{kelvin}K is equal to {kelvin_to_fahrenheit(kelvin):.2f}°F")
    else:
        print("Invalid choice. Please select a number between 1 and 6.")

if __name__ == "__main__":
    main()
