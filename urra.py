from datetime import datetime

def get_date(prompt):
    """Запрашивает дату у пользователя и проверяет формат."""
    while True:
        user_input = input(prompt)
        try:
            return datetime.strptime(user_input, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Неверный формат. Пожалуйста, введите дату в формате ГГГГ-ММ-ДД ЧЧ:ММ.")

print("Введите дату отправления и прибытия в формате ГГГГ-ММ-ДД ЧЧ:ММ.")
departure = get_date("Отправление: ")
arrival = get_date("Прибытие: ")

if arrival < departure:
    print("Дата прибытия не может быть раньше даты отправления.")
else:
    travel_time = arrival - departure
    print(f"Время в пути: {travel_time}")

