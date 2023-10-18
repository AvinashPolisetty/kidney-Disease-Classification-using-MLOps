from src.tumorClassification.config.configuration import ConfigurationManager
from src.tumorClassification.components.model_evaluation import Evaluation


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()