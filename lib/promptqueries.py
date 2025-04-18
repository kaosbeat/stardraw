import sqlite3
from random import choice

'''
sqlite> Select count(*) from prompts Where prompt LIKE '%word%';
sqlite> select word, count from wordcount order by count asc;
sqlite> select * from wordcount order by count desc;
'''

con=sqlite3.connect('data/prompts.db')
cur = con.cursor()

def countwords(word):
    strippedword = word.strip("'")
    selectQuery = "SELECT * FROM  words  WHERE word  = \"" +strippedword+ "\""
    # print(selectQuery)
    cur.execute(selectQuery)
    data = list(cur)
    totalcount = len(data)
    # print(word, totalcount)
    return totalcount

def listWords():
    query = "SELECT DISTINCT word FROM words"
    cur.execute(query)
    data = []
    for row in cur:
        w = row[0]
        data.append(w)
        # countwords(w)

    return data

def create_wordcount(conn, word, totalcount):
    """
    Create a new wordcount
    :param conn:
    :param word:
    :param totalcount
    """
    # print("adding word")

    sql = ''' INSERT INTO wordcount(word, count)
              VALUES(?,?) '''
    cur = conn.cursor()
    row = (word, totalcount)
    cur.execute(sql, row)
    conn.commit()
    return cur.lastrowid


blacklist = ["", " ", "4K", "4k", "8K", "8k", "HD", "HDR", "in", "on", "a", "of", "by", "the", "is", "for" , "with", "as" ,"and", "rutkowski", "trending", "artstation"]

def wordContext(word):
    strippedword = word.strip("'")
    blacklist.append(strippedword)
    # selectQuery = "SELECT prompt FROM prompts WHERE prompt_id IN (SELECT prompts_id FROM words WHERE word = \"" +strippedword+ "\")"
    selectQuery = "SELECT prompt FROM prompts WHERE prompt_id IN (SELECT prompts_id FROM words WHERE word = \"" +strippedword+ "\")  ORDER BY RANDOM() LIMIT 100"
    # print(selectQuery)
    cur.execute(selectQuery)
    data = list(cur)
    wordlist = []
    for p in data:
        for w in p:
            words = w.split(' ')
            for word in words:
                word = word.strip("+|[]()'\"%$#@!^&*,:")
                # print(word)
                # print("-------------")
                # # 
                if word in blacklist:
                    pass
                else:
                    wordlist.append(word)
    return wordlist


def getrandomwordlist():
    selectQuery = "SELECT word, length(word) FROM words WHERE (length(word) > 4 and length(word) < 8)"
    print(selectQuery)
    cur.execute(selectQuery)
    data = list(cur)
    wordlist = []
    for d in data:
        w = d[0].strip("|[]()'\"%$#@!^&*,:")
        print(w)
        if w in blacklist:
            pass
        else:
            wordlist.append(w)
    return wordlist



print (wordContext("nendoroid"))

# print(getrandomwordlist())