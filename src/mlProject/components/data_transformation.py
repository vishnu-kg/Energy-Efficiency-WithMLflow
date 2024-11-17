






import os
import pickle
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import train_test_split
import pandas as pd
from mlProject.entity.config_entity import DataTransformationConfig
from mlProject import logger

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_spliting(self):
        # Load data
        data = pd.read_excel(self.config.data_path)

        # Split the data into training and test sets (75% train, 25% test).
        train, test = train_test_split(data, test_size=0.25, random_state=42)

        # Separate features and target variable Y1
        y_train = train['Y1']
        y_test = test['Y1']

        X_train = train.drop(columns=['Y1', 'Y2'])  # Exclude both targets from features
        X_test = test.drop(columns=['Y1', 'Y2'])

        # Initialize RobustScaler and fit to training data
        scaler = RobustScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        # Convert scaled data back to DataFrame and append target variable Y1
        train_scaled = pd.DataFrame(X_train_scaled, columns=X_train.columns)
        train_scaled['Y1'] = y_train.reset_index(drop=True)

        test_scaled = pd.DataFrame(X_test_scaled, columns=X_test.columns)
        test_scaled['Y1'] = y_test.reset_index(drop=True)

        # Save the scaled datasets
        train_scaled.to_csv(os.path.join(self.config.root_dir, "train_scaled.csv"), index=False)
        test_scaled.to_csv(os.path.join(self.config.root_dir, "test_scaled.csv"), index=False)

        # Save the scaler object for later use
        scaler_path = os.path.join(self.config.root_dir, "robust_scaler.pkl")
        with open(scaler_path, 'wb') as f:
            pickle.dump(scaler, f)

        logger.info("Data split into training and test sets, scaled, and scaler object saved successfully.")
        logger.info(f"Train shape: {train_scaled.shape}")
        logger.info(f"Test shape: {test_scaled.shape}")
        logger.info(f"Scaler saved at: {scaler_path}")

        print(f"Train shape: {train_scaled.shape}")
        print(f"Test shape: {test_scaled.shape}")
        print(f"Scaler saved at: {scaler_path}")


























# import os
# from mlProject import logger
# from sklearn.model_selection import train_test_split
# import pandas as pd
# from mlProject.entity.config_entity import DataTransformationConfig
# from sklearn.preprocessing import RobustScaler



# class DataTransformation:
#     def __init__(self, config: DataTransformationConfig):
#         self.config = config



#     def train_test_spliting(self):
#         data = pd.read_excel(self.config.data_path)

#         # Split the data into training and test sets. (0.75, 0.25) split.
#         train, test = train_test_split(data)

#         train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
#         test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

#         logger.info("Splited data into training and test sets")
#         logger.info(train.shape)
#         logger.info(test.shape)

#         print(train.shape)
#         print(test.shape)
        