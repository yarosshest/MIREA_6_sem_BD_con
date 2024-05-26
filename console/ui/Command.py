from console.db.Collection import Collection
from console.db.Clients import Clients
from typing import Callable


def workWithColl(col: Collection, args: list[str]):
    match args[0]:
        case "insertTestData":
            col.insertTestData()
        case "show":
            col.show()
        case "showWith":
            col.showWith(' '.join(args[1:]))
        case "del":
            col.dell(' '.join(args[1:]))
        case _:
            print("Command not found")


class Commands:
    collections: dict

    def __init__(self):
        self.collections = {
            Clients.name: Clients(),
        }

    def runCommand(self, args: list[str]):
        if args[0] not in self.collections:
            print("Collection not found")
        else:
            workWithColl(self.collections[args[0]], args[1:])
