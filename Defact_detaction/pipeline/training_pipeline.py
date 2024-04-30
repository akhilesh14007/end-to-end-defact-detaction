import sys
from Defact_detaction.logger import logging
from Defact_detaction.exception import AppException
from Defact_detaction.components.data_ingestion import DataIngestion
from Defact_detaction.components.data_validation import DataValidation
from Defact_detaction.entity.config_entity import DataIngestionConfig, DataValidationConfig
from Defact_detaction.entity.artifacts_entity import DataIngestionArtifact, DataValidationArtifact

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            # Initialize DataIngestion component and start data ingestion
            data_ingestion = DataIngestion(self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            return data_ingestion_artifact
        except Exception as e:
            logging.error(f"Error occurred during data ingestion: {e}")
            raise AppException(e, sys) from e

    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        try:
            # Initialize DataValidation component and start data validation
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,
                                             data_validation_config=self.data_validation_config)
            data_validation_artifact = data_validation.initiate_data_validation()
            return data_validation_artifact
        except Exception as e:
            logging.error(f"Error occurred during data validation: {e}")
            raise AppException(e, sys) from e

    def run_pipeline(self) -> None:
        try:
            # Start data ingestion
            data_ingestion_artifact = self.start_data_ingestion()

            # Start data validation using the obtained data ingestion artifact
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)

            # Continue with other pipeline steps
            # ...
        except AppException as ae:
            # Handle application-level exceptions
            logging.error(f"Application exception occurred: {ae}")
            # Perform any cleanup or recovery actions if needed
        except Exception as e:
            # Handle other unexpected exceptions
            logging.error(f"Unexpected exception occurred: {e}")
            # Perform any cleanup or recovery actions if needed
