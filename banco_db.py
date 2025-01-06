import sqlite3
import datetime

def create_db():
    conn = sqlite3.connect("agendamentos.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS agendamentos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        sobrenome TEXT,
                        telefone TEXT,
                        servico TEXT,
                        data_agendamento TEXT,
                        horario TEXT,
                        data_registro TEXT
                    )''')
    conn.commit()
    conn.close()

def save_agendamento(nome, sobrenome, telefone, servico, data_agendamento, horario):
    conn = sqlite3.connect("agendamentos.db")
    cursor = conn.cursor()
    data_registro = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''INSERT INTO agendamentos (nome, sobrenome, telefone, servico, data_agendamento, horario, data_registro) 
                      VALUES (?, ?, ?, ?, ?, ?, ?)''', 
                   (nome, sobrenome, telefone, servico, data_agendamento, horario, data_registro))
    conn.commit()
    conn.close()

def delete_agendamento(id_agendamento):
    conn = sqlite3.connect("agendamentos.db")
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM agendamentos WHERE id = ?''', (id_agendamento,))
    conn.commit()
    conn.close()

def buscar_agendamentos():
    conn = sqlite3.connect("agendamentos.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM agendamentos')
    agendamentos = cursor.fetchall()
    conn.close()
    return agendamentos

# Função para buscar agendamentos pelo nome
def buscar_agendamentos_nome(nome):
    conn = sqlite3.connect("agendamentos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM agendamentos WHERE nome LIKE ?", ('%' + nome + '%',))
    agendamentos = cursor.fetchall()
    conn.close()
    return agendamentos

def atualizar_tabela_por_data(data_selecionada):
    # Consulta os registros no banco de dados para a data selecionada
    conn = sqlite3.connect("agendamentos.db")
    cursor = conn.cursor()
    cursor.execute("""
            SELECT id, nome, sobrenome, telefone, servico, data_agendamento, horario 
            FROM agendamentos 
            WHERE data_agendamento = ?
        """, (data_selecionada,))
    agendamentos = cursor.fetchall()
    conn.close()
    return agendamentos