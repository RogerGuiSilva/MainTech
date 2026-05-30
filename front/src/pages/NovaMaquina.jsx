import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function NovaMaquina() {

  const navigate = useNavigate();

  const [nome, setNome] = useState("");
  const [setor, setSetor] = useState("");
  const [tipo, setTipo] = useState("");
  const [status, setStatus] = useState("DISPONIVEL");

  const criarMaquina = (e) => {

    e.preventDefault();

    fetch("http://localhost:5000/maquinas", {

      method: "POST",

      headers: {
        "Content-Type": "application/json"
      },

      body: JSON.stringify({
        nome,
        setor,
        tipo,
        status
      })

    })
      .then(res => res.json())
      .then(() => {

        alert("Máquina cadastrada!");

        navigate("/maquinas");

      });

  };

  return (

    <div className="form_container">

      <h1>Nova Máquina</h1>

      <form onSubmit={criarMaquina}>

        <input
          type="text"
          placeholder="Nome"
          value={nome}
          onChange={(e) => setNome(e.target.value)}
          required
        />

        <input
          type="text"
          placeholder="Setor"
          value={setor}
          onChange={(e) => setSetor(e.target.value)}
          required
        />

        <input
          type="text"
          placeholder="Tipo"
          value={tipo}
          onChange={(e) => setTipo(e.target.value)}
          required
        />

        <select
          value={status}
          onChange={(e) => setStatus(e.target.value)}
        >
          <option value="DISPONIVEL">
            DISPONIVEL
          </option>
        </select>

        <button type="submit">
          Cadastrar Máquina
        </button>

      </form>

    </div>

  );
}