"""Plot data class"""
import pandas as pd


class PlotData:
    """Plot data class"""
    def __init__(self, df: pd.DataFrame, metric_name: str, model_name: str, label: str):
        self.df = df
        self.metric_name = metric_name
        self.model_name = model_name
        self.label = label

    def get_df(self) -> pd.DataFrame:
        """Dataframe getter"""
        return self.df

    def get_metric_name(self) -> str:
        """Metric name getter"""
        return self.metric_name

    def get_model_name(self) -> str:
        """Model name getter"""
        return self.model_name

    def get_label(self) -> str:
        """Label getter"""
        return self.label
