import os
from mlProject import logger
from mlProject.entity.config_entity import DataValidationConfig
import pandas as pd


class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_columns(self)-> bool:

        """
        Validate that all columns in the dataset match the schema definition
        in terms of names and data types.
        """
        try:
            # Load data
            data = pd.read_excel(self.config.unzip_data_dir)
            
            # Get schema columns and expected types
            schema_columns = self.config.all_schema 
            
            # Initialize validation status as True
            validation_status = True
            
            # Loop through schema columns and validate
            for col, expected_type in schema_columns.items():
                # Check if the column exists in the data
                if col not in data.columns:
                    validation_status = False
                    logger.error(f"Missing column: {col}")
                else:
                    # Validate data type without using pd.api
                    actual_type = data[col].dtype
                    if actual_type != expected_type:
                        validation_status = False
                        logger.error(f"Column {col} has incorrect type. Expected: {expected_type}, Found: {actual_type}")

            # Write the final validation status to the file after the loop
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")
            
            return validation_status
        
        except Exception as e:
            logger.exception("Error occurred during data validation.")
            raise e





       