from app.falhas import inserir_falhas
from app.lista_falha import falhas

for falha in falhas:
    inserir_falhas(**falha)

print("Falhas inseridas com sucesso")
