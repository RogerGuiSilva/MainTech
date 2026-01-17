from app.falhas import lista_falha

lista_falha(falhas)

falhas = [
    {
        "descricao": "Vazamento de óleo no circuito hidráulico",
        "tipo": "Mecânica",
        "gravidade": "Alta",
        "data_ocorrencia": "2025-01-05",
        "status": "Aberta",
        "maquina_id": 1
    },
    {
        "descricao": "Falha no sensor de pressão do molde",
        "tipo": "Elétrica",
        "gravidade": "Média",
        "data_ocorrencia": "2025-01-06",
        "status": "Em Análise",
        "maquina_id": 2
    },
    {
        "descricao": "Ruído excessivo no conjunto de fechamento",
        "tipo": "Mecânica",
        "gravidade": "Alta",
        "data_ocorrencia": "2025-01-04",
        "status": "Em Manutenção",
        "maquina_id": 3
    },
    {
        "descricao": "Desalinhamento do fuso da extrusora",
        "tipo": "Mecânica",
        "gravidade": "Alta",
        "data_ocorrencia": "2025-01-03",
        "status": "Aberta",
        "maquina_id": 4
    },
    {
        "descricao": "Sobreaquecimento do motor principal",
        "tipo": "Elétrica",
        "gravidade": "Crítica",
        "data_ocorrencia": "2025-01-07",
        "status": "Parada",
        "maquina_id": 5
    },
    {
        "descricao": "Falha de comunicação entre inversor e CLP",
        "tipo": "Automação",
        "gravidade": "Crítica",
        "data_ocorrencia": "2025-01-08",
        "status": "Parada",
        "maquina_id": 6
    },
    {
        "descricao": "Erro de referência no eixo X",
        "tipo": "CNC",
        "gravidade": "Média",
        "data_ocorrencia": "2025-01-02",
        "status": "Aberta",
        "maquina_id": 7
    },
    {
        "descricao": "Desgaste excessivo na ferramenta",
        "tipo": "Processo",
        "gravidade": "Baixa",
        "data_ocorrencia": "2025-01-01",
        "status": "Planejada",
        "maquina_id": 8
    },
    {
        "descricao": "Perda de precisão nos movimentos simultâneos",
        "tipo": "CNC",
        "gravidade": "Alta",
        "data_ocorrencia": "2025-01-06",
        "status": "Em Análise",
        "maquina_id": 9
    },
    {
        "descricao": "Folga mecânica no eixo principal",
        "tipo": "Mecânica",
        "gravidade": "Média",
        "data_ocorrencia": "2025-01-04",
        "status": "Aberta",
        "maquina_id": 10
    },

        {
        "descricao": "Falha no relé de segurança",
        "tipo": "Elétrica",
        "gravidade": "Crítica",
        "data_ocorrencia": "2025-01-09",
        "status": "Parada",
        "maquina_id": 11
    },
    {
        "descricao": "Sensor de fim de curso danificado",
        "tipo": "Automação",
        "gravidade": "Média",
        "data_ocorrencia": "2025-01-10",
        "status": "Aberta",
        "maquina_id": 12
    },
    {
        "descricao": "Correia de transmissão desgastada",
        "tipo": "Mecânica",
        "gravidade": "Baixa",
        "data_ocorrencia": "2025-01-11",
        "status": "Planejada",
        "maquina_id": 13
    },
    {
        "descricao": "Oscilação de tensão na alimentação",
        "tipo": "Elétrica",
        "gravidade": "Alta",
        "data_ocorrencia": "2025-01-12",
        "status": "Em Análise",
        "maquina_id": 14
    },
    {
        "descricao": "Falha no encoder do eixo Y",
        "tipo": "CNC",
        "gravidade": "Alta",
        "data_ocorrencia": "2025-01-13",
        "status": "Aberta",
        "maquina_id": 15
    },
    {
        "descricao": "Desbalanceamento do eixo rotativo",
        "tipo": "Mecânica",
        "gravidade": "Média",
        "data_ocorrencia": "2025-01-14",
        "status": "Em Manutenção",
        "maquina_id": 16
    },
    {
        "descricao": "Erro de parametrização no CLP",
        "tipo": "Automação",
        "gravidade": "Média",
        "data_ocorrencia": "2025-01-15",
        "status": "Aberta",
        "maquina_id": 17
    },
    {
        "descricao": "Travamento intermitente do pistão hidráulico",
        "tipo": "Hidráulica",
        "gravidade": "Alta",
        "data_ocorrencia": "2025-01-16",
        "status": "Em Análise",
        "maquina_id": 18
    },
    {
        "descricao": "Válvula proporcional com resposta lenta",
        "tipo": "Hidráulica",
        "gravidade": "Média",
        "data_ocorrencia": "2025-01-17",
        "status": "Aberta",
        "maquina_id": 19
    },
    {
        "descricao": "Falha no sistema de refrigeração",
        "tipo": "Mecânica",
        "gravidade": "Crítica",
        "data_ocorrencia": "2025-01-18",
        "status": "Parada",
        "maquina_id": 20
    },
    {
        "descricao": "Erro de sincronismo entre eixos",
        "tipo": "CNC",
        "gravidade": "Alta",
        "data_ocorrencia": "2025-01-19",
        "status": "Em Análise",
        "maquina_id": 21
    },
    {
        "descricao": "Contaminação do óleo hidráulico",
        "tipo": "Hidráulica",
        "gravidade": "Alta",
        "data_ocorrencia": "2025-01-20",
        "status": "Aberta",
        "maquina_id": 22
    },
    {
        "descricao": "Falha no botão de emergência",
        "tipo": "Segurança",
        "gravidade": "Crítica",
        "data_ocorrencia": "2025-01-21",
        "status": "Parada",
        "maquina_id": 23
    },
    {
        "descricao": "Atraso na resposta do servomotor",
        "tipo": "Automação",
        "gravidade": "Média",
        "data_ocorrencia": "2025-01-22",
        "status": "Aberta",
        "maquina_id": 24
    },
    {
        "descricao": "Desgaste no rolamento principal",
        "tipo": "Mecânica",
        "gravidade": "Alta",
        "data_ocorrencia": "2025-01-23",
        "status": "Em Manutenção",
        "maquina_id": 25
    },
    {
        "descricao": "Falha no ventilador do painel elétrico",
        "tipo": "Elétrica",
        "gravidade": "Média",
        "data_ocorrencia": "2025-01-24",
        "status": "Aberta",
        "maquina_id": 26
    },
    {
        "descricao": "Erro de leitura no sensor óptico",
        "tipo": "Automação",
        "gravidade": "Baixa",
        "data_ocorrencia": "2025-01-25",
        "status": "Planejada",
        "maquina_id": 27
    },
    {
        "descricao": "Perda de torque no motor secundário",
        "tipo": "Elétrica",
        "gravidade": "Alta",
        "data_ocorrencia": "2025-01-26",
        "status": "Em Análise",
        "maquina_id": 28
    },
    {
        "descricao": "Falha intermitente no inversor de frequência",
        "tipo": "Automação",
        "gravidade": "Alta",
        "data_ocorrencia": "2025-01-27",
        "status": "Aberta",
        "maquina_id": 29
    },
    {
        "descricao": "Desgaste irregular da correia dentada",
        "tipo": "Mecânica",
        "gravidade": "Baixa",
        "data_ocorrencia": "2025-01-28",
        "status": "Planejada",
        "maquina_id": 30
    },
    {
        "descricao": "Falha no aterramento do painel",
        "tipo": "Elétrica",
        "gravidade": "Crítica",
        "data_ocorrencia": "2025-01-29",
        "status": "Parada",
        "maquina_id": 31
    },
    {
        "descricao": "Erro de calibração do eixo Z",
        "tipo": "CNC",
        "gravidade": "Média",
        "data_ocorrencia": "2025-01-30",
        "status": "Aberta",
        "maquina_id": 32
    },
    {
        "descricao": "Falha no sistema pneumático",
        "tipo": "Pneumática",
        "gravidade": "Alta",
        "data_ocorrencia": "2025-01-31",
        "status": "Em Análise",
        "maquina_id": 33
    },
    {
        "descricao": "Vazamento de ar comprimido",
        "tipo": "Pneumática",
        "gravidade": "Baixa",
        "data_ocorrencia": "2025-02-01",
        "status": "Planejada",
        "maquina_id": 34
    },
    {
        "descricao": "Falha no pressostato",
        "tipo": "Pneumática",
        "gravidade": "Média",
        "data_ocorrencia": "2025-02-02",
        "status": "Aberta",
        "maquina_id": 35
    },
    {
        "descricao": "Erro de comunicação com supervisório",
        "tipo": "Automação",
        "gravidade": "Alta",
        "data_ocorrencia": "2025-02-03",
        "status": "Em Análise",
        "maquina_id": 36
    },
    {
        "descricao": "Falha geral por sobrecarga do sistema",
        "tipo": "Sistema",
        "gravidade": "Crítica",
        "data_ocorrencia": "2025-02-04",
        "status": "Parada",
        "maquina_id": 37
    }
]

    


