import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import "../../css/style.css";

export default function Historico() {

  const [falhas, setFalhas] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://localhost:5000/falhas/historico")
      .then(res => res.json())
      .then(data => {
        setFalhas(data);
        setLoading(false);
      })
      .catch(err => {
        console.error(err);
        setLoading(false);
      });
  }, []);

  return (
    <div className="maquinas">

      <header className="maquinas_header">
        <h1>Histórico de Falhas</h1>

        <div className="maquinas_actions">
          <Link to="/falhas" className="btn_secondary">
            Voltar
          </Link>
        </div>
      </header>

      {loading ? (
        <p>Carregando...</p>
      ) : (
        <section className="maquinas_list">

          {falhas.length === 0 ? (
            <p>Nenhuma falha no histórico.</p>
          ) : (
            falhas.map((f) => (
              <div key={f.id} className="maquina_card">

                <h2>{f.descricao}</h2>

                <p className={`status ${f.status.toLowerCase()}`}>
                  {f.status}
                </p>

                <p>
                  <strong>Tipo:</strong> {f.tipo}
                </p>

                <p>
                  <strong>Gravidade:</strong> {f.gravidade}
                </p>

                <p>
                  <strong>Data:</strong> {f.data_ocorrencia}
                </p>

                {f.maquina && (
                  <p>
                    <strong>Máquina:</strong> {f.maquina.nome}
                  </p>
                )}

                {f.equipamento && (
                  <p>
                    <strong>Equipamento:</strong> {f.equipamento.nome}
                  </p>
                )}

              </div>
            ))
          )}

        </section>
      )}

      <footer className="footer">
        <p>
          Sistema de Gestão de Manutenção Industrial © 2026
        </p>

        <p>
          Desenvolvido por Roger 
        </p>
      </footer>

    </div>
  );
}
