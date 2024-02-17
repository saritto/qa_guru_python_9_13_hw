from demoqa_tests.pages.registration_page import RegistrationPage


def test_demoqa_form():
    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.fill_full_name('Yana', 'Testovna')
    registration_page.fill_email('test@gmail.com')
    registration_page.fill_gender(2)  # 1=Male, 2=Female, 3=Other
    registration_page.fill_mobile('7777777777')
    registration_page.fill_date_of_birth('1991', '2', '11')
    registration_page.fill_subject('Computer Science')
    registration_page.choose_hobbies('Reading')
    registration_page.add_photo('/orig.jpg')
    registration_page.fill_current_address('Current Address')
    registration_page.select_state_city('raj', 'jai')
    registration_page.submit()
    registration_page.should_registered_user_with(
        'Thanks for submitting the form',
        'Yana Testovna',
        'test@gmail.com',
        'Female',
        '7777777777',
        '11 March,1991',
        'Computer Science',
        'Reading',
        'orig.jpg',
        'Current Address',
        'Rajasthan Jaipur')
