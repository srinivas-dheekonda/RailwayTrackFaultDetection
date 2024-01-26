from src.cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_02_model_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_evalution import ModelEvalution

STAGE_NAME = "PREPARE BASE MODEL"

try:
    logger.info(f"********")
    logger.info(f">>>>>>>>stage {STAGE_NAME} started <<<<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


#################################################################
#STAGE_NAME = "Model Training"

try:
    logger.info(f"********")
    logger.info(f">>>>>>>>stage {STAGE_NAME} started <<<<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


#################################################################
STAGE_NAME = "Model Training"

try:
    logger.info(f"********")
    logger.info(f">>>>>>>>stage {STAGE_NAME} started <<<<<<<<")
    obj = ModelEvalution()
    obj.main()
    logger.info(f">>>>>>>>stage {STAGE_NAME} completed <<<<<<<<\n\nX==========X")
except Exception as e:
    logger.exception(e)
    raise e


