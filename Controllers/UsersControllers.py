from DB.ConnectDB import Banco_De_Dados

class Controller_user:
    def __init__(self):
        self.DB = Banco_De_Dados()

    def adicionar(self, nome, cpf, senha, telefone):
        if self.DB.verificar_existencia(cpf, telefone):
            return False, "CPF ou telefone já cadastrado"
        try:
            self.DB.adicionar_usuario(nome, cpf, senha, telefone)
            return True, "Conta criada com sucesso"
        except Exception as e:
            return False, f"Erro ao criar conta: {str(e)}"

    def atualizar(self, nome=None, senha=None, id=None):
        return self.DB.atualizar_usuario(nome, senha, id)

    def deletar(self, id):
        return self.DB.deletar_usuario(id)

    def verificar(self, cpf, senha):
        if self.DB.verificar_login(cpf, senha):
            usuario = self.DB.obter_usuario_por_cpf(cpf)
            if usuario:
                return True, usuario  # Returns (True, {"id_user": id, "nome": name})
            return False, "Usuário não encontrado"
        return False, "CPF ou senha incorretos"

    def obter_usuario(self, cpf):
        return self.DB.obter_usuario_por_cpf(cpf)