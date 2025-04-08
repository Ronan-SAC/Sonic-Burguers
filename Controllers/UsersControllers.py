from DB.ConnectDB import Banco_De_Dados

class Controller_user:
    def __init__(self):
        self.DB = Banco_De_Dados()  # Criando instância do banco corretamente

    def adicionar(self, nome, cpf, senha):
        return self.DB.adicionar_usuario(nome, cpf, senha)  # Removido 'model'

    def atualizar(self, nome=None, senha=None, id=None):
        return self.DB.atualizar_usuario(nome, senha, id)

    def deletar(self, id):
        return self.DB.deletar_usuario(id)  # Corrigido para passar apenas 'id'

    def verificar(self, cpf, senha):
        return self.DB.verificar_login(cpf, senha)