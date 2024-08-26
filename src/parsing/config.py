"""Config wrapping class"""

from parsing.model_config import ModelConfig

#pylint: disable=R0903
class Config:
    """Config wrapping class"""
    def __init__(self, config: dict):
        """Init config class using dict"""
        self.model_configs = [ModelConfig(model_config) for model_config in config['models']]

    def get_model_configs(self) -> list[ModelConfig]:
        """return list of model configs"""
        return self.model_configs
