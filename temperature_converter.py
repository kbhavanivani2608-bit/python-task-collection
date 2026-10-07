print("===== Temperature Converter =====")

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")

choice = int(input("Enter your choice (1-6): "))
temperature = float(input("Enter temperature: "))

if choice == 1:
    result = (temperature * 9 / 5) + 32
    print(f"{temperature}°C = {result:.2f}°F")

elif choice == 2:
    result = (temperature - 32) * 5 / 9
    print(f"{temperature}°F = {result:.2f}°C")

elif choice == 3:
    result = temperature + 273.15
    print(f"{temperature}°C = {result:.2f} K")

elif choice == 4:
    result = temperature - 273.15
    print(f"{temperature} K = {result:.2f}°C")

elif choice == 5:
    result = (temperature - 32) * 5 / 9 + 273.15
    print(f"{temperature}°F = {result:.2f} K")

elif choice == 6:
    result = (temperature - 273.15) * 9 / 5 + 32
    print(f"{temperature} K = {result:.2f}°F")

else:
    print("Invalid choice!")