import mysql.connector
import bcrypt

class Banco_De_Dados:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="", 
            database="sonicburger"
        )

    def verificar_existencia(self, cpf, telefone):
        cursor = self.conexao.cursor()
        query = "SELECT COUNT(*) FROM usuarios WHERE cpf = %s OR telefone = %s"
        cursor.execute(query, (cpf, telefone))
        resultado = cursor.fetchone()
        cursor.close()
        return resultado[0] > 0

    def adicionar_usuario(self, nome, cpf, senha, telefone):
        cursor = self.conexao.cursor()
        senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
        cursor.execute(
            "INSERT INTO usuarios (nome, cpf, senha, telefone) VALUES (%s, %s, %s, %s)",
            (nome, cpf, senha_hash, telefone)
        )
        self.conexao.commit()
        cursor.close()

    def atualizar_usuario(self, nome=None, senha=None, id=None):  
        cursor = self.conexao.cursor()
        campos = []
        valores = []
        if nome is not None:
            campos.append("nome = %s")
            valores.append(nome)
        if senha is not None:
            senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
            campos.append("senha = %s") 
            valores.append(senha_hash)
        if not campos:
            cursor.close()
            return False
        query = f"UPDATE usuarios SET {','.join(campos)} WHERE id_user = %s"
        valores.append(id)
        cursor.execute(query, valores)
        self.conexao.commit()
        cursor.close()
        return True

    def deletar_usuario(self, id):
        cursor = self.conexao.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id_user = %s", (id,))
        self.conexao.commit()
        user_del = cursor.rowcount  
        cursor.close()
        return user_del > 0

    def verificar_login(self, cpf, senha):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT senha FROM usuarios WHERE cpf = %s", (cpf,))
        resultado = cursor.fetchone()
        cursor.close()
        if resultado:
            return bcrypt.checkpw(senha.encode('utf-8'), resultado[0].encode('utf-8'))
        return False

    def obter_usuario_por_cpf(self, cpf):
        cursor = self.conexao.cursor()
        query = "SELECT id_user, nome FROM usuarios WHERE cpf = %s"
        cursor.execute(query, (cpf,))
        resultado = cursor.fetchone()
        cursor.close()
        if resultado:
            return {"id_user": resultado[0], "nome": resultado[1]}
        return None
    
    def adicionar_historico(self, id_user, nota_fiscal):
        cursor = self.conexao.cursor()
        cursor.execute(
            "INSERT INTO historico (id_user, nota_fiscal) VALUES (%s, %s)",
            (id_user, nota_fiscal)
        )
        self.conexao.commit()
        cursor.close()