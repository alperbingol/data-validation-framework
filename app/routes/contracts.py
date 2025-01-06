from fastapi import APIRouter
from app.models.contract import DataContract
from app.services.contracts import list_contracts, load_contract, save_contract, delete_contract

router = APIRouter(prefix="/contracts", tags=["contracts"])

# Endpoint to create a new contract
@router.post("/")
def create_contract(contract: DataContract):
    # Placeholder for creating a contract
    return {"message": "Contract created successfully", "contract": contract}

@router.get("/")
def list_all_contracts():
    return {"contracts": list_contracts()}

@router.get("/{contract_name}")
def get_contract(contract_name: str):
    return {"contract": load_contract(contract_name)}

@router.post("/{contract_name}")
def create_contract(contract_name: str, contract: DataContract):
    save_contract(contract_name, contract.dict())
    return {"message": "Contract created successfully", "contract": contract}

@router.delete("/{contract_name}")
def delete_contract_endpoint(contract_name: str):
    delete_contract(contract_name)
    return {"message": f"Contract '{contract_name}' deleted successfully"}
