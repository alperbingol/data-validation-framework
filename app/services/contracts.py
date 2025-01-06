import json
from pathlib import Path

CONTRACTS_DIR = Path("contracts")

def save_contract(contract_name: str, contract_data: dict):
    """Save a contract to a file."""
    CONTRACTS_DIR.mkdir(exist_ok=True)
    with open(CONTRACTS_DIR / f"{contract_name}.json", "w") as file:
        json.dump(contract_data, file)

def load_contract(contract_name: str) -> dict:
    """Load a contract from a file."""
    with open(CONTRACTS_DIR / f"{contract_name}.json", "r") as file:
        return json.load(file)

def list_contracts() -> list:
    """List all available contracts."""
    return [f.stem for f in CONTRACTS_DIR.glob("*.json")]

def delete_contract(contract_name: str):
    """Delete a contract."""
    (CONTRACTS_DIR / f"{contract_name}.json").unlink()
