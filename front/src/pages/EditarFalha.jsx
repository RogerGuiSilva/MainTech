import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

export default function EditarFalha() {

  const navigate = useNavigate();

  const [falhas, setFalhas] = useState([]);
  const [maquinaId, setMaquinaId] = useState("");
  const [falhaSelecionada, setFalhaSelecionada] = useState(null);

  const [descricao, setDescricao] = useState("");
  const [tipo, setTipo] = useState("");
  const [gravidade, setGravidade] = useState("");
  const [status, setStatus] = useState("ANALISE");
  const [data, setData] = useState("");

  useEffect(() => {

    fetch("http://localhost:5000/falhas")
      .then(res => res.json())
      .then(data => setFalhas(data));

  }, []);

  const maquinasComFalha = [
    ...new Map(
      falhas
        .filter(f => f.maquina)
        .map(f => [f.maquina.id, f.maquina])
    ).values()
  ];

  const falhasDaMaquina = falhas.filter(
    f => f.maquina?.id === Number(maquinaId)
  );

  function selecionarFalha(idFalha) {

    const falha = falhas.find(f => f.id === Number(idFalha));

    if (!falha) return;

    setFalhaSelecionada(falha.id);

    setDescricao(falha.descricao);
    setTipo(falha.tipo);
    setGravidade(falha.gravidade);
    setStatus(falha.status);
    setData(falha.data_ocorrencia);
  }

  function salvar(e) {

    e.preventDefault();

    fetch(`http://localhost:5000/falhas/${falhaSelecionada}`, {
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

      <select
        value={maquinaId}
        onChange={(e) => {
          setMaquinaId(e.target.value);
          setFalhaSelecionada(null);
        }}
      >
        <option value="">
          Selecione uma máquina
        </option>

        {maquinasComFalha.map(m => (
          <option key={m.id} value={m.id}>
            {m.nome}
          </option>
        ))}
      </select>

      {maquinaId && (

        <select
          onChange={(e) => selecionarFalha(e.target.value)}
        >
          <option value="">
            Selecione uma falha
          </option>

          {falhasDaMaquina.map(f => (
            <option key={f.id} value={f.id}>
              {f.descricao}
            </option>
          ))}
        </select>

      )}

      {falhaSelecionada && (

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
            <option value="ANALISE">ANALISE</option>
            <option value="MANUTENCAO">MANUTENCAO</option>
            <option value="RESOLVIDA">RESOLVIDA</option>
            <option value="CANCELADA">CANCELADA</option>
          </select>

          <button type="submit">
            Salvar Alterações
          </button>

        </form>

      )}

    </div>

  );
}