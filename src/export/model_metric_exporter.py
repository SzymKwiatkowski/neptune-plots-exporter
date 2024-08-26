"""Class for exporting model metrics to specified plots"""
import os
from pathlib import Path
import pandas as pd
from matplotlib import pyplot as plt

from parsing import ModelConfig
from export.plot_data import PlotData


class ModelMetricExporter:
    """Class for exporting model metrics to specified plots"""
    def __init__(self, model_configs: list[ModelConfig]):
        """Init exporter"""
        self.model_configs = model_configs

    def export_models(self, data_path: Path, output_dir: Path):
        """Export model metrics to specified plots"""
        plots_data = []
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        for model_config in self.model_configs:
            exporting_series = [
                PlotData(
                    self.read_pandas_df(data_path / model_config.get_folder_name(), run_id, metric),
                    metric,
                    model_name=model_config.get_model_name(),
                    label=model_config.get_run_label(run_id),
                )
                for run_id in model_config.get_run_ids()
                for metric in model_config.get_metrics()]
            plots_data += exporting_series

            grouped_data = {metric: [series
                            for series in exporting_series
                            if series.metric_name == metric]
                            for metric in model_config.get_metrics()}

            base_model_output_dir = output_dir / model_config.get_folder_name()
            if not os.path.exists(base_model_output_dir):
                os.mkdir(base_model_output_dir)

            for key, plot_datas in grouped_data.items():
                x = []
                y = []
                plt.figure()
                for plot_data in plot_datas:
                    numpy_data = plot_data.get_df().to_numpy()
                    x.append(numpy_data[:, 0])
                    y.append(numpy_data[:, 2])
                    plt.plot(numpy_data[:, 0], numpy_data[:, 2], label=plot_data.label)
                plt.legend()
                plt.title(key)
                out_file = base_model_output_dir / f'{key}.pdf'
                plt.savefig(out_file)

    @staticmethod
    def read_pandas_df(data_path_root: Path, run_id, metric_name: str) -> pd.DataFrame:
        """Reads pandas frame based on base path with run_id and metric_name"""
        filename = run_id + "__" + metric_name + ".csv"
        return pd.read_csv(data_path_root / filename)
