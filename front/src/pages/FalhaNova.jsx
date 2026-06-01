import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "../../css/style.css";

export default function FalhaNova() {

  const navigate = useNavigate();

  const [descricao, setDescricao] = useState("");
  const [tipo, setTipo] = useState("");
  const [gravidade, setGravidade] = useState("");
  const [status, setStatus] = useState("ANALISE");
  const [data, setData] = useState("");

  const [maquinaId, setMaquinaId] = useState("");
  const [equipamentoId, setEquipamentoId] = useState("");

  const [maquinas, setMaquinas] = useState([]);
  const [equipamentos, setEquipamentos] = useState([]);

  useEffect(() => {

    fetch("http://localhost:5000/maquinas")
      .then(res => res.json())
      .then(data => setMaquinas(data))
      .catch(err => console.error(err));

    fetch("http://localhost:5000/equipamentos")
      .then(res => res.json())
      .then(data => setEquipamentos(data))
      .catch(err => console.error(err));

  }, []);

  const criarFalha = (e) => {

    e.preventDefault();

    if (!maquinaId && !equipamentoId) {
      alert("Selecione uma máquina ou um equipamento");
      return;
    }

    if (maquinaId && equipamentoId) {
      alert("Selecione apenas uma máquina ou um equipamento");
      return;
    }

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
        maquina_id: maquinaId ? Number(maquinaId) : null,
        equipamento_id: equipamentoId ? Number(equipamentoId) : null
      })
    })
      .then(res => {

        if (!res.ok) {
          return res.json().then(data => {
            throw new Error(data.erro || "Erro ao criar falha");
          });
        }

        return res.json();

      })
      .then(() => {

        alert("Falha criada com sucesso!");

        navigate(equipamentoId ? "/equipamentos" : "/falhas");

      })
      .catch(err => {

        console.error(err);
        alert(err.message);

      });
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

        <select
          value={status}
          onChange={e => setStatus(e.target.value)}
        >
          <option value="ANALISE">
            ANALISE
          </option>

          <option value="MANUTENCAO">
            MANUTENCAO
          </option>
        </select>

        <select
          value={maquinaId}
          onChange={e => setMaquinaId(e.target.value)}
        >
          <option value="">
            Selecione a máquina
          </option>

          {maquinas.map(m => (
            <option
              key={m.id}
              value={m.id}
            >
              {m.nome}
            </option>
          ))}
        </select>

        <select
          value={equipamentoId}
          onChange={e => setEquipamentoId(e.target.value)}
        >
          <option value="">
            Selecione o equipamento
          </option>

          {equipamentos.map(e => (
            <option
              key={e.id}
              value={e.id}
            >
              {e.nome}
            </option>
          ))}
        </select>

        <button type="submit">
          Criar Falha
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
