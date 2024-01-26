from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.evalution import Evaluation
from cnnClassifier import logger


STAGE_NAME = "Model Evalution"

class ModelEvalution:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()


if __name__ == '__main__':
    try:
        logger.info(f"********")
        logger.info(f">>>>>>>>stage {STAGE_NAME} started <<<<<<<<")
        obj = ModelEvalution()
        obj.main()
        logger.info(f">>>>>>>>stage {STAGE_NAME} completed <<<<<<<<\n\nX==========X")
    except Exception as e:
        logger.exception(e)
        raise e