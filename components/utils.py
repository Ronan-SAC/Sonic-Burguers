import re

def validar_nome(nome):
    """Valida o campo Nome Completo"""
    if not nome or len(nome.strip()) < 3:
        return False, "O nome deve ter pelo menos 3 caracteres"
    if not all(char.isalpha() or char.isspace() for char in nome):
        return False, "O nome deve conter apenas letras e espaços"
    if len(nome.split()) < 2:
        return False, "Digite o nome completo (pelo menos nome e sobrenome)"
    return True, ""

def validar_telefone(telefone):
    """Valida o campo Telefone"""
    # Remove caracteres não numéricos
    telefone = ''.join(filter(str.isdigit, telefone))
    # Verifica se tem 11 dígitos (formato brasileiro: DDD + número)
    if len(telefone) != 11:
        return False, "O telefone deve ter 11 dígitos (DDD + número)"
    # Verifica se o DDD é válido (11-99)
    if not (11 <= int(telefone[:2]) <= 99):
        return False, "DDD inválido"
    # Verifica se o número começa com 9 (celular)
    if telefone[2] != '9':
        return False, "O número deve começar com 9"
    return True, ""

def validar_cpf(cpf):
    """Valida o campo CPF"""
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
    # Verifica se tem 11 dígitos
    if len(cpf) != 11:
        return False, "O CPF deve ter 11 dígitos"
    # Verifica se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False, "CPF inválido (dígitos repetidos)"
    # Cálculo do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10) % 11
    digito1 = 0 if digito1 > 9 else digito1
    # Cálculo do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10) % 11
    digito2 = 0 if digito2 > 9 else digito2
    # Verifica os dígitos
    if cpf[-2:] != f"{digito1}{digito2}":
        return False, "CPF inválido"
    return True, ""

def validar_senha(senha):
    """Valida o campo Senha"""
    if len(senha) < 8:
        return False, "A senha deve ter pelo menos 8 caracteres"
    return True, ""
