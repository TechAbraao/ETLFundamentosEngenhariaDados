# Regra de Negócio: enriquecer os dados adicionando destino e uma coluna com margem de lucro

import sqlite3
import csv

def remove_ponto(valor):
    return int(valor.replace('.', '')) # Replace fará a substituição

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
            receita_total REAL,
            margem_lucro REAL
             )
            ''')
    
    for row in reader:
        if int(row[1]) > 10:
            row[3] = remove_ponto(row[3])

            margem_lucro = (row[3] / float(row[1])) - float(row[2])
            
            conn.execute('INSERT INTO producao (produto, quantidade, preco_medio, receita_total, margem_lucro) values (?, ?, ?, ?, ?)', (row[0], row[1], row[2], row[3], margem_lucro))
            


    conn.commit()
    conn.close()

print("Sucesso!")