import "../../css/style.css";
import { Link } from "react-router-dom";
import { useEffect, useState } from "react";

import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  ResponsiveContainer
} from "recharts";

export default function Controle() {

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

  const maquinasDisponiveis = maquinas.filter(
    m => m.status === "DISPONIVEL"
  ).length;

  const maquinasParadas = maquinas.filter(
    m => m.status === "PARADA"
  ).length;

  const falhasAnalise = falhas.filter(
    f => f.status === "ANALISE"
  ).length;

  const falhasManutencao = falhas.filter(
    f => f.status === "MANUTENCAO"
  ).length;

  const falhasResolvidas = falhas.filter(
    f => f.status === "RESOLVIDA"
  ).length;

  const falhasCanceladas = falhas.filter(
    f => f.status === "CANCELADA"
  ).length;

  const dadosFalhas = [
    {
      nome: "Análise",
      valor: falhasAnalise
    },
    {
      nome: "Manutenção",
      valor: falhasManutencao
    },
    {
      nome: "Resolvidas",
      valor: falhasResolvidas
    },
    {
      nome: "Canceladas",
      valor: falhasCanceladas
    }
  ];

  const dadosMaquinas = [
    {
      nome: "Disponíveis",
      quantidade: maquinasDisponiveis
    },
    {
      nome: "Paradas",
      quantidade: maquinasParadas
    }
  ];

  const CORES = [
    "#3b82f6",
    "#ef4444",
    "#22c55e",
    "#f59e0b"
  ];

  return (

    <div className="maquinas">

      <header className="maquinas_header">

        <h1>Painel de Controle</h1>

        <div className="maquinas_actions">

          <Link
            to="/"
            className="btn_secondary"
          >
            Voltar
          </Link>

        </div>

      </header>

      <div className="dashboard_cards">

        <div className="dashboard_card">
          <h2>{totalMaquinas}</h2>
          <p>Total de Máquinas</p>
        </div>

        <div className="dashboard_card">
          <h2>{totalEquipamentos}</h2>
          <p>Total de Equipamentos</p>
        </div>

        <div className="dashboard_card">
          <h2>{maquinasDisponiveis}</h2>
          <p>Máquinas Disponíveis</p>
        </div>

        <div className="dashboard_card">
          <h2>{maquinasParadas}</h2>
          <p>Máquinas Paradas</p>
        </div>

        <div className="dashboard_card">
          <h2>{falhasAnalise}</h2>
          <p>Falhas em Análise</p>
        </div>

        <div className="dashboard_card">
          <h2>{falhasManutencao}</h2>
          <p>Falhas em Manutenção</p>
        </div>

        <div className="dashboard_card">
          <h2>{falhasResolvidas}</h2>
          <p>Falhas Resolvidas</p>
        </div>

        <div className="dashboard_card">
          <h2>{falhasCanceladas}</h2>
          <p>Falhas Canceladas</p>
        </div>

      </div>

      <div className="graficos_container">

        <div className="grafico_card">

          <h2>Falhas por Status</h2>

          <ResponsiveContainer
            width="100%"
            height={300}
          >

            <PieChart>

              <Pie
                data={dadosFalhas}
                dataKey="valor"
                nameKey="nome"
                outerRadius={100}
                label
              >

                {dadosFalhas.map((entry, index) => (

                  <Cell
                    key={index}
                    fill={CORES[index]}
                  />

                ))}

              </Pie>

              <Tooltip />

            </PieChart>

          </ResponsiveContainer>

        </div>

        <div className="grafico_card">

          <h2>Status das Máquinas</h2>

          <ResponsiveContainer
            width="100%"
            height={300}
          >

            <BarChart data={dadosMaquinas}>

              <CartesianGrid strokeDasharray="3 3" />

              <XAxis dataKey="nome" />

              <YAxis />

              <Tooltip />

              <Bar
                dataKey="quantidade"
                fill="#38bdf8"
              />

            </BarChart>

          </ResponsiveContainer>

        </div>

      </div>

    </div>

  );

}