The idea with this repo is to have a template for a Flask app that exists in a package.  The package will, therefore, be pip installable.

After cloning the repo with `git clone git@github.com:umrosbrian/flask_package_template`, the `.git` directory can be removed with `rm -rf .git`.  Rename the `flask_package_template` directory to your new package name, and CD into it.  The directory `src/pkg` needs to be renamed to the package name along with the imports in `src/pkg/__init__.py` and `src/pkg/routes.py`  A new repo can then be initialized and the package can be locally installed with `pip install -e <path_to_repo>`.

Because `.flaskenv` assigns and exports `FLASK_APP`, you just need to activate the virtual environment, CD to the repo and issue `flask run`.
