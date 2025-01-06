from great_expectations.core.batch import BatchRequest
from great_expectations.data_context import DataContext
import pandas as pd
import os

# Initialize Great Expectations data context
data_context = DataContext()

def validate_dataset(dataset: pd.DataFrame, validation_config: dict):
    """
    Validates a dataset using Great Expectations.

    Args:
        dataset (pd.DataFrame): Dataset to validate.
        validation_config (dict): Data quality tests to apply.

    Returns:
        dict: Validation results.
    """
    # Save dataset to a temporary file
    temp_file = "temp_dataset.csv"
    dataset.to_csv(temp_file, index=False)

    # Add dataset to the Great Expectations batch request
    batch_request = BatchRequest(
        datasource_name="my_pandas_datasource",
        data_connector_name="default_inferred_data_connector_name",
        data_asset_name=temp_file
    )

    # Run validation
    checkpoint = data_context.get_checkpoint("my_checkpoint")
    result = checkpoint.run(batch_request=batch_request)

    # Clean up the temporary file
    os.remove(temp_file)

    return result.to_json_dict()
