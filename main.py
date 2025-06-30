import duckdb

conexao = duckdb.connect("./database.duckdb")

with open("./test.sql") as query:
    dataframe = conexao.execute(query.read()).df()
    print(dataframe)