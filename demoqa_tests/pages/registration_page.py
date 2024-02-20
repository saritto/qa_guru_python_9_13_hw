from selene import browser, have, command

from demoqa_tests.data.users import User
from demoqa_tests import path_file


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.all('[name=gender]')
        self.mobile = browser.element('#userNumber')
        self.date_of_birth = browser.element('#dateOfBirthInput')
        self.year_of_birth = browser.element('.react-datepicker__year-select')
        self.month_of_birth = browser.element('.react-datepicker__month-select')
        self.subject = browser.element('#subjectsInput')
        self.hobby = browser.all('.custom-checkbox')
        self.photo = browser.element('[type=file]')
        self.current_address = browser.element('#currentAddress')
        self.state = browser.element('#react-select-3-input')
        self.city = browser.element('#react-select-4-input')

    @staticmethod
    def open():
        browser.open('https://demoqa.com/automation-practice-form')
        browser.all('[aria-label=Consent]').element_by(have.exact_text('Consent')).click()
        browser.driver.execute_script("document.querySelector('.body-height').style.transform='scale(.50)'")

    def fill_full_name(self, first, last):
        self.first_name.type(first)
        self.last_name.type(last)

    def fill_email(self, value):
        self.email.type(value)

    def fill_gender(self, gender):
        self.gender.element_by(have.value(gender)).element('..').click()

    def fill_mobile(self, value):
        self.mobile.type(value)

    def fill_date_of_birth(self, year, month, day):
        self.date_of_birth.click()
        self.year_of_birth.element(f'[value="{year}"]').click()
        self.month_of_birth.element(f'[value="{month}"]').click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def fill_subject(self, value):
        self.subject.type(value).press_enter()

    def choose_hobbies(self, value):
        self.hobby.element_by(have.exact_text(value)).click()

    def add_photo(self, value):
        self.photo.set_value(path_file.path(value))

    def fill_current_address(self, value):
        self.current_address.type(value)

    def select_state_city(self, value1, value2):
        self.state.type(value1).press_enter()
        self.city.type(value2).press_enter()

    @staticmethod
    def submit():
        browser.element('#submit').perform(command.js.click)

    def register(self, user: User):
        self.fill_full_name(user.first_name, user.last_name)
        self.fill_email(user.email)
        self.fill_gender(user.gender)
        self.fill_mobile(user.mobile)
        self.fill_date_of_birth(user.year_of_birth, user.month_of_birth, user.day_of_birth)
        self.fill_subject(user.subjects)
        self.choose_hobbies(user.hobbies)
        self.add_photo(user.photo)
        self.fill_current_address(user.current_address)
        self.select_state_city(user.state, user.city)

    @staticmethod
    def should_have_registered(user: User):
        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.mobile,
            f'{user.day_of_birth} March,{user.year_of_birth}',
            user.subjects,
            user.hobbies,
            user.photo,
            user.current_address,
            f'{user.state} {user.city}'))
