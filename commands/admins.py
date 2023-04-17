from enum import Enum


class Commands(Enum):
    main_menu = "Меню 📇"
    come_back = "Вернуться в главное меню 📇"
    my_cart = "Корзина 🗑️"
    send_contact = "Отправить контакт ☎"
    send_location = "Отправить геолоакцию 📍"
    settings = "Настройки ⚙"


class AdminCommands(Enum):
    is_active = "Посмотреть всех пользователей 👥"
    user_orders = "Заказы пользователей 📦"
    order_history_completed = "Выполненные заказы ✔"
    order_history_uncompleted = "Не выполненные заказы ❌"
    order_complete = "Закрыть заказ ❌"


class MyCartCommands(Enum):
    delete_cart = "Очистить корзину 🗑️"
    place_order = "Оформить заказ 📦"
    order_time = "Время доставки ⏳"


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
    show_dishes = "Блюда"


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


class ShowShawarmaCommands(Enum):
    first_case = "Шаурма с говядиной Мини"
    second_case = "Шаурма с говядиной"
    third_case = "Шаурма с курицей Мини"
    fourth_case = "Шаурма с курицей"
    fifth_case = "Шаурма острая с говядиной Мини"
    sixth_case = "Шаурма острая с курицей Мини"
    seventh_case = "Шаурма острая с курицей"
    eighth_case = "Шаурма острая с говядиной"


class ShowBurgerCommands(Enum):
    first_case = "Гамбургер"
    second_case = "Даблбургер"
    third_case = "Даблчизбургер"
    fourth_case = "Чизбургер"


class ShowHotDogCommands(Enum):
    first_case = "Хот-дог"
    second_case = "Даблхот-дог"
    third_case = "Хот-дог Мини"
    fourth_case = "Картофель Фри"
    fifth_case = "Картофель по-деревенски"
    sixth_case = "Хот-дог детский"
    seventh_case = "Саб с курицей"
    eighth_case = "Саб с говядиной"
    ninth_case = "Саб с курицей и сыром"
    tenth_case = "Саб с говядиной и сыром"


class ShowDishesCommands(Enum):
    first_case = "Донар с говядиной"
    second_case = "Донар с курицей"
    third_case = "Стрипсы"
    fourth_case = "Ифтар кофте с говядиной"
    fifth_case = "Ифтар стрипс с курицей"
    sixth_case = "Донар-бокс с говядиной"
    seventh_case = "Донар-бокс с курицей"


class ShowDesertsCommands(Enum):
    first_case = "Медовик"
    second_case = "Чизкейк"
    third_case = "Донат Ягодный микс"
    fourth_case = "Донат Карамельный"


class ShowGarnishCommands(Enum):
    first_case = "Кетчуп"
    second_case = "Майонез"
    third_case = "Чесночный соус"
    fourth_case = "Сырный соус"
    fifth_case = "Чили соус"
    sixth_case = "Рис"
    seventh_case = "Салат"
    eighth_case = "Лепешка"


class ShowDrinksCommands(Enum):
    first_case = "Сок Блисс, 1 литр"
    second_case = "Сок Дена без сахара, 0,33"
    third_case = "Вода без газа 0,5л"
    fourth_case = "Пепси, 1,5л"
    fifth_case = "Пепси, разлив 0,4л"
    sixth_case = "Пепси, 0,5л"
    seventh_case = "Чай черный"
    eighth_case = "Капучино"
    ninth_case = "Американо"
    tenth_case = "Латте"
    eleventh_case = "Стакан 200мл"