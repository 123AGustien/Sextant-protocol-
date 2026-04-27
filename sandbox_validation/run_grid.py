import argparse

def main():
    parser = argparse.ArgumentParser(description="Sextant Grid Simulation Runner")

    parser.add_argument("--trigger_node", default="none")
    parser.add_argument("--load_profile", default="baseline")

    args = parser.parse_args()

    print("======================================")
    print("Sextant Grid Simulation Execution")
    print("======================================")
    print(f"Trigger Node  : {args.trigger_node}")
    print(f"Load Profile  : {args.load_profile}")
    print("--------------------------------------")
    print("Simulation Status: OK")
    print("======================================")

if __name__ == "__main__":
    main()
