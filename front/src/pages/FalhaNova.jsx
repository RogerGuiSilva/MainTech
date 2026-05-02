import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

export default function FalhaNova() {
  const navigate = useNavigate();

  const [descricao, setDescricao] = useState("");
  const [tipo, setTipo] = useState("");
  const [gravidade, setGravidade] = useState("");
  const [status, setStatus] = useState("ABERTA");
  const [data, setData] = useState("");
  const [maquinaId, setMaquinaId] = useState("");

  const [maquinas, setMaquinas] = useState([]);


  useEffect(() => {
    fetch("http://localhost:5000/maquinas")
      .then(res => res.json())
      .then(data => setMaquinas(data))
      .catch(err => console.error(err));
  }, []);


  const criarFalha = (e) => {
    e.preventDefault();

    fetch("http://localhost:5000/falhas", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        descricao,
        tipo,
        gravidade,
        data_ocorrencia: data,
        status,
        maquina_id: Number(maquinaId)
      })
    })
      .then(res => res.json())
      .then(() => {
        alert("Falha criada com sucesso!");
        navigate("/falhas");
      })
      .catch(err => console.error(err));
  };

  return (
    <div className="form_container">
      <h1>Nova Falha</h1>

      <form onSubmit={criarFalha}>

        <input
          type="text"
          placeholder="Descrição"
          value={descricao}
          onChange={e => setDescricao(e.target.value)}
          required
        />

        <input
          type="text"
          placeholder="Tipo"
          value={tipo}
          onChange={e => setTipo(e.target.value)}
          required
        />

        <input
          type="text"
          placeholder="Gravidade"
          value={gravidade}
          onChange={e => setGravidade(e.target.value)}
          required
        />

        <input
          type="date"
          value={data}
          onChange={e => setData(e.target.value)}
          required
        />

        <select value={status} onChange={e => setStatus(e.target.value)}>
          <option value="ABERTA">ABERTA</option>
          <option value="EM_ANALISE">EM_ANALISE</option>
          <option value="EM_MANUTENCAO">EM_MANUTENCAO</option>
          <option value="PARADA">PARADA</option>
        </select>

        <select
          value={maquinaId}
          onChange={e => setMaquinaId(e.target.value)}
          required
        >
          <option value="">Selecione a máquina</option>
          {maquinas.map(m => (
            <option key={m.id} value={m.id}>
              {m.nome}
            </option>
          ))}
        </select>

        <button type="submit">Criar Falha</button>

      </form>
    </div>
  );
}