from console.db.Collection import Collection


def new(FIO: str, Tel: str, Email: str) -> dict:
    return {"FIO": FIO,
            "Tel": Tel,
            "Email": Email
            }


class Clients(Collection):

    def insertTestData(self):
        self.insert([
            new("Роман Власович Волков", "+7 873 305 12 17", "bogdanovmartjan@yahoo.com"),
            new("Феофан Брониславович Евдокимов", "8 245 704 78 86", "ljubomir1988@rambler.ru"),
            new("Кондрат Эдуардович Харитонов", "+7 (233) 951-0981", "kallistrat_2004@yahoo.com"),
            new("Лазарев Конон Владиленович", "8 (555) 397-2086", "uljan49@yandex.ru"),
            new("Ульяна Романовна Рябова", "+71287516400", "nifont19@yahoo.com"),
            new("Дарья Руслановна Гуляева", "80669756162", "lidija91@yandex.ru"),
            new("Венедикт Жанович Попов", "+7 (003) 611-6141", "haritonovanatalja@yandex.ru"),
            new("Белоусов Елисей Харлампович", "+7 950 991 6621", "jakovlevaoksana@mail.ru"),
            new("Ксения Даниловна Антонова", "85724171691", "lidija2020@hotmail.com"),
            new("Носов Мирослав Герасимович", "8 534 390 4965", "valentin1981@gmail.com")
        ])
        print("Clients test data inserted")


