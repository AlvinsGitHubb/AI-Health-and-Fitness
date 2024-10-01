import mysql.connector

class mySQLInterface(object):

    #Connects to the database named _database
    def ConnectToDatabase(_host, _user, _password, _database):
        mydb = mysql.connector.connect(
            host=_host,
            user=_user,
            password=_password,
            database=_database
        )
        return mydb

    #Adds an item to mydb of type tableName
    def AddItem(mydb, tableName, rows, vals):
        mycursor = mydb.cursor()
        sql = "INSERT INTO " + tableName + " "
        rowsString = "(" + rows[0]
        valuesString = "(%s"
        for x in range(len(rows) - 2):
            rowsString += ", " + rows[x]
            valuesString += ", %s"
        rowsString += ")"
        valuesString += ")"
        sql += rowsString + " VALUES " + valuesString
        mycursor.executemany(sql, vals)
        mydb.commit()
        
    #Sets an attribute "attribute" of an item in mydb of type tablename
    def SetItemAttribute(mydb, tableName, attribute, toSetTo, _id):
        mycursor = mydb.cursor()
        sql = "UPDATE " + tableName + " SET " + attribute + " = %s WHERE id = %s"
        val = (toSetTo, _id)
        mycursor.execute(sql, val)
        mydb.commit()
        
    #Gets an attribute "attribute" from an item in mydb of type tablename
    def GetItemAttribute(mydb, tableName, attribute, _id):
        mycursor = mydb.cursor()
        sql = "SELECT " + attribute + " FROM "+ tableName + " WHERE id = %s"
        mycursor.execute(sql, _id)
        myresult = mycursor.fetchone()
        return myresult

    pass 




