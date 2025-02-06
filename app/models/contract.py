from pydantic import BaseModel, Field, field_validator
from typing import Optional, Union


class SchemaField(BaseModel):
    """
    Represents a single field in a data schema.

    Attributes:
        field_name (str): The name of the field (1-50 characters).
        field_type (str): The data type of the field (string, integer, boolean, float).
        required (bool): Indicates whether the field is required.

    Validation:
        - The field_type is automatically converted to lowercase.
        - The field_type must be one of: "string", "integer", "boolean", "float".
    """
    field_name: str = Field(..., min_length=1, max_length=50)
    field_type: Union[str, float, int, bool] = Field(..., pattern="^(string|integer|boolean|float)$") 
    required: bool
    
    #If you only need to enforce fixed values, Field(regex=...) is enough.
    #If you need custom error messages, transformation, or complex logic, use @field_validator.

    @field_validator("field_type")
    @classmethod
    def validate_and_normalize_field_type(cls, value):
        """
        Validates and normalizes the field_type value.

        - Converts the input to lowercase.
        - Ensures the value is one of the allowed field types.

        Args:
            value (str): The input field_type value.

        Returns:
            str: The validated and normalized field_type.

        Raises:
            ValueError: If the field_type is not one of the allowed values.

        Note: If we use a normal method without @classmethod, the function would expect an instance (self) of the model.
        But Pydantic does not create an instance before validation, so this wouldnt work.
        """
        # Convert to lowercase first
        value = value.lower()

        # Validate field type
        allowed_types = {"string", "integer", "boolean", "float"}
        if value not in allowed_types:
            raise ValueError(f"Invalid field_type '{value}'. Allowed values: {', '.join(allowed_types)}")

        return value  #  Now both normalization and validation are done in one function

class DataContract(BaseModel):
    """
    Represents a contract for structured data.

    Attributes:
        name (str): The contract name (1-30 characters).
        description (str): A detailed description of the contract.
        is_active (bool): Indicates if the contract is active (default: True).
        created_at (Optional[str]): Timestamp when the contract was created (ISO 8601 format).
        data_schema (SchemaField): The schema defining the contract data.
    """
    name: str = Field(title="Contract Name", min_length = 1, max_length = 30, description="Contract name (1-30) characters", example="UserContract")
    description: str = Field(..., min_length=5, max_length=100, description="Detailed description")
    is_active: bool = Field(default=True) 
    created_at: Optional[str] = Field(None, description="Creation timestamp (ISO 8601)")
    data_schema: SchemaField = Field(..., description="JSON Schema defining contract data")

