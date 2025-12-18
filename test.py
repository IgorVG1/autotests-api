from faker import Faker

fake = Faker(locale='ru_RU')

print(f'fake name: {fake.name()}')
print(f'fake address: {fake.address()}')
print(f'fake email: {fake.email()}')