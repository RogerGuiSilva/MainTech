import { Routes, Route } from "react-router-dom";

import Home from "./pages/Home.jsx";
import Maquinas from "./pages/Maquinas.jsx";
import Falhas from "./pages/Falhas.jsx";
import Equipamentos from "./pages/Equipamentos.jsx";

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/maquinas" element={<Maquinas />} />
      <Route path="/falhas" element={<Falhas />} />
      <Route path="/equipamentos" element={<Equipamentos />} />
    </Routes>
  );
}
