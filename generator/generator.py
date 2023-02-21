from faker import Faker


class Person:
    fake = Faker('ru_RU')

    def __init__(self):
        self.full_name = self.fake.name()
        self.first_name = self.fake.first_name()
        self.last_name = self.fake.last_name()
        self.email = self.fake.ascii_email()
        self.current_address = self.fake.address()
        self.permanent_address = self.fake.address()
        self.job = self.fake.job()

