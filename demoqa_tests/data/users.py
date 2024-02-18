import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    day_of_birth: str
    month_of_birth: str
    year_of_birth: str
    subjects: str
    hobbies: str
    photo: str
    current_address: str
    state: str
    city: str


admin = User(
    first_name='Yana',
    last_name='Testovna',
    email='test@gmail.com',
    gender='Female',
    mobile='7777777777',
    day_of_birth='11',
    month_of_birth='2',
    year_of_birth='1991',
    subjects='Computer Science',
    hobbies='Reading',
    photo='orig.jpg',
    current_address='Current Address',
    state='Rajasthan',
    city='Jaipur'
)
