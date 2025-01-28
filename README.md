# SGE_BLOC2

![captura1](captura1.png)

El que veiem a la imatge és la declaració d'un objecte que consisteix en la connexió amb una base de dades i es pot veure algunes especificacions de la base de dades com el nom de l'usuari que ha creat la base de dades, la contrasenya (censurada òbviament), el nom de la base en aquest cas "the_bear" i també on està allotjada la base de dades en aquest cas al localhost i al port 5432

La part on posa closed: 0 suposo que vol dir que la connexió amb la base de dades esta oberta

![captura2](captura2.png)

El que veiem a aquesta imatge es una consulta de SQL que mostra totes les dades que hem inserit mitjançant els scripts **csv_to_dict.py** i **dict_to_db.py**, l'arxiu **csv_to_dict.py** converteix el csv **Clientes.csv** a un diccionari on les keys son les capçaleres de cada columna i cada valor es una llista de les dades d'aquella columna i l'arxiu **dict_to_db.py** crea i executa la inserció de les dades a la bases de dades 

![captura3](captura3.png)