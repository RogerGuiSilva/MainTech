# app/equipamentos.py
from app.dataBase.db import get_connection

def inserir_equipamentos():
    equipamentos = [
  {"nome":"Chave de Fenda Isolada","setor":"Manutenção","tipo":"Ferramenta","status":"Disponível"},
  {"nome":"Chave Phillips Isolada","setor":"Manutenção","tipo":"Ferramenta","status":"Disponível"},
  {"nome":"Chave Torx","setor":"Manutenção","tipo":"Ferramenta","status":"Disponível"},
  {"nome":"Chave Combinada","setor":"Manutenção","tipo":"Ferramenta","status":"Disponível"},
  {"nome":"Chave Allen","setor":"Manutenção","tipo":"Ferramenta","status":"Disponível"},
  {"nome":"Chave Ajustável","setor":"Manutenção","tipo":"Ferramenta","status":"Disponível"},
  {"nome":"Martelo de Aço","setor":"Manutenção","tipo":"Ferramenta","status":"Disponível"},
  {"nome":"Martelo de Borracha","setor":"Manutenção","tipo":"Ferramenta","status":"Disponível"},
  {"nome":"Alicate Universal","setor":"Manutenção","tipo":"Ferramenta","status":"Disponível"},
  {"nome":"Alicate de Corte","setor":"Manutenção","tipo":"Ferramenta","status":"Disponível"},
  {"nome":"Alicate de Ponta","setor":"Manutenção","tipo":"Ferramenta","status":"Disponível"},
  {"nome":"Alicate Crimpador","setor":"Elétrica","tipo":"Ferramenta","status":"Disponível"},
  {"nome":"Serra Copo","setor":"Manutenção","tipo":"Ferramenta","status":"Disponível"},
  {"nome":"Lima Manual","setor":"Manutenção","tipo":"Ferramenta","status":"Disponível"},
  {"nome":"Soprador Térmico","setor":"Manutenção","tipo":"Ferramenta","status":"Disponível"},
  
  {"nome":"Furadeira Elétrica","setor":"Manutenção","tipo":"Ferramenta","status":"Disponível"},
  {"nome":"Parafusadeira Elétrica","setor":"Manutenção","tipo":"Ferramenta","status":"Disponível"},
  {"nome":"Chave de Impacto","setor":"Manutenção","tipo":"Ferramenta","status":"Disponível"},
  {"nome":"Esmerilhadeira","setor":"Manutenção","tipo":"Ferramenta","status":"Disponível"},
  {"nome":"Serra Mármore","setor":"Manutenção","tipo":"Ferramenta","status":"Disponível"},

  {"nome":"Multímetro Digital","setor":"Elétrica","tipo":"Instrumento de Medição","status":"Disponível"},
  {"nome":"Alicate Amperímetro","setor":"Elétrica","tipo":"Instrumento de Medição","status":"Disponível"},
  {"nome":"Detector de Tensão","setor":"Elétrica","tipo":"Instrumento de Medição","status":"Disponível"},
  {"nome":"Megômetro","setor":"Elétrica","tipo":"Instrumento de Medição","status":"Disponível"},
  {"nome":"Testador de Continuidade","setor":"Elétrica","tipo":"Instrumento de Medição","status":"Disponível"},
  {"nome":"Osciloscópio","setor":"Elétrica","tipo":"Instrumento de Medição","status":"Disponível"},
  {"nome":"Medidor de Temperatura","setor":"Elétrica","tipo":"Instrumento de Medição","status":"Disponível"},

  {"nome":"Fonte de Alimentação Ajustável","setor":"Elétrica","tipo":"Equipamento","status":"Disponível"},
  {"nome":"Estabilizador","setor":"Elétrica","tipo":"Equipamento","status":"Disponível"},
  {"nome":"Nobreak","setor":"Elétrica","tipo":"Equipamento","status":"Disponível"},
  {"nome":"Extensão Elétrica","setor":"Manutenção","tipo":"Equipamento","status":"Disponível"},
  {"nome":"Fita Isolante","setor":"Elétrica","tipo":"Equipamento","status":"Disponível"},
  {"nome":"Luvas Isolantes","setor":"Elétrica","tipo":"Equipamento","status":"Disponível"},
  {"nome":"Suporte de Ferramentas","setor":"Manutenção","tipo":"Equipamento","status":"Disponível"}
]
    conn = get_connection()
    cursor = conn.cursor()

    for eq in equipamentos:
        cursor.execute("""
            INSERT INTO equipamentos (nome, setor, tipo, status)
            VALUES (?, ?, ?, ?)
        """, (eq["nome"], eq["setor"], eq["tipo"], eq["status"]))

    conn.commit()
    conn.close()
    print("ok, equipamentos e ferramentas inseridos")




