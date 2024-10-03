import mysql.connector

class MySQLInterface(object):

    def __init__(self, _host, _user, _password, _database):
        self.host = _host
        self.user = _user
        self.password = _password
        self.database = _database

    #Connects to the database named _database
    def ConnectToDatabase(self):
        self.mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database #In createDatabase.py the created database is named AIHealthAndFitnessDatabase
        )

    #Adds an item to mydb of type tableName
    def AddItem(self, tableName, rows, vals):
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO " + tableName + " "
        rowsString = "(" + rows[0]
        valuesString = "(%s"
        for x in range(len(rows) - 1):
            x = x + 1
            rowsString += ", " + rows[x]
            valuesString += ", %s"
        rowsString += ")"
        valuesString += ")"
        sql += rowsString + " VALUES " + valuesString
        print(sql)
        mycursor.execute(sql, vals)
        self.mydb.commit()
        
    #Sets an attribute "attribute" of an item in mydb of type tablename
    def SetItemAttribute(self, tableName, attribute, toSetTo, _id):
        mycursor = self.mydb.cursor()
        sql = "UPDATE " + tableName + " SET " + attribute + " = %s WHERE id = %s"
        val = (toSetTo, _id)
        mycursor.execute(sql, val)
        self.mydb.commit()
        
    #Gets all of the items in a table
    def GetTable(self, tableName):
        mycursor = self.mydb.cursor()
        sql = "SELECT * FROM " + tableName;
        mycursor.execute(sql)
        results = mycursor.fetchall()
        return results

    #Gets all of the data from one item of type tablename
    def GetItem(self, tableName, _id):
        mycursor = self.mydb.cursor()
        sql = "SELECT * FROM " + tableName + " WHERE id = %s"
        mycursor.execute(sql, _id)
        results = mycursor.fetchone()
        return results

    #Gets an attribute "attribute" from an item in mydb of type tablename
    def GetItemAttribute(self, tableName, attribute, _id):
        mycursor = self.mydb.cursor()
        sql = "SELECT " + attribute + " FROM "+ tableName + " WHERE id = %s"
        mycursor.execute(sql, _id)
        myresult = mycursor.fetchone()
        return myresult

    #I put this here just for testing code and editing the database values easily it should not be used in the final code project
    def execute(self, command):
        mycursor = self.mydb.cursor()
        mycursor.execute(command)

    pass 




