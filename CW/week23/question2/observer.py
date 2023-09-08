from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from random import randrange
from typing import List


class Observer(ABC):
    @abstractmethod
    def update(self, temperature, humidity):
        pass


class Station(ABC):

    @abstractmethod
    def registering(self, observer):
        pass

    @abstractmethod
    def unregistering(self, observer):
        pass

    @abstractmethod
    def notifying(self):
        pass


@dataclass
class WeatherStation(Station):

    temperature = None
    humidity = None

    _observers: List[Observer] = field(default_factory=list)

    def registering(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def unregistering(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notifying(self) -> None:

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self.temperature, self.humidity)

    def set_measurements(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity
        self.notifying()


class TemperatureDisplay(Observer):
    def update(self, temperature, humidity):
        print(f"Temperature: {temperature}")


class HumidityDisplay(Observer):
    def update(self, temperature, humidity):
        print(f"Humidity: {humidity}")


weather_station1 = WeatherStation()

temp_display = TemperatureDisplay()
hum_display = HumidityDisplay()

weather_station1.registering(temp_display)
weather_station1.registering(hum_display)

weather_station1.set_measurements(25, 60)
