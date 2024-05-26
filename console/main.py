from console.ui.Command import Commands

printHelp = '''
Write command in order: [collection] [command] | [sort]
insertTestData -- inserts test data in collection. Example: Clients insertTestData
show -- show all in collection. Example: Clients show | sort_by=FIO order=asc
showWith -- show specific lines in collection. Example: Clients showWith Tel like "+7" | sort_by=FIO order=asc
del -- delite document in collection. Example: Clients del Tel like "+7"
new -- insert document in collection. Example: Clients new {"FIO": "г-жа Ковалева Лукия Ждановна", "Tel": "8 (142) 445-86-17", "Email": "trofim1976@mail.ru"}
'''


if __name__ == '__main__':
    com = Commands()
    print(printHelp)
    ex = False
    while not ex:
        command = input().split(" ")
        if command[0] == "exit":
            ex = True
        else:
            com.runCommand(command)



