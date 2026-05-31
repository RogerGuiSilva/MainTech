import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import "../../css/style.css";

export default function Equipamentos() {

  const [equipamentos, setEquipamentos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [busca, setBusca] = useState("");

  useEffect(() => {

    fetch("http://localhost:5000/equipamentos")
      .then(res => res.json())
      .then(data => {

        setEquipamentos(data);
        setLoading(false);

      })
      .catch(err => {

        console.error(err);
        setLoading(false);

      });

  }, []);

  function excluirEquipamento(id) {

  const confirmar = window.confirm(
    "Deseja realmente excluir este equipamento?"
  );

  if (!confirmar) return;

  fetch(`http://localhost:5000/equipamentos/${id}`, {
    method: "DELETE"
  })
    .then(() => {

      setEquipamentos(
        equipamentos.filter(
          e => e.id !== id
        )
      );

    });

}

  return (

    <div className="maquinas">

      <header className="maquinas_header">

        <h1>Equipamentos</h1>

        <div className="maquinas_actions">

          <Link to="/" className="btn_secondary">
            Voltar
          </Link>

          <Link
            to="/equipamentos/novo"
            className="btn_primary"
          >
            + Novo Equipamento
          </Link>

        </div>

      </header>

      <input
        type="text"
        placeholder="Buscar equipamento..."
        value={busca}
        onChange={(e) => setBusca(e.target.value)}
        className="busca_input"
      />

      {loading ? (

        <p>Carregando...</p>

      ) : (

        <section className="maquinas_list">

          {equipamentos
            .filter((e) => {

              const termo = busca.toLowerCase();

              return (
                e.nome?.toLowerCase().includes(termo) ||
                e.setor?.toLowerCase().includes(termo) ||
                e.tipo?.toLowerCase().includes(termo)
              );

            })
            .map((e) => (

              <div key={e.id} className="maquina_card">

                <h2>{e.nome}</h2>

                <p>
                  <strong>Setor:</strong> {e.setor}
                </p>

                <p>
                  <strong>Tipo:</strong> {e.tipo}
                </p>

                <p className={`status ${e.status.toLowerCase()}`}>
                  {e.status}
                </p>

                <button
                  className="btn_delete"
                    onClick={() => excluirEquipamento(e.id)}
                                  >
                                Excluir
                                      </button>

              </div>

            ))}

        </section>

      )}

    </div>

  );
}