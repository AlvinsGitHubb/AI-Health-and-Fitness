from ast import Attribute
import mysql.connector

class MySQLInterface(object):

    def __init__(self, _host, _user, _password, _database):
        self.host = _host #The server�s IP address or domain name
        self.user = _user #The host's username
        self.password = _password #The host's password
        self.database = _database # The name of the database being accessed

    #Connects to the database named _database
    def ConnectToDatabase(self):
        self.mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database #In createDatabase.py the created database is named AIHealthAndFitnessDatabase
        )
        self.mycursor = self.mydb.cursor()

    #Adds an item to mydb of type tableName
    def AddItem(self, tableName, columns, vals):
        sql = f"INSERT INTO {tableName} "
        rowsString = "(" + columns[0]
        valuesString = "(%s"
        for x in range(len(columns) - 1):
            x = x + 1
            rowsString += ", " + columns[x]
            valuesString += ", %s"
        rowsString += ")"
        valuesString += ")"
        sql += rowsString + " VALUES " + valuesString
        self.mycursor.execute(sql, vals)
        self.mydb.commit()
        
    #Sets an attribute "attribute" of an item in mydb of type tablename
    def SetItemAttribute(self, tableName, attribute, toSetTo, id_):
        sql = f"UPDATE {tableName} SET {attribute} = %s WHERE id = %s"
        val = (toSetTo, id_)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        
    #Gets all of the items in a table
    def GetTable(self, tableName):
        sql = f"SELECT * FROM {tableName}"
        self.mycursor.execute(sql)
        results = self.mycursor.fetchall()
        return results

    #Gets all of the data from one item of type tablename
    def GetItem(self, tableName, id_):
        sql = f"SELECT * FROM {tableName} WHERE id = {id_}"
        self.mycursor.execute(sql)
        results = self.mycursor.fetchone()
        return results

    #Gets all of the data from one item of type tablename
    def GetItemBasedOnAttribute(self, tableName, attribute, value):
        sql = f"SELECT * FROM {tableName} WHERE {attribute} = {value}"
        self.mycursor.execute(sql)
        results = self.mycursor.fetchone()
        return results
    
    #Gets all of the data from one item of type tablename
    def GetItemsBasedOnAttribute(self, tableName, attribute, value):
        sql = f"SELECT * FROM {tableName} WHERE {attribute} = {value}"
        self.mycursor.execute(sql)
        results = self.mycursor.fetchall()
        return results

    #Gets an attribute "attribute" from an item in mydb of type tablename
    def GetItemAttribute(self, tableName, attribute, id_):
        sql = f"SELECT {attribute} FROM {tableName} WHERE id = {id_}"
        self.mycursor.execute(sql)
        myresult = self.mycursor.fetchone()
        return myresult

    def GetItemAttributes(self, tableName, attributes, id_):
       attributeList = f"{attributes[0]}"
       for x in range(len(attributes) - 1):
           x = x + 1
           attributeList += ", " + attributes[x]
       sql = f"SELECT {attributeList} FROM {tableName} WHERE id = {id_}"
       self.mycursor.execute(sql)
       myresult = self.mycursor.fetchall()
       return myresult

    def GetLastInsertId(self):
       self.mycursor.execute("SELECT LAST_INSERT_ID()")
       return self.mycursor.fetchone()[0]  # Fetches the ID from the result

    #I put this here just for testing code and editing the database values easily it should not be used in the final code project
    def execute(self, command):
        self.mycursor.execute(command)

    pass 