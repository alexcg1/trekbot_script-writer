# Star Trek Script Writer

## Usage

### Download the script data

The script data comes from a [Kaggle dataset](https://www.kaggle.com/gjbroughton/start-trek-scripts). Download the file from there, unzip it, and move all_scripts_raw.json to this folder.

### Process the Data

Run `python process_data.py` to convert the JSON file to plain text that we can feed into the script writer.

### Generate Scripts

Run [trek_script_generation](trek_script_generation.ipynb) on a machine with a GPU. I wrote the notebook for Kaggle, so you may have to tweak it if you run on Google Colab or your own machine. On Kaggle, with one GPU, it takes about 4 hours to train on all the scripts.
