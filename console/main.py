from console.ui.Command import fillClients
from console.ui.Command import Command


def printHelpF():
    for com in commands.values():
        print(f"{com.name} -- {com.description}")


printHelp = Command("printHelp",
                    "All comands",
                    printHelpF)

commands = {
    printHelp.name: printHelp,
    fillClients.name: fillClients
}

if __name__ == '__main__':
    printHelpF()
    ex = False
    while not ex:
        command = input().split(" ")

        if command[0] == "exit":
            ex = True
        elif command[0] in commands:
            commandExec = commands[command[0]]
            commandExec.fun(*command[1:])
        else:
            print("Command not found")


