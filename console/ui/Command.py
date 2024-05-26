from console.db.Collection import Collection
from console.db.Collections.Clients import Clients
from console.db.Collections.Order import Order
from console.db.Collections.FurnitureTypes import FurnitureTypes
from console.db.Collections.Address import Address
from console.db.Collections.Furniture import Furniture

def workWithColl(col: Collection, args: list[str]):
    match args[0]:
        case "insertTestData":
            col.insertTestData()
        case "show":
            col.show(' '.join(args[1:]))
        case "showWith":
            col.showWith(' '.join(args[1:]))
        case "del":
            col.dell(' '.join(args[1:]))
        case "new":
            col.insertString(' '.join(args[1:]))
        case _:
            print("Command not found")


class Commands:
    collections: dict

    def __init__(self):
        self.collections = {
            Clients.name: Clients(),
            Order.name: Order(),
            FurnitureTypes.name: FurnitureTypes(),
            Address.name: Address(),
            Furniture.name: Furniture()
        }

    def runCommand(self, args: list[str]):
        if args[0] not in self.collections:
            print("Collection not found")
        else:
            workWithColl(self.collections[args[0]], args[1:])
