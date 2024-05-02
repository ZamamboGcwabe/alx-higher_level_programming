#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)
    cur = db.cursor()

    query = """SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
               FROM cities
               JOIN states ON cities.state_id = states.id
               WHERE states.name = %s
               GROUP BY states.name"""

    cur.execute(query, (state_name,))

    result = cur.fetchone()

    if result:
        print(result[0])
    else:
        print("")

    cur.close()
    db.close()
