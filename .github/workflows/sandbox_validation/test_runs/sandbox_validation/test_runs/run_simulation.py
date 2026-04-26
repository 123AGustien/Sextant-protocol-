import os
import json
import argparse


def main():
    parser = argparse.ArgumentParser(description="Sextant Grid Simulation Execution (Sandbox Mode)")
    
    parser.add_argument("--trigger_node", default="none")
    parser.add_argument("--load_profile", default="baseline")
    
    args = parser.parse_args()

    # Ensure output directory exists
    os.makedirs("sandbox_validation/outputs", exist_ok=True)

    # Deterministic simulation output (stub version)
    result = {
        "status": "SUCCESS",
        "execution_mode": "SANDBOX_STUB",
        "trigger_node": args.trigger_node,
        "load_profile": args.load_profile,
        "message": "Baseline simulation executed successfully"
    }

    output_path = "sandbox_validation/outputs/simulation_log.json"

    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)

    print(f"[OK] Simulation complete → {output_path}")


if __name__ == "__main__":
    main()
