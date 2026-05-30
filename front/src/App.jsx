import { Routes, Route } from "react-router-dom";

import Home from "./pages/Home.jsx";
import Maquinas from "./pages/Maquinas.jsx";
import FalhaNova from "./pages/FalhaNova";
import Falhas from "./pages/Falhas";
import Equipamentos from "./pages/Equipamentos.jsx";
import Historico from "./pages/Historico";
import EditarFalha from "./pages/EditarFalha";
import NovaMaquina from "./pages/NovaMaquina";
import NovoEquipamento from "./pages/NovoEquipamento";

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/maquinas" element={<Maquinas />} />
      <Route path="/maquinas/nova" element={<NovaMaquina />} />

      <Route path="/falhas" element={<Falhas />} />
      <Route path="/falhas/nova" element={<FalhaNova />} />
      <Route path="/falhas/historico" element={<Historico />} />
      <Route path="/falhas/editar/:id" element={<EditarFalha />} />

      <Route path="/equipamentos" element={<Equipamentos />} />
      <Route
        path="/equipamentos/novo"
        element={<NovoEquipamento />}
      />
    </Routes>
  );
}