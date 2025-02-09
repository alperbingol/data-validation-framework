from fastapi import APIRouter, Depends
from app.models.contract import DataContract
from app.services.contracts import list_contracts, load_contract, save_contract, delete_contract
from app.database import db

router = APIRouter(prefix="/contracts", tags=["contracts"])

# Endpoint to create a new contract
"""
@router.post("/", 
            summary="Create Contracts", 
            description="Retrieve all the data contracts stored in the system.",
            tags=["contracts"])
def create_contract(contract: DataContract):
    # Placeholder for creating a contract
    return {"message": "Contract created successfully", "contract": contract}

"""

def get_contract_service():
    """Provides the `load_contract` function as a dependency."""
    return load_contract  # Returns function reference

@router.get("/{contract_name}")
def get_contract(contract_name: str, load_contract=Depends(get_contract_service)):
    """Retrieve contract details using dependency injection."""
    return {"contract": load_contract(contract_name)}

def get_all_contracts_service():
    """Provides the `list_contracts` function as a dependency."""
    return list_contracts # Returns function reference

@router.get("/")
def list_all_contracts(list_contracts=Depends(get_all_contracts_service)):
    """Retrieve all contracts using dependency injection."""
    return {"contracts": list_contracts()}

def save_the_contract():
    """Provides the `save_contract` function as a dependency."""
    return save_contract # Returns function reference

@router.post("/{contract_name}")
def create_contract(contract_name: str, contract: DataContract, save_contract=Depends(save_the_contract)):
    save_contract(contract_name, contract.dict())
    return {"message": "Contract created successfully", "contract": contract}

def delete_the_contract():
    """Provides the `delete_contract` function as a dependency."""
    return delete_contract # Returns function reference

@router.delete("/{contract_name}")
def delete_contract_endpoint(contract_name: str, delete_contract=Depends(delete_the_contract)):
    delete_contract(contract_name)
    return {"message": f"Contract '{contract_name}' deleted successfully"}

@router.get("/test-db")
async def test_db_connection():
    # Example: Fetch all collections
    collections = await db.list_collection_names()
    return {"collections": collections}
