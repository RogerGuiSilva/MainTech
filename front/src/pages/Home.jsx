import { Link } from "react-router-dom";
import { useEffect, useState } from "react";
import "../../css/home.css";

export default function Home() {

  const [maquinas, setMaquinas] = useState([]);
  const [falhas, setFalhas] = useState([]);
  const [equipamentos, setEquipamentos] = useState([]);

  useEffect(() => {

    fetch("http://localhost:5000/maquinas")
      .then(res => res.json())
      .then(data => setMaquinas(data))
      .catch(err => console.error(err));

    fetch("http://localhost:5000/falhas")
      .then(res => res.json())
      .then(data => setFalhas(data))
      .catch(err => console.error(err));

    fetch("http://localhost:5000/equipamentos")
      .then(res => res.json())
      .then(data => setEquipamentos(data))
      .catch(err => console.error(err));

  }, []);

  const totalMaquinas = maquinas.length;

  const totalEquipamentos = equipamentos.length;

  const falhasEmMaquinas = falhas.filter(
    f => f.maquina
  ).length;

  const falhasEmEquipamentos = falhas.filter(
    f => f.equipamento
  ).length;

  const maquinasParadas = maquinas.filter(
    m => m.status === "PARADA"
  ).length;

  return (
    <div className="home">

      <header className="home_header">
        <h1 className="home_title">MainTech</h1>

        <p className="home_subtitle">
          Painel Industrial para máquinas, falhas e equipamentos
        </p>
      </header>

      <div className="dashboard_cards">

        <div className="dashboard_card">
          <h2>{totalMaquinas}</h2>
          <p>Máquinas</p>
        </div>

        <div className="dashboard_card">
          <h2>{totalEquipamentos}</h2>
          <p>Equipamentos</p>
        </div>

        <div className="dashboard_card">
          <h2>{falhasEmMaquinas}</h2>
          <p>Falhas em Máquinas</p>
        </div>

        <div className="dashboard_card">
          <h2>{falhasEmEquipamentos}</h2>
          <p>Falhas em Equipamentos</p>
        </div>

        <div className="dashboard_card">
          <h2>{maquinasParadas}</h2>
          <p>Máquinas Paradas</p>
        </div>

      </div>

      <section className="home_hero">
        <img
          className="home_image"
          src="/img/image.jpg"
          alt="Máquinas e equipamentos industriais"
        />
      </section>

      <section className="home_cards">

        <Link className="card" to="/maquinas">
          <img src="/img/maquina.png" className="card_icon" />
          <h2>Máquinas</h2>
          <p>Máquinas Cadastradas</p>
        </Link>

        <Link className="card" to="/falhas">
          <img src="/img/falhas.png" className="card_icon" />
          <h2>Falhas</h2>
          <p>Ocorrências e histórico de falhas</p>
        </Link>

        <Link className="card" to="/equipamentos">
          <img src="/img/equipamento.png" className="card_icon" />
          <h2>Equipamentos</h2>
          <p>Equipamentos Cadastrados</p>
        </Link>

      </section>

    </div>
  );
}