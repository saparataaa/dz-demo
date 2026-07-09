category = input("Введите категорию блюда (напиток / суп / десерт): ").lower()
if category == "напиток":
    print("Доступные напитки: чай, кофе, сок")
    dish = input("Выберите напиток: ").lower()

    match dish:
        case "чай":
            print(200)
        case "кофе":
            print(300)
        case "сок":
            print(250)
        case _:
            print("Такого напитка нет")

elif category == "суп":
    print("Доступные супы: борщ, щи, суп-пюре")
    dish = input("Выберите суп: ").lower()

    match dish:
        case "борщ":
            print(500)
        case "щи":
            print(350)
        case "суп-пюре":
            print(400)
        case _:
            print("Такого супа нет")

elif category == "десерт":
    print("Доступные десерты: торт, мороженое, фрукты")
    dish = input("Выберите десерт: ").lower()

    match dish:
        case "торт":
            print(600)
        case "мороженое":
            print(300)
        case "фрукты":
            print(200)
        case _:
            print("Такого десерта нет")
else:
    print("Неизвестная категория")
