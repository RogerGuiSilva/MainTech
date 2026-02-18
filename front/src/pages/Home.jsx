import { Link } from "react-router-dom";
import '../../css/home.css';


export default function Home() {
  return (
    <div className="home">

      <header className="home_header">
        <h1 className="home_title">MainTech</h1>
        <p className="home_subtitle">
          Painel Industrial para máquinas, falhas e equipamentos
        </p>
      </header>

      <section className="home_hero">
        <img
          className="home_image"
          src="/img/home-page.png"
          alt="Máquinas e equipamentos industriais"
        />
      </section>

      <section className="home_cards">

        <Link className="card" to="/maquinas">
        <img src="/img/maquina.png" className="card_icon" />
          <h2>Máquinas</h2>
          <p>Visualize e gerencie máquinas cadastradas.</p>
        </Link>

        <Link className="card" to="/falhas">
        <img src="/img/falhas.png" className="card_icon" />
          <h2>Falhas</h2>
          <p>Acompanhe ocorrências e histórico de falhas.</p>
        </Link>

        <Link className="card" to="/equipamentos">
        <img src="/img/equipamento.png" className="card_icon" />
          <h2>Equipamentos</h2>
          <p>Controle de equipamentos e componentes.</p>
        </Link>

      </section>

    </div>
  );
}
