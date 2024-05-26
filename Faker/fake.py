from faker import Faker

fake = Faker("ru_RU")
clients = []

for i in range(10):
    print(f'{{"FIO":"{fake.name()}", "Tel": "{fake.phone_number()}", "Email": "{fake.ascii_free_email()}"}},')