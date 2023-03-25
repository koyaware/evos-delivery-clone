from aiogram.types import ReplyKeyboardMarkup

from buttons.reply import IS_ACTIVE_BUTTON, MAIN_MENU_BUTTON, SHOW_SET_BUTTON, SHOW_LAVASH_BUTTON, SHOW_SHAWARMA_BUTTON, \
    SHOW_DONAR_BUTTON, SHOW_BURGER_BUTTON, SHOW_HOT_DOG_BUTTON, SHOW_DESERTS_BUTTON, SHOW_DRINKS_BUTTON, \
    SHOW_GARNISH_BUTTON, THIRD_SET_CASE_BUTTON, FIRST_SET_CASE_BUTTON, SECOND_SET_CASE_BUTTON, FIRST_LAVASH_CASE_BUTTON, \
    SECOND_LAVASH_CASE_BUTTON, THIRD_LAVASH_CASE_BUTTON, FOURTH_LAVASH_CASE_BUTTON, FIFTH_LAVASH_CASE_BUTTON, \
    SIXTH_LAVASH_CASE_BUTTON, SEVENTH_LAVASH_CASE_BUTTON, EIGHTH_LAVASH_CASE_BUTTON, NINTH_LAVASH_CASE_BUTTON, \
    TENTH_LAVASH_CASE_BUTTON, ELEVENTH_LAVASH_CASE_BUTTON, COME_BACK_BUTTON, FIRST_SHAWARMA_CASE_BUTTON, \
    SECOND_SHAWARMA_CASE_BUTTON, THIRD_SHAWARMA_CASE_BUTTON, FOURTH_SHAWARMA_CASE_BUTTON, FIFTH_SHAWARMA_CASE_BUTTON, \
    SIXTH_SHAWARMA_CASE_BUTTON, SEVENTH_SHAWARMA_CASE_BUTTON, EIGHTH_SHAWARMA_CASE_BUTTON, FIRST_BURGER_CASE_BUTTON, \
    SECOND_BURGER_CASE_BUTTON, THIRD_BURGER_CASE_BUTTON, FOURTH_BURGER_CASE_BUTTON, FIRST_HOT_DOG_CASE_BUTTON, \
    SECOND_HOT_DOG_CASE_BUTTON, THIRD_HOT_DOG_CASE_BUTTON, FOURTH_HOT_DOG_CASE_BUTTON, FIFTH_HOT_DOG_CASE_BUTTON, \
    SIXTH_HOT_DOG_CASE_BUTTON, SEVENTH_HOT_DOG_CASE_BUTTON, EIGHTH_HOT_DOG_CASE_BUTTON, NINTH_HOT_DOG_CASE_BUTTON, \
    TENTH_HOT_DOG_CASE_BUTTON, SHOW_DISHES_BUTTON, FIRST_DISHES_CASE_BUTTON, SECOND_DISHES_CASE_BUTTON, \
    THIRD_DISHES_CASE_BUTTON, FOURTH_DISHES_CASE_BUTTON, FIFTH_DISHES_CASE_BUTTON, SIXTH_DISHES_CASE_BUTTON, \
    SEVENTH_DISHES_CASE_BUTTON, FIRST_DESERTS_CASE_BUTTON, SECOND_DESERTS_CASE_BUTTON, THIRD_DESERTS_CASE_BUTTON, \
    FOURTH_DESERTS_CASE_BUTTON, FIRST_GARNISH_CASE_BUTTON, SECOND_GARNISH_CASE_BUTTON, THIRD_GARNISH_CASE_BUTTON, \
    FOURTH_GARNISH_CASE_BUTTON, FIFTH_GARNISH_CASE_BUTTON, SIXTH_GARNISH_CASE_BUTTON, SEVENTH_GARNISH_CASE_BUTTON, \
    EIGHTH_GARNISH_CASE_BUTTON, FIRST_DRINKS_BUTTON, SECOND_DRINKS_BUTTON, THIRD_DRINKS_BUTTON, FOURTH_DRINKS_BUTTON, \
    FIFTH_DRINKS_BUTTON, SIXTH_DRINKS_BUTTON, SEVENTH_DRINKS_BUTTON, EIGHTH_DRINKS_BUTTON, NINTH_DRINKS_BUTTON, \
    TENTH_DRINKS_BUTTON, ELEVENTH_DRINKS_BUTTON, MY_CART_BUTTON

ADMIN_KEYBOARDS = ReplyKeyboardMarkup([
    [IS_ACTIVE_BUTTON],
    [MAIN_MENU_BUTTON],
    [MY_CART_BUTTON]
], resize_keyboard=True)


USER_KEYBOARDS = ReplyKeyboardMarkup([
    [MAIN_MENU_BUTTON],
    [MY_CART_BUTTON]
], resize_keyboard=True)


MENU_KEYBOARDS = ReplyKeyboardMarkup([
    [SHOW_SET_BUTTON, SHOW_LAVASH_BUTTON],
    [SHOW_SHAWARMA_BUTTON, SHOW_DONAR_BUTTON],
    [SHOW_BURGER_BUTTON, SHOW_HOT_DOG_BUTTON],
    [SHOW_DISHES_BUTTON, SHOW_DESERTS_BUTTON],
    [SHOW_GARNISH_BUTTON, SHOW_DRINKS_BUTTON],
    [COME_BACK_BUTTON, MY_CART_BUTTON]
])


