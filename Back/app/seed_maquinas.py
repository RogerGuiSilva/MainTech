
from app.maquinas import inserir_maquina
from app.dataBase.db import get_connection

def tabela_tem_dados(nome_tabela: str) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {nome_tabela}")
    qtd = cursor.fetchone()[0]
    conn.close()
    return qtd > 0

def seed_maquinas():
    
    if tabela_tem_dados("maquinas"):
        print("já tem dados.")
        return

    maquinas = [
        {"nome":"Injetora Plástica 120T","setor":"Injeção","tipo":"Máquina","status":"Disponível"},
        {"nome":"Injetora Plástica 300T","setor":"Injeção","tipo":"Máquina","status":"Disponível"},
        {"nome":"Injetora Plástica 500T","setor":"Injeção","tipo":"Máquina","status":"Manutenção"},
        {"nome":"Extrusora de Filme 75mm","setor":"Extrusão","tipo":"Máquina","status":"Disponível"},
        {"nome":"Extrusora Monoscrew 90mm","setor":"Extrusão","tipo":"Máquina","status":"Disponível"},
        {"nome":"Extrusora Duplo Parafuso 120mm","setor":"Extrusão","tipo":"Máquina","status":"Em Uso"},
        {"nome":"Torno CNC Ø500","setor":"Usinagem","tipo":"Máquina","status":"Disponível"},
        {"nome":"Centro de Usinagem 3 Eixos","setor":"Usinagem","tipo":"Máquina","status":"Disponível"},
        {"nome":"Centro de Usinagem 5 Eixos","setor":"Usinagem","tipo":"Máquina","status":"Em Uso"},
        {"nome":"Fresadora Universal","setor":"Usinagem","tipo":"Máquina","status":"Disponível"},
        {"nome":"Retífica Cilíndrica","setor":"Usinagem","tipo":"Máquina","status":"Manutenção"},
        {"nome":"Robot Paletizador 6 Eixos","setor":"Automação","tipo":"Sistema","status":"Disponível"},
        {"nome":"Linha Automática de Montagem","setor":"Automação","tipo":"Sistema","status":"Em Uso"},
        {"nome":"Estação de Visão Industrial","setor":"Automação","tipo":"Equipamento","status":"Disponível"},
        {"nome":"Transportador de Correia 10m","setor":"Movimentação","tipo":"Equipamento","status":"Disponível"},
        {"nome":"Empilhadeira Elétrica 2T","setor":"Movimentação","tipo":"Veículo","status":"Disponível"},
        {"nome":"Pórtico Giratório 180°","setor":"Movimentação","tipo":"Equipamento","status":"Em Uso"},
        {"nome":"Guindaste Monoviga 5T","setor":"Movimentação","tipo":"Equipamento","status":"Manutenção"},
        {"nome":"Prensa Hidráulica 200T","setor":"Usinagem","tipo":"Máquina","status":"Disponível"},
        {"nome":"Calandra de Laminação 3 Rolos","setor":"Usinagem","tipo":"Máquina","status":"Disponível"},
        {"nome":"Sopradora de Garrafas 4 Cabeças","setor":"Sopro","tipo":"Máquina","status":"Em Uso"},
        {"nome":"Sopradora PET 8 Cabeças","setor":"Sopro","tipo":"Máquina","status":"Disponível"},
        {"nome":"Sopradora de Jarras 2L","setor":"Sopro","tipo":"Máquina","status":"Disponível"},
        {"nome":"Torquímetro Automatizado","setor":"Automação","tipo":"Equipamento","status":"Disponível"},
        {"nome":"Transportador de Rolo 15m","setor":"Movimentação","tipo":"Equipamento","status":"Disponível"},
        {"nome":"Mesa Rotativa Indexadora","setor":"Automação","tipo":"Equipamento","status":"Em Uso"},
        {"nome":"Separador Magnético Industrial","setor":"Automação","tipo":"Equipamento","status":"Disponível"},
        {"nome":"Cortadora a Laser 4000W","setor":"Usinagem","tipo":"Máquina","status":"Disponível"},
        {"nome":"Laser de Corte e Gravação","setor":"Usinagem","tipo":"Máquina","status":"Em Uso"},
        {"nome":"Cabine de Pintura Automatizada","setor":"Automação","tipo":"Sistema","status":"Disponível"},
        {"nome":"Sistema de Visão 3D","setor":"Automação","tipo":"Equipamento","status":"Disponível"},
        {"nome":"Extrusora de Tubos 150mm","setor":"Extrusão","tipo":"Máquina","status":"Em Uso"},
        {"nome":"Injetora Vertical 80T","setor":"Injeção","tipo":"Máquina","status":"Disponível"},
        {"nome":"Injetora Horizontal 250T","setor":"Injeção","tipo":"Máquina","status":"Manutenção"},
        {"nome":"Elevador de Paletes","setor":"Movimentação","tipo":"Equipamento","status":"Disponível"},
        {"nome":"Braço Robótico Pick & Place","setor":"Automação","tipo":"Sistema","status":"Em Uso"},
        {"nome":"Prensa Excêntrica 100T","setor":"Usinagem","tipo":"Máquina","status":"Disponível"}
    ]

    for m in maquinas:
        inserir_maquina(**m)

    print("concluído.")

if __name__ == "__main__":
    seed_maquinas()
