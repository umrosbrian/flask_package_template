The idea with this repo is to have a template for a Flask app that exists in a package.  The package will, therefore, be pip installable.

After cloning the repo with `git clone git@github.com:umrosbrian/flask_package_template`, rename the `flask_package_template` directory to the name of the package you'll be creating.  CD to the directory and remove the `.git` directory with `rm -rf .git`.  The directory `src/pkg` needs to be renamed to the package name along with the imports in `start_server.py`, the line `src/pkg.egg-info` in `.gitignore`, `src/pkg/__init__.py` and `src/pkg/routes.py`.  A new repo can then be initialized and the package can be locally installed with `pip install -e <path_to_repo>`.

Because `.flaskenv` assigns and exports `FLASK_APP`, you just need to activate the virtual environment, CD to the repo and issue `flask run`.

## blueprints

The `flask_package_template/src/pkg/bp_1` directory is a sub-package that is a blueprint.  This directory can be copied and the `bp_1` replaced with a new name to create another blueprint.  In `flask_package_template/src/pkg/bp_1/__init__.py`, a Blueprint class object is created, which is then imported in `flask_package_template/src/pkg/__init__.py`.