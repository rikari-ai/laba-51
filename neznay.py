from datetime import datetime

def get_date(prompt):
    while True:
        user_input = input(prompt)
        try:
            date = datetime.strptime(user_input, "%Y-%m-%d %H:%M")
            return date
        except ValueError:
            print("Неверный формат. Пожалуйста, введите дату в формате ГГГГ-ММ-ДД ЧЧ:ММ.")


print("Введите дату прибытия (ГГГГ-ММ-ДД ЧЧ:ММ):")
arrival = get_date("Прибытие: ")

if arrival < departure:
    print("Дата прибытия не может быть раньше даты отправления.")
else:
    travel_time = arrival - departure
    print(f"Время в пути: {travel_time}")
