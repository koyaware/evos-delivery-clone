from enum import Enum


class Commands(Enum):
    is_active = "Посмотреть всех пользователей 👥"
    main_menu = "Меню 📇"
    come_back = "Вернуться в главное меню 📇"


class MenuCommands(Enum):
    show_set = "Сет"
    show_lavash = "Лаваш"
    show_shawarma = "Шаурма"
    show_donar = "Донар"
    show_burger = "Бургер"
    show_hot_dog = "Хот-Дог"
    show_deserts = "Десерты"
    show_drinks = "Напитки"
    show_garnish = "Гарнир"


class ShowSetCommands(Enum):
    first_case = "Комбо плюс Pepsi"
    second_case = "Детское комбо"
    third_case = "ФитCOMBO"


class ShowLavashCommands(Enum):
    first_case = "Лаваш с говядиной"
    second_case = "Лаваш с курицей"
    third_case = "Лаваш с говядиной Мини"
    fourth_case = "Лаваш с курицей Мини"
    fifth_case = "Лаваш с говядиной и сыром"
    sixth_case = "Лаваш с курицей и сыром"
    seventh_case = "Лаваш с говядиной и сыром Мини"
    eighth_case = "Лаваш с курицей и сыром Мини"
    ninth_case = "Лаваш острый с говядиной"
    tenth_case = "Лаваш острый с курицей"
    eleventh_case = "Фиттер"