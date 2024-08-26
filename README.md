# Neptune Logger Plots Viewer
Repository created for viewing metrics using .csv files 
provided from neptune.ai website when using logger.

## Using repository
To use exporter prepare setup file based on example provided in templates.
By default, file is plotting results for each metric and saves it as individual plots eg.
When evaluating ResNet18 model for 2 different runs and 4 metrics used in each run
you need to provide data config file as follows:
```json
{
  "models": [
    {
      "model_name": "ResNet 18", // Display model name
      // Folder in data directory in which data is stored
      "folder_name": "res18",
      "run_ids": [ // run ids (coming from neptune)
        "SIM-75",
        "SIM-138"
      ],
      "mapping_dict": { // specify mapping between run_id and label on plot
        "SIM-75":  "",
        "SIM-138": "Full"
      },
      "metrics": [ // Metrics to export
        "metrics_pooled_iou",
        "metrics_pooled_val_iou",
        "metrics_pooled_ce_loss",
        "metrics_pooled_val_ce_loss"
      ]
    }
  ]
}
```
This setup will result in 4 different plots with data for each run as individual
series on it.

Then to run script use:
```bash
python3 main.py -d ../data -c ../data/config.json -o ../out
```
This should load data placed in created `data` directory using information provided in `config.json` file and
save it to `out` directory.

## Pylint
For linux bash pylint is supported via command:
```bash
bash pylint.sh
```

Either way add pylint to IDE or editor to work with project without failing on push.