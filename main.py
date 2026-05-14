import pyodbc

connection_string =  (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\vinic\OneDrive\CODE\PROJECTS\app-adm\Requerimento MATERIAL.accdb;'
    )
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()


# for table_info in cursor.tables(tableType='TABLE'):
#     print(table_info.table_name)


#CRIAÇÃO DE UM REQUERIMENTO NOVO E ENVIO AO BD
# sql = "INSERT INTO [Requerimento] ([Beneficiado], [Responsável], [Finalidade], [Data do Requerimento]) VALUES (?, ?, ?, ?)"
# cursor.execute(sql, (193, 1, 'Compra de material', '10/05/2026'))
# connection.commit()



# cursor.execute("select Nome from Beneficiado")
# row = cursor.fetchall()
# if row:
#     print(row)

# cursor.execute("select Nome, Dt_Digitação  from Beneficiado")
# row = cursor.fetchone()
# print("Data: ", row[1])
# print("name: ", row.Nome)


# cursor.execute("select Nome, Dt_Digitação  from Beneficiado")
# while True:
#     row = cursor.fetchone()
#     if not row:
#         break
#     print('Nome:', row.Nome)

##variaveis uteis
ID_REQ = "Id_Requerimento"
BEN = "Beneficiado"
RESP = "Responsável"
OBS = "Observação"
FIN = "Finalidade"

## CONSULTAR REQUERIMENTO PELO ID
def consultaId(id):
    #cria um dicionário pra armazenar os dados do requerimento
    req = {
        "id: ": "",
        "Data:" : "",
        "Beneficiado:": "",
        "Responsavel:": "",
        "Finalidade": "",
        "Observação": "",
    }
    #pesquisa no requerimento 
    sql = f"SELECT [{ID_REQ}], [Data do Requerimento], [{BEN}], [{RESP}], [{FIN}], [{OBS}]  from Requerimento where [{ID_REQ}] = ?"
    cursor.execute(sql, (id,))

    

    #resgata o resultado da execução
    result = cursor.fetchone()


    if id in result:
        print("passa")
    else:
        print("não passa")
    #colocando os valores no dicionario e retorno eles 
    if result:
        for i,j  in zip(req, result):
            req[i] = j
    
  

    #buscando no Beneficiado o que tiver o id do requerimento
    beneficiado = req["Beneficiado:"]
    sql = f"SELECT [Nome] from Beneficiado WHERE [Id_Beneficiado] = ?"
    cursor.execute(sql, (beneficiado))
    beneficiado = cursor.fetchone()
    req["Beneficiado:"] = beneficiado[0]

    #fazendoa  mesma alteração para o responsável
    responsavel = req["Responsavel:"]
    sql = f"SELECT [Nome] from Responsavel WHERE [Id_Responsavel] = ?"
    cursor.execute(sql, (responsavel))
    responsavel = cursor.fetchone()
    req["Responsavel:"] = responsavel[0]

    for i in req:
        print(f"{i} : {req[i]}")

while True:
    id = int(input("Digite o id:"))
    consultaId(id)