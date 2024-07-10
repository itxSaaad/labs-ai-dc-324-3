def celsius_to_fahrenheit(C):
    return (C * 9/5) + 32

def fahrenheit_to_celsius(F):
    return (F - 32) * 5/9

def main():
    celsius = 60
    fahrenheit = 45
    print(f'{celsius}°C is {celsius_to_fahrenheit(celsius)} in Fahrenheit')
    print(f'{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit)} in Celsius')

main()
