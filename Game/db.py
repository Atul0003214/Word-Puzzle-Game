import sqlite3 as sq
cur = ""
connection = ""
def connectDb(functionName):
    '''
    This function will create a words db and crate a connection to it.
    '''     
    # Create a table and inset new words to database
    global connection,cur
    connection = sq.connect("./Game/words.db",300)    
    cur = connection.cursor()
    # Getting all tables from sqlite_master
    sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""
    cur.execute(sql_query)
    tableResult = cur.fetchall()
    if len(tableResult) > 0:
        if not "wordTable" in tableResult[0]:
            query = """CREATE TABLE wordTable(wordList TEXT);"""
            cur.executescript(query)
            connection.commit()
    else:
        query = """CREATE TABLE wordTable(wordList TEXT);"""
        cur.executescript(query)
        connection.commit()
    return functionName

@connectDb
def insertWord(wordList):
    '''
    This function will insert the words to words databse.
    '''
    for word in wordList: 
        insertQuery = f"INSERT INTO wordTable (wordList) VALUES ('{word}');"
        re = cur.executescript(insertQuery)

    connection.commit()
    cur.execute("SELECT wordList from wordTable;")
    re1 = cur.fetchall()
    print(len(re1))

listWord = ["abstract","absolute","academic","accepted","accident","accuracy","accurate","achieved","acquired","activity","actually","addition","adequate","adjacent","adjusted","advanced","advisory","advocate","affected","aircraft","alliance","although","aluminum","analysis","announce","anything","anywhere","apparent","appendix","approach","approval","argument","artistic","assembly","assuming","athletic","attached","attitude","attorney"]
insertWord(listWord)


