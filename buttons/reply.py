from aiogram.types import KeyboardButton

from commands.admins import Commands, MenuCommands, ShowSetCommands, ShowLavashCommands, ShowShawarmaCommands, \
    ShowBurgerCommands, ShowHotDogCommands, ShowDishesCommands, ShowDesertsCommands, ShowGarnishCommands, \
    ShowDrinksCommands, MyCartCommands, AdminCommands


MAIN_MENU_BUTTON = KeyboardButton(Commands.main_menu.value)
COME_BACK_BUTTON = KeyboardButton(Commands.come_back.value)
MY_CART_BUTTON = KeyboardButton(Commands.my_cart.value)
SEND_CONTACT_BUTTON = KeyboardButton(Commands.send_contact.value, request_contact=True)
SEND_LOCATION_BUTTON = KeyboardButton(Commands.send_location.value, request_location=True)


# КНОПКИ АДМИНОВ

IS_ACTIVE_BUTTON = KeyboardButton(AdminCommands.is_active.value)
USER_ORDERS_BUTTON = KeyboardButton(AdminCommands.user_orders.value)
ORDER_HISTORY_COMPLETED_BUTTON = KeyboardButton(AdminCommands.order_history_completed.value)
ORDER_HISTORY_UNCOMPLETED_BUTTON = KeyboardButton(AdminCommands.order_history_uncompleted.value)
ORDER_COMPLETE_BUTTON = KeyboardButton(AdminCommands.order_complete.value)


# МОЯ КОРЗИНА КНОПКИ

PLACE_ORDER_BUTTON = KeyboardButton(MyCartCommands.place_order.value)
EMPTY_THE_TRASH_BUTTON = KeyboardButton(MyCartCommands.delete_cart.value)
DELIVERY_TIME_BUTTON = KeyboardButton(MyCartCommands.order_time.value)


# КНОПКА НАСТРОЕК

SETTINGS_BUTTON = KeyboardButton(Commands.settings.value)


# МЕНЮ КНОПКИ

SHOW_SET_BUTTON = KeyboardButton(MenuCommands.show_set.value)
SHOW_LAVASH_BUTTON = KeyboardButton(MenuCommands.show_lavash.value)
SHOW_SHAWARMA_BUTTON = KeyboardButton(MenuCommands.show_shawarma.value)
SHOW_DONAR_BUTTON = KeyboardButton(MenuCommands.show_donar.value)
SHOW_BURGER_BUTTON = KeyboardButton(MenuCommands.show_burger.value)
SHOW_HOT_DOG_BUTTON = KeyboardButton(MenuCommands.show_hot_dog.value)
SHOW_DISHES_BUTTON = KeyboardButton(MenuCommands.show_dishes.value)
SHOW_DESERTS_BUTTON = KeyboardButton(MenuCommands.show_deserts.value)
SHOW_DRINKS_BUTTON = KeyboardButton(MenuCommands.show_drinks.value)
SHOW_GARNISH_BUTTON = KeyboardButton(MenuCommands.show_garnish.value)


# SHOW SET КНОПКИ

FIRST_SET_CASE_BUTTON = KeyboardButton(ShowSetCommands.first_case.value)
SECOND_SET_CASE_BUTTON = KeyboardButton(ShowSetCommands.second_case.value)
THIRD_SET_CASE_BUTTON = KeyboardButton(ShowSetCommands.third_case.value)


#SHOW LAVASH КНОПКИ

FIRST_LAVASH_CASE_BUTTON = KeyboardButton(ShowLavashCommands.first_case.value)
SECOND_LAVASH_CASE_BUTTON = KeyboardButton(ShowLavashCommands.second_case.value)
THIRD_LAVASH_CASE_BUTTON = KeyboardButton(ShowLavashCommands.third_case.value)
FOURTH_LAVASH_CASE_BUTTON = KeyboardButton(ShowLavashCommands.fourth_case.value)
FIFTH_LAVASH_CASE_BUTTON = KeyboardButton(ShowLavashCommands.fifth_case.value)
SIXTH_LAVASH_CASE_BUTTON = KeyboardButton(ShowLavashCommands.sixth_case.value)
SEVENTH_LAVASH_CASE_BUTTON = KeyboardButton(ShowLavashCommands.seventh_case.value)
EIGHTH_LAVASH_CASE_BUTTON = KeyboardButton(ShowLavashCommands.eighth_case.value)
NINTH_LAVASH_CASE_BUTTON = KeyboardButton(ShowLavashCommands.ninth_case.value)
TENTH_LAVASH_CASE_BUTTON = KeyboardButton(ShowLavashCommands.tenth_case.value)
ELEVENTH_LAVASH_CASE_BUTTON = KeyboardButton(ShowLavashCommands.eleventh_case.value)


#SHOW ШАУРМА КНОПКИ

FIRST_SHAWARMA_CASE_BUTTON = KeyboardButton(ShowShawarmaCommands.first_case.value)
SECOND_SHAWARMA_CASE_BUTTON = KeyboardButton(ShowShawarmaCommands.second_case.value)
THIRD_SHAWARMA_CASE_BUTTON = KeyboardButton(ShowShawarmaCommands.third_case.value)
FOURTH_SHAWARMA_CASE_BUTTON = KeyboardButton(ShowShawarmaCommands.fourth_case.value)
FIFTH_SHAWARMA_CASE_BUTTON = KeyboardButton(ShowShawarmaCommands.fifth_case.value)
SIXTH_SHAWARMA_CASE_BUTTON = KeyboardButton(ShowShawarmaCommands.sixth_case.value)
SEVENTH_SHAWARMA_CASE_BUTTON = KeyboardButton(ShowShawarmaCommands.seventh_case.value)
EIGHTH_SHAWARMA_CASE_BUTTON = KeyboardButton(ShowShawarmaCommands.eighth_case.value)


