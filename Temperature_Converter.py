#function to convert temperature
def convert_temp(temperature, from_unit, to_unit):
    if from_unit == "C" and to_unit == "F":
        converted_temperature = temperature *9/5 + 32
        return converted_temperature
    elif from_unit == "F" and to_unit == "C":
        converted_temperature = (temperature- 32) * 5/9
        return converted_temperature
    else:
      
      print("Invalid conversion units.")
      return None
    
  
celsius_temperature = 25
fahrenheit_temperature = convert_temp(celsius_temperature, "C", "F")
print(f"{celsius_temperature} degrees Celsius is equal to {fahrenheit_temperature} degrees Fahrenheit.")



fahrenheit_temperaturee = 200
celsius_temperature = convert_temp(celsius_temperature, "F", "C")
print(f"{fahrenheit_temperature} degrees Celsius is equal to {celsius_temperature} degrees Fahrenheit.")
