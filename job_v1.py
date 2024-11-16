# Criando um Banco de Dados SQLite e inserindo valores através do arquivo 'producao_alimentos.csv'

import csv
import sqlite3

# Criando um banco de dados 
conn = sqlite3.connect("dsadb.db")

# Criando uma tabela no banco de dados
conn.execute('''
    CREATE TABLE producao (
             produto TEXT,
             quantidade INTEGER,
             preco_medio REAL,
             receita_total REAL
             )
            ''')

# Gravando a alteração e fechando a conexão
conn.commit()
conn.close()

#
with open('producao_alimentos.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    conn = sqlite3.connect("dsadb.db")
    for row in reader:
        conn.execute('INSERT INTO producao (produto, quantidade, preco_medio, receita_total) values (?, ?, ?, ?)', row)
    conn.commit()
    conn.close()

print("Concluído Com Sucesso!")