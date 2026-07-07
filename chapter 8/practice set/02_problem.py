# using function to convert celcius to frenheit
def celsius_to_farenheit(c):
    f=(c*9/5)+32
    return f

celsius=float(input("Enter the temperature in celcius: ")) 

farenheit=celsius_to_farenheit(celsius)

print(f"Temperture in farenheit : {farenheit}")