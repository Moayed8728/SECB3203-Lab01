# SECB3203 Lab 1 - Python fundamentals and a reproducible project

Student: Moayed Mohamed Saleh (A24CS0017)

## Setup
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt

Linux:
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt

## Run
python -m pytest
ruff check src
python src/env_check.py > results/environment_report.txt

## What is in this repository
src/	                    Contains Python source code
tests/	                    Contains automated tests
data/	                    Contains original, read-only input files
results/	                Stores generated output reports
src/env_check.py	        Reports Python, operating system, and package versions
src/basics.py	            Calculates GC percentages, formats reports, and parses counts
tests/test_lab01_own.py	    Contains the three or more tests you write
README.md	                Documents how to set up and run the project
requirements-frozen.txt	    Records the installed package versions
AI_USE_LOG.md	            Records and declares your AI usage

## What is not committed, and why
Git didnt commit .venv/, results/, cache folders, and .env

Committing them could add unnecessary files, or expose sensitive information