from faker import Faker

fake = Faker("ru_RU")
clients = []

for i in range(10):
    print(f'new("{fake.name()}", "{fake.phone_number()}", "{fake.ascii_free_email()}"),')