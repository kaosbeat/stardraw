import random
import sqlite3

# showtime


con=sqlite3.connect('data/Belgium14.sqlite')
con16=sqlite3.connect('data/Belgium16.sqlite')

cur = con.cursor()
cur16 = con16.cursor()

# cur.execute( 'SELECT * FROM db_sanitized14 WHERE relationshipstatus = "It\'s complicated"')
# cur.execute( 'SELECT relationshipstatus FROM db_sanitized14 WHERE relationshipstatus != ""' )
global relationshipstatusses
relationshipstatusses = ["\"In a relationship\"",  "\"It\'s complicated\"", "\"Divorced\"", "\"Engaged\"", "\"Widowed\"", "\"Single\"", "\"Married\"", "\"\""] 
global data
data = []


def getnewList(datatype):
    global data
    global cur
    global relationshipstatusses
    rs = relationshipstatusses[datatype]
    # statement = 'SELECT phone FROM db_sanitized14 WHERE relationshipstatus =' + rs + 'AND phone != ""'
    statement = 'SELECT firstname FROM db_sanitized14 WHERE relationshipstatus =' + rs + 'AND firstname != ""'
    # print(statement)
    cur.execute(statement)
    data = list(cur)

def getRandomname(names):
    # names should be list of tuples like the one you can get from getMaxNamecount [('Xavier', 2), ('Kevin', 4)]
    return names[random.randint(0,len(names)-1)][0]

def getName(names, pos):
     # names should be list of tuples like the one you can get from getMaxNamecount [('Xavier', 2), ('Kevin', 4)]
    return names[pos][0]

zone = random.randint(0,6)
getnewList(zone)



def getMaxNamecount(rs):
    statement = '''SELECT  firstname FROM db_sanitized14 WHERE relationshipstatus = ''' + rs + '''
                GROUP BY firstname
                HAVING COUNT(*) = ( 
                SELECT MAX(Cnt) 
                FROM(
                    SELECT COUNT(*) as Cnt
                    FROM db_sanitized14 WHERE relationshipstatus = '''+rs+'''
                    GROUP BY firstname
                        ) tmp
                    )
                    '''
    # statement = statement + statement2
    # print(statement)
    cur.execute(statement)
    data = list(cur)
    # print(data)
    return data

# data = getMaxNamecount("\"In a relationship\"")


def getNamesCounts(rs):
    statement = '''SELECT firstname, COUNT(firstname) FROM  db_sanitized14 WHERE relationshipstatus = ''' + rs + ''' GROUP BY firstname'''
    cur.execute(statement)
    data = list(cur)
    data.sort(key = lambda x: x[1])
    return data

# getNamesCounts("\"In a relationship\"")


def getAllFromHometown(city):
    statement = '''
                SELECT firstname FROM  db_sanitized16 WHERE city OR workcity LIKE '%'''+city+'''%'

                '''
    cur16.execute(statement)
    # cur16.execute(statement, (hometown) )
    data =  list(cur16)
    # print (len(data))
    # print(data[2][0])
    return data

# data = getAllFromHometown('Antwerp')

                # SELECT * FROM FROM db_sanitized16 WHERE hometown LIKE '%'||?||'%'


# SELECT * FROM media WHERE mediaId IN
#   (SELECT mediaId FROM fav WHERE userId=1)

def GetMostFRequentNameInRelationstatusInCity(relationshipstatus, city):
    statement=  '''
    SELECT firstname, COUNT(firstname) FROM db_sanitized16  WHERE relationshipstatus = ''' + relationshipstatus + ''' AND (city LIKE '%'''+city+'''%' OR workcity LIKE '%'''+city+'''%')
    GROUP BY firstname
    '''
    cur16.execute(statement)
    data =  list(cur16)
    data.sort(key = lambda x: x[1])
    data.reverse()
    # print(data)
    print (len(data), "persons in database with city = ", city, "and relationshipstatus = ", relationshipstatus)
    print(data[-1][0], "is the most common name for a ", relationshipstatus, " person in ", city)
    return data

def GetMostFRequentNameInRelationstatus(relationshipstatus):
    statement=  '''
    SELECT firstname, COUNT(firstname) FROM db_sanitized16  WHERE relationshipstatus = ''' + relationshipstatus + ''' 
    GROUP BY firstname
    '''
    cur16.execute(statement)
    data =  list(cur16)
    data.sort(key = lambda x: x[1])
    data.reverse()
    # print(data)
    print (len(data), "persons in database with relationshipstatus = ", relationshipstatus)
    print(data[-1][0], "is the most common name for a ", relationshipstatus)
    return data


# GetMostFRequentNameInRelationstatusInCity("\"In a relationship\"", "Antwerp")
# data = GetMostFRequentNameInRelationstatusInCity("\"It\'s complicated\"", "Antwerp")
# GetMostFRequentNameInRelationstatusInCity(relationshipstatusses[6], "Antwerp")


# for i in range(10):
#     print(getRandomname(data))

# for i in range(10):
#     print(getName(data, i))