import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

export default function EditarFalha() {

  const navigate = useNavigate();

  const [falhas, setFalhas] = useState([]);

  const [tipoItem, setTipoItem] = useState("");

  const [maquinaId, setMaquinaId] = useState("");
  const [equipamentoId, setEquipamentoId] = useState("");

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

  const equipamentosComFalha = [
    ...new Map(
      falhas
        .filter(f => f.equipamento)
        .map(f => [f.equipamento.id, f.equipamento])
    ).values()
  ];

  const falhasDaMaquina = falhas.filter(
    f => f.maquina?.id === Number(maquinaId)
  );

  const falhasDoEquipamento = falhas.filter(
    f => f.equipamento?.id === Number(equipamentoId)
  );

  function selecionarFalha(idFalha) {

    const falha = falhas.find(
      f => f.id === Number(idFalha)
    );

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
        value={tipoItem}
        onChange={(e) => {

          setTipoItem(e.target.value);

          setMaquinaId("");
          setEquipamentoId("");
          setFalhaSelecionada(null);

        }}
      >
        <option value="">
          Selecione o tipo
        </option>

        <option value="MAQUINA">
          Máquina
        </option>

        <option value="EQUIPAMENTO">
          Equipamento
        </option>

      </select>

      {tipoItem === "MAQUINA" && (

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

            <option
              key={m.id}
              value={m.id}
            >
              {m.nome}
            </option>

          ))}

        </select>

      )}

      {tipoItem === "EQUIPAMENTO" && (

        <select
          value={equipamentoId}
          onChange={(e) => {

            setEquipamentoId(e.target.value);
            setFalhaSelecionada(null);

          }}
        >
          <option value="">
            Selecione um equipamento
          </option>

          {equipamentosComFalha.map(eq => (

            <option
              key={eq.id}
              value={eq.id}
            >
              {eq.nome}
            </option>

          ))}

        </select>

      )}

      {(maquinaId || equipamentoId) && (

        <select
          onChange={(e) =>
            selecionarFalha(e.target.value)
          }
        >
          <option value="">
            Selecione uma falha
          </option>

          {(tipoItem === "MAQUINA"
            ? falhasDaMaquina
            : falhasDoEquipamento
          ).map(f => (

            <option
              key={f.id}
              value={f.id}
            >
              {f.descricao}
            </option>

          ))}

        </select>

      )}

      {falhaSelecionada && (

        <form onSubmit={salvar}>

          <input
            value={descricao}
            onChange={(e) =>
              setDescricao(e.target.value)
            }
          />

          <input
            value={tipo}
            onChange={(e) =>
              setTipo(e.target.value)
            }
          />

          <input
            value={gravidade}
            onChange={(e) =>
              setGravidade(e.target.value)
            }
          />

          <input
            type="date"
            value={data}
            onChange={(e) =>
              setData(e.target.value)
            }
          />

          <select
            value={status}
            onChange={(e) =>
              setStatus(e.target.value)
            }
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

      )}

    </div>

  );
}