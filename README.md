# Star Trek Script Writer

This is an automatic script writer for Star Trek. It's got a model of what a Star Trek script looks like, and tries to write its own. Right now the output is a bit disjointed or surreal.

## Quick Start

[Open the notebook on Kaggle](https://www.kaggle.com/alexcg1/trekbot-script-generator/). Ensure that GPU acceleration is enabled, otherwise it'll be really slow

## Run on your own machine

You can download the notebook from the [notebooks](./notebooks) folder and run in Colab, Kaggle, or on your own machine.ZZ

%%## Usage

%%### Download the script data

%%The script data comes from a [Kaggle dataset](https://www.kaggle.com/gjbroughton/start-trek-scripts). Download the file from there, unzip it, and move all_scripts_raw.json to this folder.

%%### Process the Data

%%Run `python process_data.py` to convert the JSON file to plain text that we can feed into the script writer.

%%### Generate Scripts

%%Run [trek_script_generation](trek_script_generation.ipynb) on a machine with a GPU. I wrote the notebook for Kaggle, so you may have to tweak it if you run on Google Colab or your own machine. On Kaggle, with one GPU, it takes about 4 hours to train on all the scripts.
