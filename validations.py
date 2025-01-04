def validar_campos(nome, sobrenome, telefone, servico, data_agendamento, horario):
    erros = []

    if not nome.strip():
        erros.append("O campo 'Nome' não pode estar vazio.")
    if not sobrenome.strip():
        erros.append("O campo 'Sobrenome' não pode estar vazio.")
    if not telefone.strip() or not telefone.isdigit() or len(telefone) < 9:
        erros.append("O campo 'Telefone' deve conter apenas números e ter pelo menos 8 dígitos.")
    if not servico:
        erros.append("Você deve selecionar um serviço.")
    if data_agendamento == "Agendar Data":
        erros.append("Você deve selecionar uma data de agendamento.")
    if not horario:
        erros.append("Você deve selecionar um horário.")

    return erros
