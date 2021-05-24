"""Вариант 3. Создать класс Airline: Пункт назначения, Номер рейса, Тип самолета, Время вылета, Дни недели. Функции- члены реализуют запись и считывание полей (проверка корректности).
Создать список объектов. Вывести:
a)	список рейсов для заданного пункта назначения;
b)	список рейсов для заданного дня недели"""

class Airline:
    __destination = " "
    __flight_number = 0
    __plane_type = " "
    __departure_time = " "
    __days_of_the_week = " "

    def __init__(self, destination, flight_number, plane_type, departure_time, days_of_the_week):
        self.__destination = destination
        self.__flight_number = flight_number
        self.__plane_type = plane_type
        self.__departure_time = departure_time
        self.__days_of_the_week = days_of_the_week


    def get_destination(self):
        return self.__destination

    def get_flight_number(self):
        return self.__flight_number

    def get_plane_type(self):
        return self.__plane_type

    def get_departure_time(self):
        return self.__departure_time

    def get_days_of_the_week(self):
        return self.__days_of_the_week

    def list_destination(self):
        pass

    def flight_by_days(self):
        pass

    def __str__(self):
        return str(self.__destination) + " " + str(self.__flight_number) + " " + str(self.__plane_type) + " " + str(self.__departure_time) + " " + str(self.__days_of_the_week)

list_fly = [
    Airline("Minsk", 17001, "Airbus", "04:50", "Sunday"),
    Airline("Helsinki", 21018, "Boing", "18:10", "Monday"),
    Airline("Varna", 87544, "Icarus", "12:30", "Tuesday"),
    Airline("Istanbul", 65423, "Zlin", "14:40", "Wednesday"),
    Airline("Moscow",33355, "SuperJet", "08:50", "Thursday"),
    Airline("Kyiv", 12345, "Shuttle", "11:00", "Friday"),
    Airline("Beirut", 14789, "Il", "8:45", "Saturday"),
    Airline("Rome", 19501, "Airbus", "09:50", "Sunday"),
    Airline("New York", 29918, "Boing", "08:10", "Monday"),
    Airline("Baku", 99544, "Boing", "19:30", "Tuesday"),
    Airline("Moscow", 22413, "Boing", "17:40", "Wednesday"),
    Airline("Rome",42128, "SuperJet", "02:50", "Thursday"),
    Airline("Minsk", 78976, "Shuttle", "11:00", "Friday"),
    Airline("Moscow", 35799, "Shuttle", "8:45", "Saturday"),
    Airline("Beirut", 17001, "Airbus", "04:50", "Sunday"),
    Airline("Ulan-Ude", 94018, "Shuttle", "18:10", "Monday"),
    Airline("Minsk", 88524, "Airbus", "12:30", "Tuesday"),
    Airline("Istanbul", 63323, "Airbus", "14:40", "Wednesday"),
    Airline("Beirut",30325, "Shuttle", "01:50", "Thursday"),
    Airline("Helsinki", 15745, "Airbus", "18:00", "Friday"),
    Airline("Surgut", 44799, "Il", "18:45", "Saturday")]

dest = input("Enter destination, please: ")
print("  "*15)

for plane in list_fly:
    if plane.get_destination() == dest:
        print(plane)
        print("  "*15)

days = input("Enter days of the week what do you prefer: ")
print("  "*15)

for plane in list_fly:
    if plane.get_days_of_the_week() == days:
        print("  "*15)
        print(plane)