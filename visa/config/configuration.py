import os,sys
from visa.constant import *
from visa.logger import logging
from visa.exception import CustomException
from visa.entity.config_entity import *
from visa.utils.utils import read_yaml_file


class Configuration:
    def __init__(self,
                    config_file_path:str = CONFIG_FILE_PATH,
                    current_time_stamp:str = CURRENT_TIME_STAMP)-> None:
        

        try:
            self.config_file_info = read_yaml_file(file_path=config_file_path)
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.time_stamp = current_time_stamp
            

        except Exception as e:
            raise CustomException(e,sys) from e

    def get_data_ingestion_config(self)->DataIngestionConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_ingestion_artifact_dir = os.path.join(artifact_dir,DATA_INGESTION_ARTIFACT_DIR,
                                                                        self.time_stamp) 
        except Exception as e:
            raise CustomException(e,sys) from e      
     

    def get_training_pipeline_config(self)->TrainingPipelineConfig:
        try:
            training_pipeline_config = self.config_file_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR,training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
                                                 training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY])
            
            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)

            return training_pipeline_config
            logging.info(f"training pipeline competed: {training_pipeline_config}")


        except Exception as e:
            raise CustomException(e,sys) from e




