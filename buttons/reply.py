from aiogram.types import KeyboardButton

from commands.admins import Commands, MenuCommands, ShowSetCommands, ShowLavashCommands

IS_ACTIVE_BUTTON = KeyboardButton(Commands.is_active.value)
MAIN_MENU_BUTTON = KeyboardButton(Commands.main_menu.value)


# МЕНЮ КНОПКИ

SHOW_SET_BUTTON = KeyboardButton(MenuCommands.show_set.value)
SHOW_LAVASH_BUTTON = KeyboardButton(MenuCommands.show_lavash.value)
SHOW_SHAWARMA_BUTTON = KeyboardButton(MenuCommands.show_shawarma.value)
SHOW_DONAR_BUTTON = KeyboardButton(MenuCommands.show_donar.value)
SHOW_BURGER_BUTTON = KeyboardButton(MenuCommands.show_burger.value)
SHOW_HOT_DOG_BUTTON = KeyboardButton(MenuCommands.show_hot_dog.value)
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