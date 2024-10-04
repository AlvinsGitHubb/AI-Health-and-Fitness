sqlInterface = MySQLInterface.MySQLInterface("localhost", "root", "*tr5d7Ka9q", "AIHealthAndFitnessDatabase")

sqlInterface.ConnectToDatabase()

def GetSQLInterface():
    return sqlInterface
