from main import get_weather_information

def get_information():
    temperatura, descripcion = get_weather_information('Barcelona')
    assert temperatura is not None
    assert descripcion is not None