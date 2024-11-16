# Regra de Negócio: Inserir registros no Banco de Dados onde a quantidade é superior a 10.

import csv
import sqlite3

with open('producao_alimentos.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)

    conn = sqlite3.connect('dsadb.db')
    conn.execute('DROP TABLE IF EXISTS producao')

    conn.execute('''
    CREATE TABLE producao (
             produto TEXT,
             quantidade INTEGER,
             preco_medio REAL,
             receita_total REAL
             )
            ''')
    
    for row in reader:
        if int(row[1]) > 10:
             conn.execute('INSERT INTO producao (produto, quantidade, preco_medio, receita_total) values (?, ?, ?, ?)', row)
        
    conn.commit()
    conn.close()

print("Concluído com Sucesso!")