from console.db.Collection import Collection
from console.db.Clients import Clients
from typing import Callable


class Command:
    name: str
    description: str
    fun: Callable

    def __init__(self, name: str, description: str, fun: Callable):
        self.name = name
        self.description = description
        self.fun = fun

    def run(self, *args):
        self.fun(*args)


fillClients = Command("fillClients",
                      "fill collection Clients",
                      Clients.insertTestData)
