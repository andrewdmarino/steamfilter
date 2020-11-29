import psycopg2
import collections
import simplejson as json

connection = psycopg2.connect(user="quikbot",
                              password="1Minus0123",
                              host="database-1.cfzq7u8p3cto.us-west-2.rds.amazonaws.com",
                              port="5432",
                              database="postgres")

cursor = connection.cursor()
# Print PostgreSQL Connection properties
#print (connection.get_dsn_parameters(),"\n")

# Print PostgreSQL version
#cursor.execute("SELECT version();")
#record = cursor.fetchone()
#print("You are connected to - ", record,"\n")

# dynamic query / query all data / write to ordered dictionary
cursor.execute("SELECT * FROM steam_clean")
rows = cursor.fetchall()
print(len(rows))
game_list = []
for row in rows:
    d = collections.OrderedDict()
    d['appID'] = row[0]
    d['game_name'] = row[1]
    d['game_score'] = row[2]
    d['genre'] = row[3]
    d['tag'] = row[4]
    d['price'] = row[5]
    d['min_owners'] = row[6]
    d['max_owners'] = row[7]
    d['hit'] = row[8]
    game_list.append(d)

json_object = json.dumps(game_list, indent = 4)   
#print(json_object) 

with open("sample.json", "w") as outfile: 
    json.dump(json_object, outfile) 

cursor.close()
connection.close()
print("PostgreSQL connection is closed")
