print("privet trubochisti")
import random
user_action = input("Сделайте выбор - камень, ножницы, бумага")
possible_actions = ["камень", "ножницы", "бумага"]
computer_actions = random.choice((possible_actions))
if user_action == computer_actions:
    print("Оба пользователя выбрали (user_action) Ничья!")
elif user_action == "камень":
    if computer_actions == "ножницы":
        print("Камень бьет ножницы!Ты ботик выиграл!")
        else:
            ("Бумага ебет камень! Ты проиграл!")
elif user_action == "Бумага":
    if computer_actions == "камень":
        print(Бумага ебет камень! Ты выиграл!)
        else:
            (Ножницы ебут бумагу! ты проиграл!)
elif user_action == "ножницы":
    if computer_actions == "бумага":
        print(ножницы ебут бумагу! Ты выиграл!)
        else:
            (Камень ебет ножницы! Ты проиграл!)
            
