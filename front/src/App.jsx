import { Routes, Route } from "react-router-dom";

import Home from "./pages/Home.jsx";
import Maquinas from "./pages/Maquinas.jsx";
import FalhaNova from "./pages/FalhaNova";
import Falhas from "./pages/Falhas";
import Equipamentos from "./pages/Equipamentos.jsx";

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/maquinas" element={<Maquinas />} />
      <Route path="/falhas" element={<Falhas />} />
      <Route path="/falhas/nova" element={<FalhaNova />} />
      <Route path="/equipamentos" element={<Equipamentos />} />
    </Routes>
  );
}