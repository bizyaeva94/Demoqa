from faker import Faker


class Person:
    fake = Faker('ru_RU')
    full_name = fake.name()
    email = fake.ascii_email()
    current_address = fake.address()
    permanent_address = fake.address()
    print(full_name)
    print(email)
    print(current_address)
    print(permanent_address)
