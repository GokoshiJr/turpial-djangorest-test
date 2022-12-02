import json
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="turpialrest"
)
mycursor = mydb.cursor()

f = open('db/regions.json')

a = json.load(f)

print(a['data'][0])

# SELECT

mycursor.execute("SELECT * FROM api_region")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

mydb.close()

"""
    {
        'location':'canalave-city',
        'name': 'canalave-city-area',
        'pokemons': ['tentacool', 'tentacruel', 'staryu', 'magikarp', 'gyarados', 'wingull', 'pelipper', 'shellos', 'gastrodon', 'finneon', 'lumineon']
    }
"""

""" for el in a['data']:
    print(el['location']) """
"""
areas = a["data"] """

""" for area in areas:
    for pokemon in area["pokemons"]:
        location = area["location"]
        name = area["name"]
        print(f"location: {location}, name: {name}, pokemon: {pokemon}") """


""" # INSERT
for pokemon in area_1["pokemons"]:
    # print(area_1["location"], area_1["name"], pokemon)
    sql = "INSERT INTO area_area (location, name, pokemon) VALUES (%s, %s, %s);"
    val = (area_1["location"], area_1["name"], pokemon)
    mycursor.execute(sql, val)
mydb.commit() """

# INSERT

""" sql = f"INSERT INTO test_jjson (obj) VALUES (%s);"
val = json.dumps(a['data'][0])
mycursor.execute(sql, val)
mydb.commit()

# SELECT

mycursor.execute("SELECT * FROM area_area")
myresult = mycursor.fetchall() """

# mycursor.execute(f"INSERT ")

""" for x in myresult:
    print(x)

mydb.close() """
