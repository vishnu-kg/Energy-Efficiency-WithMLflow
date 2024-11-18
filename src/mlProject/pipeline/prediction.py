import joblib
import numpy as np
import pandas as pd
from pathlib import Path


class PredictionPipeline:
    def __init__(self):
        # Load the model
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))
        
        # Load the scaler
        self.scaler = joblib.load(Path('artifacts/data_transformation/robust_scaler.pkl'))

    def predict(self, data):
        """
        Predict outcomes for the given data after applying transformations.

        Args:
            data (pd.DataFrame or np.ndarray): Input data to predict.

        Returns:
            np.ndarray: Predictions made by the model.
        """
        # Ensure data is in the correct format (e.g., DataFrame or ndarray)
        if isinstance(data, pd.DataFrame):
            data = data.values  # Convert to NumPy array if DataFrame

        # Transform the data using the scaler
        transformed_data = self.scaler.transform(data)

        # Make predictions
        prediction = self.model.predict(transformed_data)

        return prediction