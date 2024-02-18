from demoqa_tests.data import users
from demoqa_tests.pages.registration_page import RegistrationPage


def test_demoqa_form():
    registration_page = RegistrationPage()
    admin = users.admin

    registration_page.open()
    registration_page.register(admin)
    registration_page.submit()
    registration_page.should_have_registered(admin)