SHOW_SET_KEYBOARDS = ReplyKeyboardMarkup([
    [FIRST_SET_CASE_BUTTON, SECOND_SET_CASE_BUTTON],
    [THIRD_SET_CASE_BUTTON],
    [COME_BACK_BUTTON, MY_CART_BUTTON]
], resize_keyboard=True)


SHOW_LAVASH_KEYBOARDS = ReplyKeyboardMarkup([
    [FIRST_LAVASH_CASE_BUTTON, SECOND_LAVASH_CASE_BUTTON],
    [THIRD_LAVASH_CASE_BUTTON, FOURTH_LAVASH_CASE_BUTTON],
    [FIFTH_LAVASH_CASE_BUTTON, SIXTH_LAVASH_CASE_BUTTON],
    [SEVENTH_LAVASH_CASE_BUTTON, EIGHTH_LAVASH_CASE_BUTTON],
    [NINTH_LAVASH_CASE_BUTTON, TENTH_LAVASH_CASE_BUTTON],
    [ELEVENTH_LAVASH_CASE_BUTTON],
    [COME_BACK_BUTTON, MY_CART_BUTTON]
], resize_keyboard=True)


SHOW_SHAWARMA_KEYBOARDS = ReplyKeyboardMarkup([
    [FIRST_SHAWARMA_CASE_BUTTON, SECOND_SHAWARMA_CASE_BUTTON],
    [THIRD_SHAWARMA_CASE_BUTTON, FOURTH_SHAWARMA_CASE_BUTTON],
    [FIFTH_SHAWARMA_CASE_BUTTON, SIXTH_SHAWARMA_CASE_BUTTON],
    [SEVENTH_SHAWARMA_CASE_BUTTON, EIGHTH_SHAWARMA_CASE_BUTTON],
    [COME_BACK_BUTTON, MY_CART_BUTTON]
], resize_keyboard=True)


SHOW_BURGER_KEYBOARDS = ReplyKeyboardMarkup([
    [FIRST_BURGER_CASE_BUTTON, SECOND_BURGER_CASE_BUTTON],
    [THIRD_BURGER_CASE_BUTTON, FOURTH_BURGER_CASE_BUTTON],
    [COME_BACK_BUTTON, MY_CART_BUTTON]
], resize_keyboard=True)


SHOW_HOT_DOG_KEYBOARDS = ReplyKeyboardMarkup([
    [FIRST_HOT_DOG_CASE_BUTTON, SECOND_HOT_DOG_CASE_BUTTON],
    [THIRD_HOT_DOG_CASE_BUTTON, FOURTH_HOT_DOG_CASE_BUTTON],
    [FIFTH_HOT_DOG_CASE_BUTTON, SIXTH_HOT_DOG_CASE_BUTTON],
    [SEVENTH_HOT_DOG_CASE_BUTTON, EIGHTH_HOT_DOG_CASE_BUTTON],
    [NINTH_HOT_DOG_CASE_BUTTON, TENTH_HOT_DOG_CASE_BUTTON],
    [COME_BACK_BUTTON, MY_CART_BUTTON]
], resize_keyboard=True)


SHOW_DISHES_KEYBOARDS = ReplyKeyboardMarkup([
    [FIRST_DISHES_CASE_BUTTON, SECOND_DISHES_CASE_BUTTON],
    [THIRD_DISHES_CASE_BUTTON, FOURTH_DISHES_CASE_BUTTON],
    [FIFTH_DISHES_CASE_BUTTON, SIXTH_DISHES_CASE_BUTTON],
    [SEVENTH_DISHES_CASE_BUTTON],
    [COME_BACK_BUTTON, MY_CART_BUTTON]
], resize_keyboard=True)


SHOW_DESERTS_KEYBOARDS = ReplyKeyboardMarkup([
    [FIRST_DESERTS_CASE_BUTTON, SECOND_DESERTS_CASE_BUTTON],
    [THIRD_DESERTS_CASE_BUTTON, FOURTH_DESERTS_CASE_BUTTON],
    [COME_BACK_BUTTON, MY_CART_BUTTON]
], resize_keyboard=True)


SHOW_GARNISH_KEYBOARDS = ReplyKeyboardMarkup([
    [FIRST_GARNISH_CASE_BUTTON, SECOND_GARNISH_CASE_BUTTON],
    [THIRD_GARNISH_CASE_BUTTON, FOURTH_GARNISH_CASE_BUTTON],
    [FIFTH_GARNISH_CASE_BUTTON, SIXTH_GARNISH_CASE_BUTTON],
    [SEVENTH_GARNISH_CASE_BUTTON, EIGHTH_GARNISH_CASE_BUTTON],
    [COME_BACK_BUTTON, MY_CART_BUTTON]
], resize_keyboard=True)


SHOW_DRINKS_KEYBOARDS = ReplyKeyboardMarkup([
    [FIRST_DRINKS_BUTTON, SECOND_DRINKS_BUTTON],
    [THIRD_DRINKS_BUTTON, FOURTH_DRINKS_BUTTON],
    [FIFTH_DRINKS_BUTTON, SIXTH_DRINKS_BUTTON],
    [SEVENTH_DRINKS_BUTTON, EIGHTH_DRINKS_BUTTON],
    [NINTH_DRINKS_BUTTON, TENTH_DRINKS_BUTTON],
    [ELEVENTH_DRINKS_BUTTON],
    [COME_BACK_BUTTON, MY_CART_BUTTON]
], resize_keyboard=True)