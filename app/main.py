from fastapi import FastAPI
from app.routes import contracts

app = FastAPI()

# Include routes
app.include_router(contracts.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Data Validation Framework"}


'''
import pandas as pd
from app.services.validation import validate_dataset

# Sample dataset
data = {"id": [1, 2, 3], "email": ["a@test.com", "b@test.com", "c@test.com"]}
df = pd.DataFrame(data)

# Example validation config (simplified)
validation_config = {
    "id": {"unique": True, "nullable": False},
    "email": {"format": "email", "nullable": False}
}

result = validate_dataset(df, validation_config)
print(result)
'''