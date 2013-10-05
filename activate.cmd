PUSHD %~dp0
IF EXIST .venv GOTO ACTIVATE
python -mvenv .venv
curl -o .venv\distribute_setup.py http://python-distribute.org/distribute_setup.py
.venv\Scripts\python .venv\distribute_setup.py
.venv\Scripts\easy_install pip
.venv\Scripts\pip install -r requirements.txt
:ACTIVATE
CALL .venv\Scripts\activate.bat
POPD