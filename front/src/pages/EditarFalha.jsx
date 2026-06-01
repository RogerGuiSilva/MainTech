import { useState, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";
import "../../css/style.css";

export default function EditarFalha() {

  const navigate = useNavigate();
  const { id } = useParams();

  const [descricao, setDescricao] = useState("");
  const [tipo, setTipo] = useState("");
  const [gravidade, setGravidade] = useState("");
  const [status, setStatus] = useState("ANALISE");
  const [data, setData] = useState("");

  const [maquina, setMaquina] = useState(null);
  const [equipamento, setEquipamento] = useState(null);

  useEffect(() => {

    fetch(`http://localhost:5000/falhas/${id}`)
      .then(res => res.json())
      .then(falha => {

        setDescricao(falha.descricao);
        setTipo(falha.tipo);
        setGravidade(falha.gravidade);
        setStatus(falha.status);
        setData(falha.data_ocorrencia);

        setMaquina(falha.maquina);
        setEquipamento(falha.equipamento);

      });

  }, [id]);

  function salvar(e) {

    e.preventDefault();

    fetch(`http://localhost:5000/falhas/${id}`, {
      method: "PUT",

      headers: {
        "Content-Type": "application/json"
      },

      body: JSON.stringify({
        descricao,
        tipo,
        gravidade,
        status,
        data_ocorrencia: data
      })
    })
      .then(res => res.json())
      .then(() => {

        alert("Falha atualizada!");

        navigate("/falhas");

      });

  }

  return (

    <div className="form_container">

      <h1>Editar Falha</h1>

      {maquina && (
        <p>
          <strong>Máquina:</strong> {maquina.nome}
        </p>
      )}

      {equipamento && (
        <p>
          <strong>Equipamento:</strong> {equipamento.nome}
        </p>
      )}

      <form onSubmit={salvar}>

        <input
          value={descricao}
          onChange={(e) => setDescricao(e.target.value)}
        />

        <input
          value={tipo}
          onChange={(e) => setTipo(e.target.value)}
        />

        <input
          value={gravidade}
          onChange={(e) => setGravidade(e.target.value)}
        />

        <input
          type="date"
          value={data}
          onChange={(e) => setData(e.target.value)}
        />

        <select
          value={status}
          onChange={(e) => setStatus(e.target.value)}
        >
          <option value="ANALISE">
            ANALISE
          </option>

          <option value="MANUTENCAO">
            MANUTENCAO
          </option>

          <option value="RESOLVIDA">
            RESOLVIDA
          </option>

          <option value="CANCELADA">
            CANCELADA
          </option>
        </select>

        <button type="submit">
          Salvar Alterações
        </button>

      </form>

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
