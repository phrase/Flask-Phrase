Creating the virtual environment in the root folder:

1. `python -m venv env` Set up the virtual environment
2. `source env/bin/activate` Activate the environment

Once you have created the virtual environment in the parent folder:

1. Cd to this folder
2. run `pip install ../.` to install the local (most up to date) version of the integration
3. Run `flask --app demo run`
4. Navigate to `http://127.0.0.1:5000`
5. Login with `demo@phrase.com` / `phrase`
