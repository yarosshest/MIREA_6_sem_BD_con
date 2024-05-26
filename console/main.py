from console.ui.Command import Commands


# def printHelpF():
#     for com in commands.values():
#         print(f"{com.name} -- {com.description}")
#
#
# printHelp = Command("printHelp",
#                     "All comands",
#                     printHelpF)
#
# commands = {
#     printHelp.name: printHelp,
#     fillClients.name: fillClients,
#     showClients.name: showClients,
# }

if __name__ == '__main__':
    com = Commands()
    ex = False
    while not ex:
        command = input().split(" ")

        if command[0] == "exit":
            ex = True
        else:
            com.runCommand(command)



