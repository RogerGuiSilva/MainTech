# app/seed_falhas.py
from app.falhas import inserir_falha
from app.dataBase.db import get_connection

def tabela_tem_dados(nome_tabela: str) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {nome_tabela}")
    qtd = cursor.fetchone()[0]
    conn.close()
    return qtd > 0

def seed_falhas():
    if tabela_tem_dados("falhas"):
        print("Seed ignorado: tabela 'falhas' já tem dados.")
        return
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM maquinas")
    qtd_maquinas = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM equipamentos")
    qtd_equipamentos = cursor.fetchone()[0]

    conn.close()

    if qtd_maquinas == 0:
        print("ERRO: Não Existe Máquinas no Banco")
        return

    if qtd_equipamentos == 0:
        print("ERRO: Não existe Equipamentos no Banco")
        return

    
    falhas = [

        {
    "descricao": "Vazamento de óleo no circuito hidráulico",
    "tipo": "Mecânica",
    "gravidade": "Alta",
    "data_ocorrencia": "2025-01-05",
    "status": "ABERTA",
    "maquina_id": 1
},
{
    "descricao": "Falha no sensor de pressão do molde",
    "tipo": "Elétrica",
    "gravidade": "Média",
    "data_ocorrencia": "2025-01-06",
    "status": "EM_ANALISE",
    "maquina_id": 2
},
{
    "descricao": "Ruído excessivo no conjunto de fechamento",
    "tipo": "Mecânica",
    "gravidade": "Alta",
    "data_ocorrencia": "2025-01-04",
    "status": "EM_MANUTENCAO",
    "maquina_id": 3
},
{
    "descricao": "Desalinhamento do fuso da extrusora",
    "tipo": "Mecânica",
    "gravidade": "Alta",
    "data_ocorrencia": "2025-01-03",
    "status": "ABERTA",
    "maquina_id": 4
},
{
    "descricao": "Sobreaquecimento do motor principal",
    "tipo": "Elétrica",
    "gravidade": "Crítica",
    "data_ocorrencia": "2025-01-07",
    "status": "PARADA",
    "maquina_id": 5
},
{
    "descricao": "Falha de comunicação entre inversor e CLP",
    "tipo": "Automação",
    "gravidade": "Crítica",
    "data_ocorrencia": "2025-01-08",
    "status": "PARADA",
    "maquina_id": 6
},
{
    "descricao": "Erro de referência no eixo X",
    "tipo": "CNC",
    "gravidade": "Média",
    "data_ocorrencia": "2025-01-02",
    "status": "ABERTA",
    "maquina_id": 7
},
{
    "descricao": "Desgaste excessivo na ferramenta",
    "tipo": "Processo",
    "gravidade": "Baixa",
    "data_ocorrencia": "2025-01-01",
    "status": "PLANEJADA",
    "maquina_id": 8
},
{
    "descricao": "Perda de precisão nos movimentos simultâneos",
    "tipo": "CNC",
    "gravidade": "Alta",
    "data_ocorrencia": "2025-01-06",
    "status": "EM_ANALISE",
    "maquina_id": 9
},
{
    "descricao": "Folga mecânica no eixo principal",
    "tipo": "Mecânica",
    "gravidade": "Média",
    "data_ocorrencia": "2025-01-04",
    "status": "ABERTA",
    "maquina_id": 10
},
{
    "descricao": "Falha no relé de segurança",
    "tipo": "Elétrica",
    "gravidade": "Crítica",
    "data_ocorrencia": "2025-01-09",
    "status": "PARADA",
    "maquina_id": 11
},
{
    "descricao": "Sensor de fim de curso danificado",
    "tipo": "Automação",
    "gravidade": "Média",
    "data_ocorrencia": "2025-01-10",
    "status": "ABERTA",
    "maquina_id": 12
},
{
    "descricao": "Correia de transmissão desgastada",
    "tipo": "Mecânica",
    "gravidade": "Baixa",
    "data_ocorrencia": "2025-01-11",
    "status": "PLANEJADA",
    "maquina_id": 13
},
{
    "descricao": "Oscilação de tensão na alimentação",
    "tipo": "Elétrica",
    "gravidade": "Alta",
    "data_ocorrencia": "2025-01-12",
    "status": "EM_ANALISE",
    "maquina_id": 14
},
{
    "descricao": "Falha no encoder do eixo Y",
    "tipo": "CNC",
    "gravidade": "Alta",
    "data_ocorrencia": "2025-01-13",
    "status": "ABERTA",
    "maquina_id": 15
},
{
    "descricao": "Desbalanceamento do eixo rotativo",
    "tipo": "Mecânica",
    "gravidade": "Média",
    "data_ocorrencia": "2025-01-14",
    "status": "EM_MANUTENCAO",
    "maquina_id": 16
},
{
    "descricao": "Erro de parametrização no CLP",
    "tipo": "Automação",
    "gravidade": "Média",
    "data_ocorrencia": "2025-01-15",
    "status": "ABERTA",
    "maquina_id": 17
},
{
    "descricao": "Travamento intermitente do pistão hidráulico",
    "tipo": "Hidráulica",
    "gravidade": "Alta",
    "data_ocorrencia": "2025-01-16",
    "status": "EM_ANALISE",
    "maquina_id": 18
},
{
    "descricao": "Válvula proporcional com resposta lenta",
    "tipo": "Hidráulica",
    "gravidade": "Média",
    "data_ocorrencia": "2025-01-17",
    "status": "ABERTA",
    "maquina_id": 19
},
{
    "descricao": "Falha no sistema de refrigeração",
    "tipo": "Mecânica",
    "gravidade": "Crítica",
    "data_ocorrencia": "2025-01-18",
    "status": "PARADA",
    "maquina_id": 20
},
{
    "descricao": "Erro de sincronismo entre eixos",
    "tipo": "CNC",
    "gravidade": "Alta",
    "data_ocorrencia": "2025-01-19",
    "status": "EM_ANALISE",
    "maquina_id": 21
},
{
    "descricao": "Contaminação do óleo hidráulico",
    "tipo": "Hidráulica",
    "gravidade": "Alta",
    "data_ocorrencia": "2025-01-20",
    "status": "ABERTA",
    "maquina_id": 22
},
{
    "descricao": "Falha no botão de emergência",
    "tipo": "Segurança",
    "gravidade": "Crítica",
    "data_ocorrencia": "2025-01-21",
    "status": "PARADA",
    "maquina_id": 23
},
{
    "descricao": "Atraso na resposta do servomotor",
    "tipo": "Automação",
    "gravidade": "Média",
    "data_ocorrencia": "2025-01-22",
    "status": "ABERTA",
    "maquina_id": 24
},
{
    "descricao": "Desgaste no rolamento principal",
    "tipo": "Mecânica",
    "gravidade": "Alta",
    "data_ocorrencia": "2025-01-23",
    "status": "EM_MANUTENCAO",
    "maquina_id": 25
},
{
    "descricao": "Falha no ventilador do painel elétrico",
    "tipo": "Elétrica",
    "gravidade": "Média",
    "data_ocorrencia": "2025-01-24",
    "status": "ABERTA",
    "maquina_id": 26
},
{
    "descricao": "Erro de leitura no sensor óptico",
    "tipo": "Automação",
    "gravidade": "Baixa",
    "data_ocorrencia": "2025-01-25",
    "status": "PLANEJADA",
    "maquina_id": 27
},
{
    "descricao": "Perda de torque no motor secundário",
    "tipo": "Elétrica",
    "gravidade": "Alta",
    "data_ocorrencia": "2025-01-26",
    "status": "EM_ANALISE",
    "maquina_id": 28
},
{
    "descricao": "Falha intermitente no inversor de frequência",
    "tipo": "Automação",
    "gravidade": "Alta",
    "data_ocorrencia": "2025-01-27",
    "status": "ABERTA",
    "maquina_id": 29
},
{
    "descricao": "Desgaste irregular da correia dentada",
    "tipo": "Mecânica",
    "gravidade": "Baixa",
    "data_ocorrencia": "2025-01-28",
    "status": "PLANEJADA",
    "maquina_id": 30
},
{
    "descricao": "Falha no aterramento do painel",
    "tipo": "Elétrica",
    "gravidade": "Crítica",
    "data_ocorrencia": "2025-01-29",
    "status": "PARADA",
    "maquina_id": 31
},
{
    "descricao": "Erro de calibração do eixo Z",
    "tipo": "CNC",
    "gravidade": "Média",
    "data_ocorrencia": "2025-01-30",
    "status": "ABERTA",
    "maquina_id": 32
},
{
    "descricao": "Falha no sistema pneumático",
    "tipo": "Pneumática",
    "gravidade": "Alta",
    "data_ocorrencia": "2025-01-31",
    "status": "EM_ANALISE",
    "maquina_id": 33
},
{
    "descricao": "Vazamento de ar comprimido",
    "tipo": "Pneumática",
    "gravidade": "Baixa",
    "data_ocorrencia": "2025-02-01",
    "status": "PLANEJADA",
    "maquina_id": 34
},
{
    "descricao": "Falha no pressostato",
    "tipo": "Pneumática",
    "gravidade": "Média",
    "data_ocorrencia": "2025-02-02",
    "status": "ABERTA",
    "maquina_id": 35
},
{
    "descricao": "Erro de comunicação com supervisório",
    "tipo": "Automação",
    "gravidade": "Alta",
    "data_ocorrencia": "2025-02-03",
    "status": "EM_ANALISE",
    "maquina_id": 36
},
{
    "descricao": "Falha geral por sobrecarga do sistema",
    "tipo": "Sistema",
    "gravidade": "Crítica",
    "data_ocorrencia": "2025-02-04",
    "status": "PARADA",
    "maquina_id": 37
},
{
    "descricao": "Ponta gasta e escorregando no parafuso, risco de espanar.",
    "tipo": "Desgaste",
    "gravidade": "Média",
    "data_ocorrencia": "2026-01-10",
    "status": "ABERTA",
    "equipamento_id": 1
},
{
    "descricao": "Isolação marcada e cabo com folga, comprometendo a segurança.",
    "tipo": "Segurança",
    "gravidade": "Alta",
    "data_ocorrencia": "2026-01-12",
    "status": "EM_ATENDIMENTO",
    "equipamento_id": 2
},
{
    "descricao": "Ponta Torx arredondada, parafuso patinando.",
    "tipo": "Desgaste",
    "gravidade": "Média",
    "data_ocorrencia": "2026-01-09",
    "status": "ABERTA",
    "equipamento_id": 3
},
{
    "descricao": "Oxidação e folga na chave, perda de torque.",
    "tipo": "Mecânica",
    "gravidade": "Baixa",
    "data_ocorrencia": "2026-01-08",
    "status": "RESOLVIDA",
    "equipamento_id": 4
},
{
    "descricao": "Ponta deformada, não encaixa totalmente no parafuso.",
    "tipo": "Desgaste",
    "gravidade": "Baixa",
    "data_ocorrencia": "2026-01-07",
    "status": "EM_ATENDIMENTO",
    "equipamento_id": 5
},
{
    "descricao": "Mecanismo de ajuste travando durante o uso.",
    "tipo": "Mecânica",
    "gravidade": "Média",
    "data_ocorrencia": "2026-01-11",
    "status": "ABERTA",
    "equipamento_id": 6
},
{
    "descricao": "Cabo solto e vibração excessiva em impacto.",
    "tipo": "Mecânica",
    "gravidade": "Média",
    "data_ocorrencia": "2026-01-06",
    "status": "ABERTA",
    "equipamento_id": 7
},
{
    "descricao": "Cabeça com fissura, risco de ruptura durante impacto.",
    "tipo": "Segurança",
    "gravidade": "Alta",
    "data_ocorrencia": "2026-01-14",
    "status": "ABERTA",
    "equipamento_id": 8
},
{
    "descricao": "Mandíbulas desalinhadas, escorregando ao apertar.",
    "tipo": "Mecânica",
    "gravidade": "Baixa",
    "data_ocorrencia": "2026-01-05",
    "status": "RESOLVIDA",
    "equipamento_id": 9
},
{
    "descricao": "Perda de fio no corte, desempenho abaixo do esperado.",
    "tipo": "Desgaste",
    "gravidade": "Média",
    "data_ocorrencia": "2026-01-10",
    "status": "ABERTA",
    "equipamento_id": 10
},
{
    "descricao": "Mola fraca e ponta não fecha totalmente.",
    "tipo": "Mecânica",
    "gravidade": "Baixa",
    "data_ocorrencia": "2026-01-04",
    "status": "EM_ATENDIMENTO",
    "equipamento_id": 11
},
{
    "descricao": "Crimpagem fora do padrão gerando mau contato.",
    "tipo": "Qualidade",
    "gravidade": "Alta",
    "data_ocorrencia": "2026-01-15",
    "status": "ABERTA",
    "equipamento_id": 12
},
{
    "descricao": "Serra copo empenada, vibração excessiva no corte.",
    "tipo": "Mecânica",
    "gravidade": "Média",
    "data_ocorrencia": "2026-01-12",
    "status": "ABERTA",
    "equipamento_id": 13
},
{
    "descricao": "Dentes cegos, baixa remoção de material.",
    "tipo": "Desgaste",
    "gravidade": "Baixa",
    "data_ocorrencia": "2026-01-03",
    "status": "RESOLVIDA",
    "equipamento_id": 14
},
{
    "descricao": "Superaquecimento após uso contínuo.",
    "tipo": "Elétrica",
    "gravidade": "Alta",
    "data_ocorrencia": "2026-01-16",
    "status": "EM_ATENDIMENTO",
    "equipamento_id": 15
},
{
    "descricao": "Mandril com folga, broca patina durante perfuração.",
    "tipo": "Mecânica",
    "gravidade": "Média",
    "data_ocorrencia": "2026-01-09",
    "status": "ABERTA",
    "equipamento_id": 16
},
{
    "descricao": "Bateria não segura carga e torque reduzido.",
    "tipo": "Energia",
    "gravidade": "Média",
    "data_ocorrencia": "2026-01-13",
    "status": "ABERTA",
    "equipamento_id": 17
},
{
    "descricao": "Ruído metálico e aquecimento excessivo.",
    "tipo": "Mecânica",
    "gravidade": "Alta",
    "data_ocorrencia": "2026-01-14",
    "status": "ABERTA",
    "equipamento_id": 18
},
{
    "descricao": "Faíscas excessivas e perda de rotação.",
    "tipo": "Elétrica",
    "gravidade": "Crítica",
    "data_ocorrencia": "2026-01-16",
    "status": "ABERTA",
    "equipamento_id": 19
},
{
    "descricao": "Cabo com microcortes e aquecimento no gatilho.",
    "tipo": "Segurança",
    "gravidade": "Crítica",
    "data_ocorrencia": "2026-01-15",
    "status": "ABERTA",
    "equipamento_id": 20
},
{
    "descricao": "Leituras instáveis em tensão AC.",
    "tipo": "Calibração",
    "gravidade": "Alta",
    "data_ocorrencia": "2026-01-12",
    "status": "EM_ATENDIMENTO",
    "equipamento_id": 21
},
{
    "descricao": "Medição de corrente com erro de offset.",
    "tipo": "Calibração",
    "gravidade": "Alta",
    "data_ocorrencia": "2026-01-11",
    "status": "ABERTA",
    "equipamento_id": 22
},
{
    "descricao": "Falsos positivos próximos a motores.",
    "tipo": "Calibração",
    "gravidade": "Média",
    "data_ocorrencia": "2026-01-10",
    "status": "ABERTA",
    "equipamento_id": 23
},
{
    "descricao": "Não atinge tensão de teste especificada.",
    "tipo": "Elétrica",
    "gravidade": "Crítica",
    "data_ocorrencia": "2026-01-16",
    "status": "ABERTA",
    "equipamento_id": 24
},
{
    "descricao": "Bip intermitente mesmo com circuito aberto.",
    "tipo": "Eletrônica",
    "gravidade": "Média",
    "data_ocorrencia": "2026-01-08",
    "status": "RESOLVIDA",
    "equipamento_id": 25
},
{
    "descricao": "Canal sem sinal e ruído elevado.",
    "tipo": "Eletrônica",
    "gravidade": "Alta",
    "data_ocorrencia": "2026-01-14",
    "status": "EM_ATENDIMENTO",
    "equipamento_id": 26
},
{
    "descricao": "Sensor demora estabilizar e indica valor incorreto.",
    "tipo": "Calibração",
    "gravidade": "Média",
    "data_ocorrencia": "2026-01-09",
    "status": "ABERTA",
    "equipamento_id": 27
},
{
    "descricao": "Saída oscilando sob carga.",
    "tipo": "Elétrica",
    "gravidade": "Alta",
    "data_ocorrencia": "2026-01-13",
    "status": "ABERTA",
    "equipamento_id": 28
},
{
    "descricao": "Aquecimento excessivo e cheiro de verniz.",
    "tipo": "Elétrica",
    "gravidade": "Crítica",
    "data_ocorrencia": "2026-01-15",
    "status": "ABERTA",
    "equipamento_id": 29
},
{
    "descricao": "Autonomia muito abaixo do esperado.",
    "tipo": "Energia",
    "gravidade": "Alta",
    "data_ocorrencia": "2026-01-12",
    "status": "EM_ATENDIMENTO",
    "equipamento_id": 30
},
{
    "descricao": "Mau contato no plug e aquecimento.",
    "tipo": "Segurança",
    "gravidade": "Crítica",
    "data_ocorrencia": "2026-01-16",
    "status": "ABERTA",
    "equipamento_id": 31
},
{
    "descricao": "Fita ressecada e descolando.",
    "tipo": "Qualidade",
    "gravidade": "Média",
    "data_ocorrencia": "2026-01-07",
    "status": "RESOLVIDA",
    "equipamento_id": 32
},
{
    "descricao": "Microfuros e perda de rigidez dielétrica.",
    "tipo": "Segurança",
    "gravidade": "Crítica",
    "data_ocorrencia": "2026-01-14",
    "status": "ABERTA",
    "equipamento_id": 33
},
{
    "descricao": "Travas quebradas e ferramentas caindo no transporte.",
    "tipo": "Mecânica",
    "gravidade": "Média",
    "data_ocorrencia": "2026-01-10",
    "status": "EM_ATENDIMENTO",
    "equipamento_id": 34
}

   

]

    for f in falhas:
        resp = inserir_falha(**f)
        if str(resp).startswith("Erro"):
            print("erro", resp)

    print("Seed de falhas concluído.")

if __name__ == "__main__":
    seed_falhas()
