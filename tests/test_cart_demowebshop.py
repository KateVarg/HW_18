import allure
from demowebshop_test.pages.cart_page import add_product_api
from demowebshop_test.test_data.data import ID_PRODUCT_1, NAME_1, ID_PRODUCT_2, NAME_2


@allure.story('Добавление и проверка товара в корзине')
def test_add_product():
    add_product_api.add_product(ID_PRODUCT_1).open_cart().check_add_product(NAME_1)
    add_product_api.add_product(ID_PRODUCT_2).open_cart().check_add_product(NAME_2)
