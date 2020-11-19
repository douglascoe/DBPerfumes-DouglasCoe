import sqlite3

def titulo(n,s):
    print("=" * n)
    print(f"{s}".center(n))
    print("=" * n)

banco = sqlite3.connect(r"DBPerfumes.db")
cursor = banco.cursor()
#Select Perfume
cursor.execute("SELECT id,nome,quantidade FROM Perfumes")
tabela = cursor.fetchall()
titulo(40, "Perfumes")
print("id".ljust(6)+"nome".ljust(16)+"quantidade".ljust(1))
for linha in tabela:
    print(str(linha[0]).ljust(6), end="")
    print(linha[1].ljust(16), end="")
    print(str(linha[2]).ljust(1))


#Select Volumes
cursor.execute("SELECT * FROM Volumes")
tabela = cursor.fetchall()
titulo(40, "Volumes")
print("id".ljust(6)+"nome".ljust(16))
for linha in tabela:
    print(str(linha[0]).ljust(6), end="")
    print(linha[1].ljust(16))
