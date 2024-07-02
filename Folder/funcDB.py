import sqlite3

def ShowDB(database = "Image_Record_SQLDB.db", table_name = "Image_Record_SQLDB_TABLE"):

    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    table_name_1 = str("\'")+str(table_name)+str("\'")
    sql_query_1 = str("pragma table_info(")+str(table_name_1)+str(")")
    cursor.execute(sql_query_1)
    columns = cursor.fetchall()
    column_name = []    
    for column in columns:
        column_name.append(column[1])
    conn.close()
    return column_name
    print(column_name)
    
    
def read_sql_databse(database, sql_query):
    
    connection_1 = sqlite3.connect(database)
    cursor_1 = connection_1.cursor()
    cursor_1.execute(sql_query)
    datas = cursor_1.fetchall()
    connection_1.commit()
    connection_1.close()
    
    return datas

def searchDB(database, filename):
    filename = str(filename)
    connection_1 = sqlite3.connect(database)
    cursor_1 = connection_1.cursor()
    sql_query = str("SELECT image_filename from Image_Record_SQLDB_TABLE where image_filename = '")+str(filename)+str("';")
    # sql_query = "select image_filename from Image_Record_SQLDB_TABLE where image_filename = '1.jpg';"
    # print(sql_query)
    # sql_query = "SELECT image_filename from Image_Record_SQLDB_TABLE where image_filename = filename";
    cursor_1.execute(sql_query)
    datas = cursor_1.fetchall()
    connection_1.commit()
    connection_1.close()
    
    return datas