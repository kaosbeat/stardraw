import sqlite3

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



def wordContext(word):
    strippedword = word.strip("'")
    selectQuery = "SELECT prompt FROM prompts WHERE prompt_id IN (SELECT prompts_id FROM words WHERE word = \"" +strippedword+ "\")"
    # print(selectQuery)
    cur.execute(selectQuery)
    data = list(cur)
    wordlist = []
    for p in data:
        for w in p[0]:
            wordlist.append(w)
    return wordlist
        
