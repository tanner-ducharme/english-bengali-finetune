## Instructions for running our code

Install the requirements from our requirements.txt

### Seq2Seq models

### Gemma models
The Gemma notebook for our best experiment is `gemma7b - best experiment.ipynb`
it's best run on google colab as a notebook, but a python file version has been made available (although you might have to tweak to get it to work with your GPU)

The notebooks from our other experiments can be found in `/other notebooks/`, but these have not been fully cleaned and/or commented
More detailed instructions on the running the code can be found within the notebook.

### BLEU score
The script we used to calculate BLEU score is multi-bleu-detok.pl.
We use it as follows: perl multi-bleu-detok.pl -lc <reference_file> < <hypothesis_file>.
The -lc flag is optional

If the data is provided as a csv file in the form: Source, target, prediction, 
Then we can calculate the BLEU score by running:
./docwise <csv_file> <name_for_reference_file> <name_for_hypothesis_file>

### Visualizations
All graphs were generated using tensorboard. The tensorboard files are automatically created in the `results/exp_name/runs/` folder
