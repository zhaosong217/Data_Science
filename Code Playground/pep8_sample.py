"""这个脚本展示了一些PEP 8的规则
"""
import datetime as dt
TEMPERATURE_SCALES = ("fahrenheit", "kelvin",
"celsius")

class TemperatureConverter:
    pass  # 暂时不做任何事


def convert_to_celsius(degrees, source="fahrenheit"):
    """这个函数将华氏度或开氏度转化为摄氏度
    """
    if source.lower() == "fahrenheit":
        return (degrees-32) * (5/9)
    elif source.lower() == "kelvin":
        return degrees - 273.15
    else:
        return f"Don't know how to convert from {source}"
  
  
celsius = convert_to_celsius(44, source="fahrenheit")
non_celsius_scales = TEMPERATURE_SCALES[:-1]

print("Current time: " + dt.datetime.now().isoformat())
print(f"The temperature in Celsius is: {celsius}")