#SHOW BURGER КНОПКИ

FIRST_BURGER_CASE_BUTTON = KeyboardButton(ShowBurgerCommands.first_case.value)
SECOND_BURGER_CASE_BUTTON = KeyboardButton(ShowBurgerCommands.second_case.value)
THIRD_BURGER_CASE_BUTTON = KeyboardButton(ShowBurgerCommands.third_case.value)
FOURTH_BURGER_CASE_BUTTON = KeyboardButton(ShowBurgerCommands.fourth_case.value)


#SHOW HOTDOG КНОПКИ

FIRST_HOT_DOG_CASE_BUTTON = KeyboardButton(ShowHotDogCommands.first_case.value)
SECOND_HOT_DOG_CASE_BUTTON = KeyboardButton(ShowHotDogCommands.second_case.value)
THIRD_HOT_DOG_CASE_BUTTON = KeyboardButton(ShowHotDogCommands.third_case.value)
FOURTH_HOT_DOG_CASE_BUTTON = KeyboardButton(ShowHotDogCommands.fourth_case.value)
FIFTH_HOT_DOG_CASE_BUTTON = KeyboardButton(ShowHotDogCommands.fifth_case.value)
SIXTH_HOT_DOG_CASE_BUTTON = KeyboardButton(ShowHotDogCommands.sixth_case.value)
SEVENTH_HOT_DOG_CASE_BUTTON = KeyboardButton(ShowHotDogCommands.seventh_case.value)
EIGHTH_HOT_DOG_CASE_BUTTON = KeyboardButton(ShowHotDogCommands.eighth_case.value)
NINTH_HOT_DOG_CASE_BUTTON = KeyboardButton(ShowHotDogCommands.ninth_case.value)
TENTH_HOT_DOG_CASE_BUTTON = KeyboardButton(ShowHotDogCommands.tenth_case.value)


#SHOW DISHES КНОПКИ

FIRST_DISHES_CASE_BUTTON = KeyboardButton(ShowDishesCommands.first_case.value)
SECOND_DISHES_CASE_BUTTON = KeyboardButton(ShowDishesCommands.second_case.value)
THIRD_DISHES_CASE_BUTTON = KeyboardButton(ShowDishesCommands.third_case.value)
FOURTH_DISHES_CASE_BUTTON = KeyboardButton(ShowDishesCommands.fourth_case.value)
FIFTH_DISHES_CASE_BUTTON = KeyboardButton(ShowDishesCommands.fifth_case.value)
SIXTH_DISHES_CASE_BUTTON = KeyboardButton(ShowDishesCommands.sixth_case.value)
SEVENTH_DISHES_CASE_BUTTON = KeyboardButton(ShowDishesCommands.seventh_case.value)


#SHOW DESERTS КНОПКИ

FIRST_DESERTS_CASE_BUTTON = KeyboardButton(ShowDesertsCommands.first_case.value)
SECOND_DESERTS_CASE_BUTTON = KeyboardButton(ShowDesertsCommands.second_case.value)
THIRD_DESERTS_CASE_BUTTON = KeyboardButton(ShowDesertsCommands.third_case.value)
FOURTH_DESERTS_CASE_BUTTON = KeyboardButton(ShowDesertsCommands.fourth_case.value)


#SHOW GARNISH КНОПКИ

FIRST_GARNISH_CASE_BUTTON = KeyboardButton(ShowGarnishCommands.first_case.value)
SECOND_GARNISH_CASE_BUTTON = KeyboardButton(ShowGarnishCommands.second_case.value)
THIRD_GARNISH_CASE_BUTTON = KeyboardButton(ShowGarnishCommands.third_case.value)
FOURTH_GARNISH_CASE_BUTTON = KeyboardButton(ShowGarnishCommands.fourth_case.value)
FIFTH_GARNISH_CASE_BUTTON = KeyboardButton(ShowGarnishCommands.fifth_case.value)
SIXTH_GARNISH_CASE_BUTTON = KeyboardButton(ShowGarnishCommands.sixth_case.value)
SEVENTH_GARNISH_CASE_BUTTON = KeyboardButton(ShowGarnishCommands.seventh_case.value)
EIGHTH_GARNISH_CASE_BUTTON = KeyboardButton(ShowGarnishCommands.eighth_case.value)


#SHOW DRINKS КНОПКИ

FIRST_DRINKS_BUTTON = KeyboardButton(ShowDrinksCommands.first_case.value)
SECOND_DRINKS_BUTTON = KeyboardButton(ShowDrinksCommands.second_case.value)
THIRD_DRINKS_BUTTON = KeyboardButton(ShowDrinksCommands.third_case.value)
FOURTH_DRINKS_BUTTON = KeyboardButton(ShowDrinksCommands.fourth_case.value)
FIFTH_DRINKS_BUTTON = KeyboardButton(ShowDrinksCommands.fifth_case.value)
SIXTH_DRINKS_BUTTON = KeyboardButton(ShowDrinksCommands.sixth_case.value)
SEVENTH_DRINKS_BUTTON = KeyboardButton(ShowDrinksCommands.seventh_case.value)
EIGHTH_DRINKS_BUTTON = KeyboardButton(ShowDrinksCommands.eighth_case.value)
NINTH_DRINKS_BUTTON = KeyboardButton(ShowDrinksCommands.ninth_case.value)
TENTH_DRINKS_BUTTON = KeyboardButton(ShowDrinksCommands.tenth_case.value)
ELEVENTH_DRINKS_BUTTON = KeyboardButton(ShowDrinksCommands.eleventh_case.value)