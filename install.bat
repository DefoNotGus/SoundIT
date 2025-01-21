@echo off
REM Batch file to set up the project

REM Create a virtual environment in a hidden .venv folder
python -m venv .venv

REM Activate the virtual environment
call .venv\Scripts\activate

REM Install the required dependencies
pip install -r requirements.txt

REM Deactivate the virtual environment
call .venv\Scripts\deactivate

echo Setup complete. Use the command "call .venv\Scripts\activate" to activate the virtual environment.