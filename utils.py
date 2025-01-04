def gerar_horarios():
    horarios = []
    for hora in range(7, 20, 2):  # Incremento de 2 em 2 horas
        horarios.append(f"{hora:02d}:00")
    return horarios
