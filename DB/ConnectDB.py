import mysql.connector

class Banco_De_Dados:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="", 
            database="sonicBurger",
        )

    def adicionar_usuario(self, nome, cpf, senha):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO usuarios (nome, cpf, senha) VALUES (%s, %s, %s)", (nome, cpf, senha))
        self.conexao.commit()
        cursor.close()

    def atualizar_usuario(self, nome=None, senha=None, id=None):  
        cursor = self.conexao.cursor()
        
        # Lista para montar a query dinamicamente
        campos = []
        valores = []

        # Adiciona apenas os campos que foram fornecidos
        if nome is not None:
            campos.append("nome = %s")
            valores.append(nome)
        if senha is not None:
            campos.append("senha = %s") 
            valores.append(senha)

        # Se nenhum campo foi fornecido, não faz nada
        if not campos:
            cursor.close()
            return False
        
        # Monta a query com os campos a atualizar
        query = f"UPDATE usuarios SET {','.join(campos)} WHERE id = %s"  # Corrigido: Nome da tabela e WHERE
        valores.append(id)

        # Executa a query
        cursor.execute(query, valores)
        self.conexao.commit()
        cursor.close()
        return True

    def deletar_usuario(self, id):
        cursor = self.conexao.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))  
        self.conexao.commit()
        user_del = cursor.rowcount  
        cursor.close()
        return user_del > 0  # Retorna True se algo foi deletado

    def verificar_login(self, cpf, senha):
        cursor = self.conexao.cursor()
        query = "SELECT COUNT(*) FROM usuarios WHERE cpf = %s AND senha = %s"
        cursor.execute(query, (cpf, senha))
        resultado = cursor.fetchone() 
        cursor.close()
        return resultado[0] > 0  # Retorna True se encontrou um usuário com esse CPF e senha
