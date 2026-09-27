from datetime import datetime

print("Програма для обчислення різниці між двома датами")

date1 = input("Введіть першу дату (дд.мм.рррр): ")
date2 = input("Введіть другу дату (дд.мм.рррр): ")

try:
    first_date = datetime.strptime(date1, "%d.%m.%Y")
    second_date = datetime.strptime(date2, "%d.%m.%Y")

    difference = abs(second_date - first_date)

    print("Перша дата:", first_date.strftime("%d.%m.%Y"))
    print("Друга дата:", second_date.strftime("%d.%m.%Y"))
    print("Різниця між датами:", difference.days, "днів")

except ValueError:
    print("Помилка! Введіть дату у форматі дд.мм.рррр.")