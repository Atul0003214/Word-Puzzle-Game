from db import *
import random

def getWord():
    """
    This function will generate the 5 random words from the list of words stored in the database. 
    """
    wordDict = {}
    getQuery = "SELECT wordList from wordTable;"
    cur.execute(getQuery)
    result = cur.fetchall()
    randomWords = random.sample(result, 5)
    for words in randomWords:
        wordDict[words[0]] = "".join(random.sample(words[0], len(words[0])))
    cur.execute("DELETE FROM wordTable;")
    connection.commit()
    connection.close()
    return wordDict


def clearDatabase():
    """This function will clear the stored words in the database"""
    cur.execute("DELETE FROM wordTable;")
    connection.commit()
    connection.close()


