def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def main():
    print("Welcome to the Temperature Converter!")
    print("Select conversion type:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")

    choice = input("Enter your choice (1-6): ")
    temperature = float(input("Enter the temperature value: "))

    if choice == '1':
        print(f"{temperature}°C is {celsius_to_fahrenheit(temperature)}°F")
    elif choice == '2':
        print(f"{temperature}°F is {fahrenheit_to_celsius(temperature)}°C")
    elif choice == '3':
        print(f"{temperature}°C is {celsius_to_kelvin(temperature)}K")
    elif choice == '4':
        print(f"{temperature}K is {kelvin_to_celsius(temperature)}°C")
    elif choice == '5':
        print(f"{temperature}°F is {fahrenheit_to_kelvin(temperature)}K")
    elif choice == '6':
        print(f"{temperature}K is {kelvin_to_fahrenheit(temperature)}°F")
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
- 👋 Hi, I’m @cyber824
- 👀 I’m interested in ...
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...

<!---
cyber824/cyber824 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
