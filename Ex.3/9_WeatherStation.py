class WeatherStation:
    def __init__(self, name_of_station):
        self.name_of_station = name_of_station
        self.observations = []
    
    def add_observation(self, observation: str):
        self.observations.append(observation)

    def latest_observation(self):
        if not self.observations:
            return "empty"
        else:
            return self.observations[-1]

    def number_of_observations(self):
        return len(self.observations)

    def __str__(self):
        return f"{self.name_of_station}, {self.number_of_observations()} observations"

station = WeatherStation("Houston")
station.add_observation("Rain 10mm")
station.add_observation("Sunny")
print(station.latest_observation())

station.add_observation("Thunderstorm")
print(station.latest_observation())
print(station.number_of_observations())
print(station)