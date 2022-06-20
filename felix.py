import mysql.connector

def goedenmorgen():
    return "goedemorgen van felix"


def toevoegenaandb(meegegevenwaarde):
    mydb = mysql.connector.connect(
        host="localhost",  #port erbij indien mac
        user="root",
        password="",
        database="test"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM fiets")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x[1])
    sql = "INSERT INTO `fiets` (`merk`, `eigenaar`) VALUES (%s, %s);"
    val = (meegegevenwaarde, "fred")
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    return "gelukt"