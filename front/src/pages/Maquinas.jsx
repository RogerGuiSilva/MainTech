import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import "../../css/maquinas.css";


export default function Maquinas() {


  const [maquinas, setMaquinas] = useState([]);

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://localhost:5000/maquinas")
      .then(res => res.json())
      .then(data => {
        setMaquinas(data);
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
        <h1>Máquinas</h1>


        <div className="maquinas_actions">
          <Link to="/" className="btn_secondary">Voltar</Link>

          <Link to="/maquinas/nova" className="btn_primary">
            + Nova Máquina
          </Link>

        </div>
      </header>

      {loading ? (
        <p>Carregando...</p>
      ) : (
        <section className="maquinas_list">
          {maquinas.map((m) => (
            <div key={m.id} className="maquina_card">
              <h2>{m.nome}</h2>

              <p className={`status ${m.status.toLowerCase()}`}>
  {m.status}
</p>

              <p><strong>Setor:</strong> {m.setor}</p>

              <p><strong>Tipo:</strong> {m.tipo}</p>

              <p><strong>Status:</strong> {m.status}</p>

            </div>
          ))}
        </section>
      )}

    </div>
  );
}