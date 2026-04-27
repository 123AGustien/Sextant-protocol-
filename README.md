# ⚡ Sextant Protocol – Power Grid Dependency Modelling & Failure Simulation

Sextant Protocol is a deterministic simulation framework for electrical power grid systems, designed to model dependency structures and analyse cascading failure propagation within controlled, read-only environments.

The framework supports resilience analysis, dependency mapping, and structured failure scenario simulation across interconnected grid infrastructure components.

---

## ▶ Run Simulation

Access the CI/CD simulation workflow here:  
Access the CI/CD simulation workflow here:
👉 https://github.com/123AGustien/Sextant-protocol-/actions⁠�


👉 https://github.com/123AGustien/Sextant-protocol-/actions/runs/⁠�
(Each run will generate a full success/failure log page)

Steps:
1. Select **"Sextant Grid Simulation Execution"**
2. Click **"Run workflow"**
3. Execute simulation with predefined scenario inputs

---

## 🧠 System Capabilities

- Deterministic dependency graph construction  
  (nodes: generators, substations, transformers)  

- Cascading failure propagation simulation  

- Event sequence reconstruction and replay  

- Scenario-based stress simulation  
  (e.g., overload, line failure, node isolation)  

---

## 🔗 Integration Model

- Structured ingestion of grid event data  
  (telemetry, logs, operational signals)  

- Read-only analytical processing  

- Sandbox-contained execution environment  

- No interaction with live or production grid systems  

---

## 🏗️ Architecture Overview

1. Ingest grid system event data  
2. Construct dependency graph  
3. Model system state transitions  
4. Simulate cascading failures  
5. Reconstruct event timelines  
6. Output traceable results for analysis  

---

## 🔒 Safety Boundary

- No control interface to physical grid systems  
- No write capability to operational infrastructure  
- Fully sandboxed execution via CI/CD workflows  

---

## 📊 Status

Early-stage deterministic simulation framework designed for:

- Grid resilience analysis  
- Infrastructure dependency modelling  
- Controlled scenario evaluation  

---

## 🔬 Positioning

This repository represents the **core simulation kernel (Cascade Lens architecture)** underpinning the Sextant Grid Digital Twin system.

It provides the foundational modelling logic used across all higher-level simulation and replay environments.
