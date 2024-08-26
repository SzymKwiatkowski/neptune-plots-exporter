"""Model Config parsing class"""


class ModelConfig:
    """Model Config class"""
    def __init__(self, model):
        self.model_name = model['model_name']
        self.folder_name = model['folder_name']
        self.run_ids = model['run_ids']
        self.mapping_dict = model['mapping_dict']
        self.metrics = model['metrics']

    def get_run_ids(self) -> list[str]:
        """Get run_ids"""
        return self.run_ids

    def get_model_name(self) -> str:
        """Get model_name"""
        return self.model_name

    def get_folder_name(self) -> str:
        """Get folder_name"""
        return self.folder_name

    def get_mapping_dict(self) -> dict[str, str]:
        """Get mapping_dict"""
        return self.mapping_dict

    def get_run_label(self, run_id: str) -> str:
        """Get run_label"""
        return self.mapping_dict[run_id]

    def get_metrics(self) -> list[str]:
        """Get metrics"""
        return self.metrics
