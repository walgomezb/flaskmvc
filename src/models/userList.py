from userModel import User
class UserList:
    listName="NoName"
    listOfUser=[]
    def __init__(self, listName):
        self.listName = listName
        self.listOfUser=[]
        self.retriveInfo()

    def retriveInfo(self):
        usuarios = [{"name":"Juan","lastName":"Perez"},
                    {"name":"Pedro","lastName":"Ramirez"}]

        for usuario in usuarios:
            newUser = User(usuario['name'],usuario['lastName'])
            self.listOfUser.append(newUser)