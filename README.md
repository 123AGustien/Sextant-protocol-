
⚡ Sextant Protocol – Power Grid Dependency Modelling & Failure Simulation
Sextant Protocol is a deterministic simulation framework for electrical power grid systems, designed to model dependency structures and analyse cascading failure propagation within controlled, read-only environments.
The framework supports resilience analysis, dependency mapping, and structured failure scenario simulation across interconnected grid infrastructure components.
▶ Run Simulation
Access the CI/CD simulation workflow

## ▶ Run Simulation

👉 https://github.com/123AGustien/Sextant-protocol-/actions

From there:
1. Select workflow: **Sextant Grid Simulation Execution**
2. Click **Run workflow**


⚡ Sextant Protocol – Power Grid Dependency Modelling & Failure Simulation
Sextant Protocol is a deterministic simulation framework for electrical power grid systems, designed to model dependency structures and analyse cascading failure propagation within controlled, read-only environments.
The framework supports resilience analysis, dependency mapping, and structured failure scenario simulation across interconnected grid infrastructure components.
▶ Run Simulation
Access the CI/CD simulation workflow here:
👉 https://github.com/123AGustien/Sextant-protocol-/actions/workflows/sextant-grid-simulation.yml⁠�
Steps:
Open the workflow page above
Select “Sextant Grid Simulation Execution”
Click “Run workflow”
Choose parameters (optional):
trigger_node → failure injection point
load_profile → baseline / stress / peak
Execute simulation
🧠 System Capabilities
Deterministic dependency graph construction
(generators, substations, transformers)
Cascading failure propagation modelling
Event sequence reconstruction and replay
Scenario-based stress simulation
(overload, line failure, node isolation)
🔗 Integration Model
Structured ingestion of grid event data
(telemetry, logs, operational signals)
Read-only analytical processing
Sandbox-contained execution environment
No interaction with live or production grid systems
🏗️ Architecture Overview
Ingest grid system event data
Construct dependency graph
Model system state transitions
Simulate cascading failures
Reconstruct event timelines
Output traceable results for analysis
🔒 Safety Boundary
No control interface to physical grid systems
No write capability to operational infrastructure
Fully sandboxed CI/CD execution via GitHub Actions
📊 Status
Early-stage deterministic simulation framework for:
Grid resilience analysis
Infrastructure dependency modelling
Controlled scenario evaluation
🔬 Positioning
This repository represents the core simulation kernel (Cascade Lens architecture) underpinning the Sextant Grid Digital Twin system.
It provides the foundational modelling logic used across all higher-level simulation and replay environments.
