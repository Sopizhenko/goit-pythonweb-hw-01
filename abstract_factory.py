from abc import abstractmethod, ABC
import logging

logging.basicConfig(level=logging.INFO)


class Vehicle:
    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def __init__(self, make: str, model: str, region_spec: str):
        self.make = make
        self.model = model
        self.region_spec = region_spec

    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} ({self.region_spec}): Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, region_spec: str):
        self.make = make
        self.model = model
        self.region_spec = region_spec

    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} ({self.region_spec}): Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make, model) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "US Spec")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "EU Spec")


if __name__ == "__main__":
    # Використання
    factory_us = USVehicleFactory()
    car_us = factory_us.create_car("Toyota", "Corolla")
    car_us.start_engine()

    bike_us = factory_us.create_motorcycle("Harley-Davidson", "Sportster")
    bike_us.start_engine()

    factory_eu = EUVehicleFactory()
    car_eu = factory_eu.create_car("Toyota", "Corolla")
    car_eu.start_engine()

    bike_eu = factory_eu.create_motorcycle("Harley-Davidson", "Sportster")
    bike_eu.start_engine()
