import main
import MySQLInterface

def CheckUserCredentials(email, password): #This might check if the username and password are correct but it also might not idk.
    users = main.GetSQLInterface().GetItemsBasedOnAttribute("user", "username", email)
    for x in users:
        if x[7] == password:
            return x[0]

def CreateUser(username, password):
    main.GetSQLInterface().AddItem("user", ("email", "password"), (username, password))

def SetUserAttribute(attribute, value, userId):
    main.GetSQLInterface().SetItemAttribute("user", attribute, value, userId)
