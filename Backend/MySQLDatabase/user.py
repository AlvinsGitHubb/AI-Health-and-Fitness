from .MySQLInterface import MySQLInterface


def Login(sqlInterface, email, password): #This might check if the username and password are correct but it also might not idk.
    users = sqlInterface.GetTable("users")
    for x in users:
        if x[8] == email and x[9] == password:
            return x[0]
    return -1

def CreateAccount(sqlInterface, email, password):
     sqlInterface.AddItem("users", ("email", "password"), (email, password))

     return Login(sqlInterface, email, password)

def SetUserAttribute(sqlInterface, attribute, value, userId):
    sqlInterface.SetItemAttribute("users", attribute, value, userId)

def GetUserAttributes(sqlInterface, userId):
    _user = sqlInterface.GetItem("users", userId)
    return _user
        
def GetUserAttribute(sqlInterface, attribute, userId):
    _attribute = sqlInterface.GetItemAttribute("users", attribute, userId)
    return _attribute

def GetUserAttributesForAI(sqlInterface, userId):
    _attributes = sqlInterface.GetItemAttributes("users", ("sex", "age", "height", "weight", "diabetes", "fitnessGoal"), userId)
    OHEData = GetOneHotEncodedVersionOfUserData(_attributes)
    return OHEData

def GetOneHotEncodedVersionOfUserData(userData):
    OHEUserData = []
    if userData[0] == 1: # 1 is male
        OHEUserData.append(True)
        OHEUserData.append(False)
    else:
        OHEUserData.append(False)
        OHEUserData.append(True)

    for x in range(1, 5):
        OHEUserData.append(userData[x])

    
    if userData[5] == 0: # 0 is loose weight
        OHEUserData.append(True)
        OHEUserData.append(False)
    else:
        OHEUserData.append(False)
        OHEUserData.append(True)

    return OHEUserData
