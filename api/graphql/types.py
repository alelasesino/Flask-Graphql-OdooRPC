from graphene import ObjectType, String, Int


class Product(ObjectType):
    id = Int()
    name = String()

    def __init__(self):
        self.id = 5
        self.name = "Nombrelol"

    def resolve_name(self, info):
        print("resuolve")
        return self.name

    def resolve_id(self, info):
        return self.id





