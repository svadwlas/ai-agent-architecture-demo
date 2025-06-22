import yaml
from pathlib import Path

def load_config():
    with open(Path("config/agent_config.yaml"), "r") as f:
        return yaml.safe_load(f)

def main():
    config = load_config()
    print(f"Loaded agent config: {config['agent']['name']}")
    print("Pretend to launch the agent loop...")

if __name__ == "__main__":
    main()
