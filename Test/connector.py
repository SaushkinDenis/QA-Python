import sqlite3

import mysql.connector

DB = "DB/SQLite.sqlite"
DB = ""

class Sqlite:
    def __init__(self, file):
        self.db = file
        self.connection = sqlite3.connect(self.db, timeout=10)


class MySQL:
    def __init__(self):
        self.connection = mysql.connector.connect(user='root', password='root', host='0.0.0.0', port='3306')


def __connect_sql(sql="Sqlite"):
    if sql == "Sqlite":
        return Sqlite(DB)
    elif sql == "MySql":
        return MySQL()



def __close_connect_sql():
    Sqlite(DB).connection.close()


def _execute(execute=None, value=None):
    db = __connect_sql()
    if value:
        result = db.connection.execute(execute, value)
    else:
        result = db.connection.execute(execute)
    db.connection.commit()
    __close_connect_sql()
    return result


def add_row(table, value):
    sql = "INSERT INTO {table} ({title}) VALUES ({value})".format(table=table["name"],
                                                                  title=table["title"],
                                                                  value=value)
    _execute(sql)


def update_row(table, field, search_value, new_value):
    sql = "UPDATE {table} SET {field}='{new_value}' WHERE {field}='{search_value}'".format(table=table["name"],
                                                                                           field=field,
                                                                                           new_value=new_value,
                                                                                           search_value=search_value)
    _execute(sql)


def delete_row(table, field, search_value):
    sql = "DELETE FROM {table} WHERE {field}='{search_value}'".format(table=table['name'],
                                                                      field=field,
                                                                      search_value=search_value)
    _execute(sql)


def get_param_row(table, field, search_field, search_value):
    sql = "SELECT {field} FROM {table} WHERE {search_field} = '{search_value}'".format(field=field,
                                                                                       table=table["name"],
                                                                                       search_field=search_field,
                                                                                       search_value=search_value)
    return _execute(sql)


def get_all_rows(table):
    sql = "SELECT * FROM {DB}".format(DB=table['name'])
    return _execute(sql).fetchall()


def get_count_row(table):
    return len(get_all_rows(table))


def print_rows(table):
    for i in get_all_rows(table):
        print(i)
