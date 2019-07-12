import pyowm

owm = pyowm.OWM('fa82b0f3be0b1c3404402250a18fc925')
observation = owm.weather_at_place('London,uk')
w = observation.get_weather()

print (w.get_wind()['deg'])
print (w.get_humidity())
print (w.get_temperature()['temp_min'])