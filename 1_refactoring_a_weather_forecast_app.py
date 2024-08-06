'''
1. Refactoring a Weather Forecast Application into Classes and Modules

Task 1: Identifying and Creating Classes - Analyze the provided script and identify distinct functionalities that can be encapsulated into classes. Create classes that represent different aspects of the weather forecast application, such as fetching data (WeatherDataFetcher), parsing data (DataParser), and user interaction (UserInterface).

'''

class WeatherDataFetcher:
    def __init__(self, city):
        self.city = city
    
    def fetch_weather_data(self, city):
        print(f"Fetching weather data for {city}...")
        weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }
        return weather_data.get(city, {})
    
class DataParser:
    def __init__(self, data):
        self.data = data
    
    def parse_weather_data(self, data):
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["condition"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"
    
    def get_detailed_forecast(self, city):
        data = WeatherDataFetcher.fetch_weather_data(city)
        return WeatherDataFetcher.fetch_weather_data(data)
    
    def display_weather(self, city):
        data = WeatherDataFetcher.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report = DataParser.parse_weather_data(data)
            print(weather_report)


def main():
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        if detailed == 'yes':
            forecast = DataParser.get_detailed_forecast(city)
        else:
            forecast = DataParser.display_weather(city)
        print(forecast)

if __name__ == "__main__":
    main()