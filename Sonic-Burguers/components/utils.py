from validate_docbr import CPF

def validar_e_formatar_cpf(cpf):
    cpf_validator = CPF()
    cpf_limpo = ''.join(filter(str.isdigit, cpf))  # Remove caracteres não numéricos
    
    # Aplica a máscara se tiver 11 dígitos, senão retorna o valor limpo
    cpf_mascarado = cpf_validator.mask(cpf_limpo) if len(cpf_limpo) == 11 else cpf_limpo
    
    # Verifica se o CPF é válido
    if cpf_validator.validate(cpf_limpo):
        return True, cpf_mascarado  # CPF válido
    return False, cpf_mascarado  # CPF inválido