import { useState } from "react";
import { Link } from "react-router-dom";
import AssistantPanel from "../components/AssistantPanel";
import FaciesPanel from "../components/FaciesPanel";
import FmiViewer from "../components/FmiViewer";
import FractureStats from "../components/FractureStats";
import TadpolePlot from "../components/TadpolePlot";
import WellLogPanel from "../components/WellLogPanel";
import WellSelector from "../components/WellSelector";

export default function DashboardPage() {
  const [status, setStatus] = useState("idle");

  return (
    <div className="app-shell">
      <header className="topbar">
        <div>
          <p className="eyebrow">Intelligent Wellbore</p>
          <h1>Fracture & Facies Analysis</h1>
        </div>
        <Link className="text-button" to="/login">
          Log out
        </Link>
      </header>

      <section className="status-row">
        <WellSelector />
        <div className="panel status-panel">
          <h2>Analysis status</h2>
          <p className="status-value">{status}</p>
          <button type="button" onClick={() => setStatus("idle")}>
            Analyze Well
          </button>
        </div>
      </section>

      <FmiViewer />

      <section className="split">
        <FractureStats />
        <FaciesPanel />
      </section>

      <TadpolePlot />
      <WellLogPanel />
      <AssistantPanel />
    </div>
  );
}
