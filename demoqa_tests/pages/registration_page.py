from selene import browser, have
import os
from os.path import dirname, abspath

path = os.path.join(dirname(dirname(dirname(abspath(__file__)))), "resources")


class RegistrationPage:
    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.driver.execute_script("document.querySelector('.body-height').style.transform='scale(.50)'")

    def fill_full_name(self, first, last):
        browser.element('#firstName').type(first)
        browser.element('#lastName').type(last)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').element(f'[value="{year}"]').click()
        browser.element('.react-datepicker__month-select').element(f'[value="{month}"]').click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def fill_gender(self, value):
        browser.element(f'[for="gender-radio-{value}"]').click()

    def fill_mobile(self, value):
        browser.element('#userNumber').type(value)

    def fill_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def choose_hobbies(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()

    def add_photo(self, value):
        browser.element('[type=file]').send_keys(path + value)

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)

    def select_state_city(self, value1, value2):
        browser.element('#react-select-3-input').type(value1).press_enter()
        browser.element('#react-select-4-input').type(value2).press_enter()

    def submit(self):
        browser.element('#submit').press_enter()

    def should_registered_user_with(self, thanks, full_name, email, gender, mobile, birthdate, subjects, hobbies,
                                    picture, cur_address, state_city):
        browser.element('#example-modal-sizes-title-lg').should(have.text(thanks))
        browser.element('.table-responsive').all('tr>td').even.should(have.exact_texts(
            full_name,
            email,
            gender,
            mobile,
            birthdate,
            subjects,
            hobbies,
            picture,
            cur_address,
            state_city))