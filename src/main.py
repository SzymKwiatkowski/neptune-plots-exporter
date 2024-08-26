import argparse
from pathlib import Path

from utils.helpers import load_json
from parsing.config import Config
from export.model_metric_exporter import ModelMetricExporter


def main(args):
    """Main executable script"""
    config = Config(load_json(Path(args.config)))
    model_metric_exporter = ModelMetricExporter(config.get_model_configs())
    model_metric_exporter.export_models(Path(args.data_path), Path(args.output_path))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='NeptuneAi data exporter',
        description='Export csv dataseries downloaded from neptune.ai',
        epilog='Export data to pngs')
    parser.add_argument('-d', '--data-path', action='store', default='./data')
    parser.add_argument('-c', '--config', action='store', default='./data/config.json')
    parser.add_argument('-o', '--output-path', action='store', default='./out')
    args_parsed = parser.parse_args()
    main(args_parsed)
