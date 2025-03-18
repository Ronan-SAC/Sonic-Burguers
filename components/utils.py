from validate_docbr import CPF

def validar_e_formatar_cpf(cpf):
    cpf_validator = CPF()
    cpf_limpo = ''.join(filter(str.isdigit, cpf))     
    cpf_mascarado = cpf_validator.mask(cpf_limpo) if len(cpf_limpo) == 11 else cpf_limpo
    if cpf_validator.validate(cpf_limpo):
        return True, cpf_mascarado 
    return False, cpf_mascarado  

def formatar_telefone(telefone):
    apenas_digitos = ''.join(filter(str.isdigit, telefone))
    if len(apenas_digitos) < 10:
        return False, apenas_digitos

    if len(apenas_digitos) == 10:  
        telefone_formatado = f"({apenas_digitos[0:2]}) {apenas_digitos[2:6]}-{apenas_digitos[6:10]}"
    elif len(apenas_digitos) == 11:  
        telefone_formatado = f"({apenas_digitos[0:2]}) {apenas_digitos[2:7]}-{apenas_digitos[7:11]}"
    else:
        return False, apenas_digitos
    
    return True, telefone_formatado

