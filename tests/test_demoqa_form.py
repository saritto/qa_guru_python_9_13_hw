from demoqa_tests.data import users
from demoqa_tests.pages.registration_page import RegistrationPage
import allure
from allure_commons.types import Severity


@allure.tag("web")
@allure.description("Проверка страницы Demoqa practice form")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "saritto")
@allure.link("https://demoqa.com/automation-practice-form", name="Demoqa form")
@allure.title("Проверка страницы Demoqa practice form")
def test_demoqa_form():
    registration_page = RegistrationPage()
    admin = users.admin

    with allure.step("Открываем главную страницу:"):
        registration_page.open()

    with allure.step("Регистрируем пользователя:"):
        registration_page.register(admin)

    with allure.step("Отправляем заполненную форму:"):
        registration_page.submit()

    with allure.step("Открывается форма с зарегистрированными данными:"):
        registration_page.should_have_registered(admin)
