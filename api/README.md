# API Layer

This layer defines read-only ingestion and evaluation endpoints for telemetry processing.

## 🚀 Workflow Trigger (Execution Layer)

The Sextant Protocol – Grid Module is executed through a controlled GitHub Actions workflow environment.

---

### ▶️ Manual Trigger (Primary Method)

The simulation can be initiated via GitHub Actions:

1. Navigate to the repository → **Actions tab**
2. Select workflow:
   **"Sextant Grid Simulation Execution"**
3. Click **Run workflow**
4. Optional parameters:
   - `trigger_node` → initiates failure scenario
   - `load_profile` → defines grid load conditions
5. Start execution

---

### 🔁 System Execution Flow

Once triggered, the system executes the following deterministic pipeline:

Grid Input Scenario  
→ Integration Adapter  
→ Core Simulation Engine  
→ Dependency Graph Evaluation  
→ Failure Propagation Engine  
→ Resilience Engine  
→ Output Artifact Generation  

---

### 📦 Output Artifacts

Each execution produces:

- `simulation_log.json`
- `system_state_snapshot.json`
- `resilience_report.json`

Stored under:
**GitHub Actions → Artifacts**

---

### 🧠 Deterministic Guarantee

- Identical input produces identical output  
- Fully replayable execution  
- No external system modification  
- Sandbox-isolated processing environment


## Purpose
To expose structured interfaces for:
- Telemetry ingestion
- Trace reconstruction
- Replay execution
- Simulation triggers

## Constraint
No write-back to external systems.
