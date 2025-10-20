source .venv/bin/activate
pip3 install -r cli/reporting/evaluation_scripts/requirements.txt

python -m cli.reporting.evaluation_scripts.variants_report
python -m cli.reporting.evaluation_scripts.data_plot