import sqlite3
banco = sqlite3.connect(r"DBPerfumes.db")
cursor = banco.cursor()

#Essencias
cursor.execute("INSERT INTO Essencias VALUES(1,'ACQUA')")
cursor.execute("INSERT INTO Essencias VALUES(2,'ALECRIM')")
cursor.execute("INSERT INTO Essencias VALUES(3,'ALECRIM LE LIS')")
#Fixacoes
cursor.execute("INSERT INTO Fixacoes VALUES(1,'Tipo de Pele')")
cursor.execute("INSERT INTO Fixacoes VALUES(2,'Clima')")
cursor.execute("INSERT INTO Fixacoes VALUES(3,'Concentração')")
#Volumes
cursor.execute("INSERT INTO Volumes VALUES(1,'25ml')")
cursor.execute("INSERT INTO Volumes VALUES(2,'45ml')")
cursor.execute("INSERT INTO Volumes VALUES(3,'55ml')")
#Marcas
cursor.execute("INSERT INTO Marcas VALUES(1,'A')")
cursor.execute("INSERT INTO Marcas VALUES(2,'B')")
cursor.execute("INSERT INTO Marcas VALUES(3,'C')")
#Perfumes
cursor.execute("INSERT INTO Perfumes VALUES(1,'Perfume A',5,3,1,3)")
cursor.execute("INSERT INTO Perfumes VALUES(2,'Perfume B',5,2,2,2)")
cursor.execute("INSERT INTO Perfumes VALUES(3,'Perfume C',5,1,3,1)")
#Essencia_Perfume
cursor.execute("INSERT INTO Essencia_Perfume VALUES(1,1)")
cursor.execute("INSERT INTO Essencia_Perfume VALUES(2,2)")
cursor.execute("INSERT INTO Essencia_Perfume VALUES(3,3)")
banco.commit()
