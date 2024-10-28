from datetime import datetime


def get_date(prompt):
    while True:
        user_input = input(prompt)
        try:
            return datetime.strptime(user_input, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Неверный формат. Пожалуйста, введите дату в формате ГГГГ-ММ-ДД ЧЧ:ММ.")


def calculate_travel_time(departure, arrival):
    if arrival < departure:
        print("Дата прибытия не может быть раньше даты отправления.")
    else:
        travel_time = arrival - departure
        print(f"Время в пути: {travel_time}")


print("Введите даты отправления и прибытия в формате ГГГГ-ММ-ДД ЧЧ:ММ.")
departure = get_date("Отправление: ")
arrival = get_date("Прибытие: ")
calculate_travel_time(departure, arrival)
