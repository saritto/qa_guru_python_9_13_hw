from selene import browser, have
import os
from os.path import dirname, abspath

path = os.path.join(dirname(abspath(__file__)), "resources")


def test_demoqa_form():

    browser.open('https://demoqa.com/automation-practice-form')
    browser.driver.execute_script("document.querySelector('.body-height').style.transform='scale(.50)'")

    browser.element('#firstName').type('firstName')
    browser.element('#lastName').type('lastName')
    browser.element('#userEmail').type('test@gmail.com')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('7777777777')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').element('[value="1991"]').click()
    browser.element('.react-datepicker__month-select').element('[value="2"]').click()
    browser.element('.react-datepicker__day--003').click()

    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[type=file]').send_keys(path + '/orig.jpg')
    browser.element('#currentAddress').type('Current Address')
    browser.element('#react-select-3-input').type('raj').press_enter()
    browser.element('#react-select-4-input').type('jai').press_enter()
    browser.element('#submit').press_enter()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table-responsive').all('tr>td').even.should(have.exact_texts(
        'firstName lastName',
        'test@gmail.com',
        'Female',
        '7777777777',
        '03 March,1991',
        'Computer Science',
        'Reading',
        'orig.jpg',
        'Current Address',
        'Rajasthan Jaipur'))
