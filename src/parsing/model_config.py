"""Model Config parsing class"""


class ModelConfig:
    def __init__(self, model):
        self.model_name = model['model_name']
        self.folder_name = model['folder_name']
        self.run_ids = model['run_ids']
        self.mapping_dict = model['mapping_dict']
        self.metrics = model['metrics']

    def get_run_ids(self) -> list[str]:
        return self.run_ids

    def get_model_name(self) -> str:
        return self.model_name

    def get_folder_name(self) -> str:
        return self.folder_name

    def get_mapping_dict(self) -> dict[str, str]:
        return self.mapping_dict

    def get_run_label(self, run_id: str) -> str:
        return self.mapping_dict[run_id]

    def get_metrics(self) -> list[str]:
        return self.metrics
