import sys
sys.path.append(".")
sys.path.append("../models/")
sys.path.append("./models/")
from userList import UserList


class UserListCtrl():

    def __init__(self, listName):
        self.userList = UserList(listName)

