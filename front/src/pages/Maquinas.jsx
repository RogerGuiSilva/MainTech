import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import "../../css/style.css";

export default function Maquinas() {

  const [maquinas, setMaquinas] = useState([]);
  const [loading, setLoading] = useState(true);
  const [busca, setBusca] = useState("");

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

  function excluirMaquina(id) {

  const confirmar = window.confirm(
    "Deseja realmente excluir esta máquina?"
  );

  if (!confirmar) return;

  fetch(`http://localhost:5000/maquinas/${id}`, {
    method: "DELETE"
  })
    .then(res => {

      if (!res.ok) {
        return res.json().then(data => {
          throw new Error(data.erro || "Erro ao excluir máquina");
        });
      }

      return res.json();

    })
    .then(() => {

      setMaquinas(
        maquinas => maquinas.filter(m => m.id !== id)
      );

    })
    .catch(err => {

      console.error(err);
      alert(err.message);

    });

}


  

  
  return (

    <div className="maquinas">

      <header className="maquinas_header">

        <h1>Máquinas</h1>

        <div className="maquinas_actions">

          <Link to="/" className="btn_secondary">
            Voltar
          </Link>

          <Link to="/maquinas/nova" className="btn_primary">
            + Nova Máquina
          </Link>

        </div>

      </header>

      <input
        type="text"
        placeholder="Buscar máquina..."
        value={busca}
        onChange={(e) => setBusca(e.target.value)}
        className="busca_input"
      />

      {loading ? (

        <p>Carregando...</p>

      ) : (

        <section className="maquinas_list">

          {maquinas
            .filter((m) => {

              const termo = busca.toLowerCase();



              return (
                m.nome?.toLowerCase().includes(termo) ||
                m.setor?.toLowerCase().includes(termo) ||
                m.tipo?.toLowerCase().includes(termo)
              );

            })
            .map((m) => (

              <div key={m.id} className="maquina_card">

                <h2>{m.nome}</h2>

                <p className={`status ${m.status.toLowerCase()}`}>
                  {m.status}
                </p>

                <p>
                  <strong>Setor:</strong> {m.setor}
                </p>

                <p>
                  <strong>Tipo:</strong> {m.tipo}
                </p>

                <button
                  className="btn_delete"
                  onClick={() => excluirMaquina(m.id)}
                  >
                      Excluir
                            </button>

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
