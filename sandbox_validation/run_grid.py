import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--trigger_node", default="none")
    parser.add_argument("--load_profile", default="baseline")
    args = parser.parse_args()

    print("=== Sandbox Grid Run ===")
    print("Trigger Node:", args.trigger_node)
    print("Load Profile:", args.load_profile)
    print("Status: OK")

if __name__ == "__main__":
    main()
