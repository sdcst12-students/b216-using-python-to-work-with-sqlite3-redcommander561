"""
Create a query to create a table to store game information for a league of Provincial/Territory teams
Each entry should list:

id unique integer identifier
home team name
away team name
home team score
away team score

choose appropriate variable types for each field
add the data in the dictionary to your table
"""
import sqlite3
#if there is an easier way to convert the scores i could not find and had to do manually
scores = [
    {'home': 'NU', 'homeScore': 2, 'away': 'NS', 'awayScore': 2},
    {'home': 'PE', 'homeScore': 0, 'away': 'YT', 'awayScore': 2},
    {'home': 'NU', 'homeScore': 1, 'away': 'YT', 'awayScore': 3},
    {'home': 'NT', 'homeScore': 3, 'away': 'ON', 'awayScore': 1},
    {'home': 'NU', 'homeScore': 2, 'away': 'ON', 'awayScore': 1},
    {'home': 'BC', 'homeScore': 0, 'away': 'SK', 'awayScore': 3},
    {'home': 'SK', 'homeScore': 2, 'away': 'NU', 'awayScore': 0},
    {'home': 'MN', 'homeScore': 1, 'away': 'NS', 'awayScore': 3},
    {'home': 'ON', 'homeScore': 0, 'away': 'AB', 'awayScore': 1},
    {'home': 'MN', 'homeScore': 3, 'away': 'NU', 'awayScore': 2},
    {'home': 'NB', 'homeScore': 0, 'away': 'NL', 'awayScore': 1},
    {'home': 'BC', 'homeScore': 3, 'away': 'NT', 'awayScore': 2},
    {'home': 'ON', 'homeScore': 1, 'away': 'NU', 'awayScore': 3},
    {'home': 'NS', 'homeScore': 1, 'away': 'ON', 'awayScore': 1},
    {'home': 'NL', 'homeScore': 3, 'away': 'BC', 'awayScore': 1},
    {'home': 'NL', 'homeScore': 2, 'away': 'NT', 'awayScore': 1},
    {'home': 'NU', 'homeScore': 2, 'away': 'AB', 'awayScore': 3},
    {'home': 'MN', 'homeScore': 1, 'away': 'YT', 'awayScore': 1},
    {'home': 'BC', 'homeScore': 1, 'away': 'PE', 'awayScore': 0},
    {'home': 'QC', 'homeScore': 1, 'away': 'NL', 'awayScore': 0},
    {'home': 'NL', 'homeScore': 1, 'away': 'NT', 'awayScore': 3},
    {'home': 'BC', 'homeScore': 1, 'away': 'ON', 'awayScore': 0},
    {'home': 'SK', 'homeScore': 0, 'away': 'AB', 'awayScore': 1},
    {'home': 'YT', 'homeScore': 2, 'away': 'QC', 'awayScore': 2},
    {'home': 'NT', 'homeScore': 2, 'away': 'NU', 'awayScore': 3},
    {'home': 'NB', 'homeScore': 2, 'away': 'NT', 'awayScore': 2},
    {'home': 'PE', 'homeScore': 2, 'away': 'BC', 'awayScore': 0},
    {'home': 'PE', 'homeScore': 2, 'away': 'NB', 'awayScore': 0},
    {'home': 'PE', 'homeScore': 0, 'away': 'YT', 'awayScore': 0},
    {'home': 'NB', 'homeScore': 3, 'away': 'MN', 'awayScore': 2},
    {'home': 'AB', 'homeScore': 0, 'away': 'NL', 'awayScore': 2},
    {'home': 'QC', 'homeScore': 2, 'away': 'NL', 'awayScore': 1},
    {'home': 'SK', 'homeScore': 0, 'away': 'MN', 'awayScore': 0},
    {'home': 'QC', 'homeScore': 2, 'away': 'BC', 'awayScore': 3},
    {'home': 'NU', 'homeScore': 2, 'away': 'AB', 'awayScore': 2},
    {'home': 'NS', 'homeScore': 3, 'away': 'AB', 'awayScore': 3},
    {'home': 'QC', 'homeScore': 1, 'away': 'NT', 'awayScore': 1},
    {'home': 'SK', 'homeScore': 3, 'away': 'AB', 'awayScore': 0},
    {'home': 'NL', 'homeScore': 3, 'away': 'QC', 'awayScore': 1},
    {'home': 'NL', 'homeScore': 2, 'away': 'SK', 'awayScore': 1},
    {'home': 'YT', 'homeScore': 1, 'away': 'BC', 'awayScore': 3},
    {'home': 'NL', 'homeScore': 2, 'away': 'PE', 'awayScore': 2},
    {'home': 'YT', 'homeScore': 1, 'away': 'NL', 'awayScore': 1},
    {'home': 'NS', 'homeScore': 0, 'away': 'QC', 'awayScore': 1},
    {'home': 'BC', 'homeScore': 1, 'away': 'NB', 'awayScore': 3},
    {'home': 'NL', 'homeScore': 3, 'away': 'NU', 'awayScore': 1},
    {'home': 'QC', 'homeScore': 0, 'away': 'SK', 'awayScore': 0},
    {'home': 'NS', 'homeScore': 0, 'away': 'SK', 'awayScore': 0},
    {'home': 'AB', 'homeScore': 1, 'away': 'NT', 'awayScore': 2},
    {'home': 'YT', 'homeScore': 2, 'away': 'QC', 'awayScore': 2},
    {'home': 'YT', 'homeScore': 1, 'away': 'NB', 'awayScore': 3},
    {'home': 'NT', 'homeScore': 0, 'away': 'QC', 'awayScore': 2},
    {'home': 'ON', 'homeScore': 2, 'away': 'BC', 'awayScore': 2},
    {'home': 'BC', 'homeScore': 0, 'away': 'ON', 'awayScore': 1},
    {'home': 'MN', 'homeScore': 1, 'away': 'ON', 'awayScore': 3},
    {'home': 'SK', 'homeScore': 2, 'away': 'NU', 'awayScore': 1},
    {'home': 'MN', 'homeScore': 3, 'away': 'PE', 'awayScore': 1},
    {'home': 'NU', 'homeScore': 2, 'away': 'YT', 'awayScore': 3},
    {'home': 'AB', 'homeScore': 0, 'away': 'NT', 'awayScore': 0}
]

file = 'dbase.db'
connection = sqlite3.connect(file)
print(connection)

cursor = connection.cursor()
cursor.execute("delete from games")

query = """
create table if not exists games (
    id integer primary key autoincrement,
    homeName text,
    homeScore int,
    awayName text,
    awayScore int
);
"""
cursor.execute(query)

for score in scores:
    query = f"""
    insert into games (homeName, homeScore, awayName, awayScore)
    values ('{score['home']}', {score['homeScore']}, '{score['away']}', {score['awayScore']});
    """
    cursor.execute(query)

connection.commit()

query = "select * from games"
cursor.execute(query)
result = cursor.fetchall()
for row in result:
    print(row)

connection.close()