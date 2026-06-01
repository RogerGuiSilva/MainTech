import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import "../../css/style.css";

export default function Falhas() {

  const [falhas, setFalhas] = useState([]);
  const [loading, setLoading] = useState(true);
  const [busca, setBusca] = useState("");

  useEffect(() => {
    fetch("http://localhost:5000/falhas")
      .then(res => res.json())
      .then(data => {
        setFalhas(Array.isArray(data) ? data : []);
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
        <h1>Falhas</h1>

        <div className="maquinas_actions">
          <Link to="/" className="btn_secondary">
            Voltar
          </Link>

          <Link to="/falhas/nova" className="btn_primary">
            + Nova Falha
          </Link>

          <Link to="/falhas/historico" className="btn_secondary">
            Histórico
          </Link>
        </div>
      </header>

      <input
        type="text"
        placeholder="Buscar falha..."
        value={busca}
        onChange={(e) => setBusca(e.target.value)}
        className="busca_input"
      />

      {loading ? (
        <p>Carregando...</p>
      ) : (
        <section className="maquinas_list">

          {falhas
            .filter((f) => {

              const termo = busca.toLowerCase();

              return (
                f.descricao?.toLowerCase().includes(termo) ||
                f.maquina?.nome?.toLowerCase().includes(termo) ||
                f.equipamento?.nome?.toLowerCase().includes(termo)
              );

            })
            .map((f) => (

              <div key={f.id} className="maquina_card">

                <h2>{f.descricao}</h2>

                <p className={`status ${f.status?.toLowerCase()}`}>
                  {f.status}
                </p>

                <p><strong>Tipo:</strong> {f.tipo}</p>

                <p><strong>Gravidade:</strong> {f.gravidade}</p>

                <p><strong>Data:</strong> {f.data_ocorrencia}</p>

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

                <Link
                  to={`/falhas/editar/${f.id}`}
                  className="btn_secondary"
                >
                  Editar
                </Link>

              </div>

            ))}

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
