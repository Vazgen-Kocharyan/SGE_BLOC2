import connect

def read_reg():
    conn = connect.connection_db()
    cursor = conn.cursor()

    sql_read = "SELECT * FROM clientes"

    cursor.execute(sql_read)
    conn.commit()

    results = cursor.fetchall()
    
    for i in results:
        if i[0] == "Andreu":
            print("Les dades de l'Andreu")
            print(i)
            print("El correu de l'Andreu")
            print(i[3])
   
    for i in results:   
        if i[0] == "Vivian":
            print("Les dades de la Vivian")
            print(i)
            print("La direcció de la Vivian")
            print(i[1])

    for i in results:
        if i[0] == "Albert":
            print("Les dades de l'Albert")
            print(i)
            print("La data de cumpleanys de l'Albert")
            print(i[len(i)-1])

    return results
