import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import "../../css/falhas.css";

export default function Equipamentos() {

  const [equipamentos, setEquipamentos] = useState([]);
  const [loading, setLoading] = useState(true);

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

      {loading ? (

        <p>Carregando...</p>

      ) : (

        <section className="maquinas_list">

          {equipamentos.map((e) => (

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

            </div>

          ))}

        </section>

      )}

    </div>

  );
}