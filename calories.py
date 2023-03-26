# weight = int(input("Введите свой вес "))
# calories = int(input("Введите количество калорий, которое хотите сбросить "))
#
#
# print("Доступные темы для бега: низкий, средний, высокий")
# run_temp = {"низкий": 6.0, "средний": 8.0, "высокий": 10.0}
#
#
# while True:
#     run_choice = input("Выберите тем для бега: ").lower()
#     if run_choice not in run_temp:
#         print("Неккоректный выбор темпа для бега")
#     else:
#         break
#
#
# run = calories / (run_temp[run_choice] * weight * 5) * 60
# print(f"Чтобы сбросить {calories} калорий, вам нужно бегать {run} минут с {run_choice} темпом")

#massa = int(input("Введите свою массу: "))
#kalories = int(input("Сколько хотите сбросить калорий?: "))
#print("Виды бега: низкий/высокий/средний")
#temps = {
    "низкий": 5.9,
    "средний": 8.12,
    "высокий": 9.74
}
choice = input("Введите темп бега: ")
answer = round(kalories / (temps[choice] * massa * 5) * 60,2)
if choice == "низкий":
    print(f"Вы будете бежать {answer} минуты")
elif choice == "средний":
    print(f"Вы будете бежать {answer} минуты")#elif choice == "высокий":
    print(f"Вы будете бежать {answer} минуты")


