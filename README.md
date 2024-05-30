The idea with this repo is to have a template for a Flask app that exists in a package.  The package will, therefore, be pip installable.

## make a new repo/package from this repo

1. `git clone git@github.com:umrosbrian/flask_package_template`
2. Rename the `flask_package_template` directory to the name of the package you'll be creating.
3. CD to the directory and remove the `.git` directory with `rm -rf .git`.
4. The directory `src/pkg` needs to be renamed to the package name along with the imports in `start_server.py`, the line `src/pkg.egg-info` in `.gitignore`, `src/pkg/__init__.py` and `src/pkg/routes.py`.  This can all be done using ` python <path to pyutils/recursively_replace.py> --path . --old_string pkg --new_string <new package name> --ignore README. md .git --all`. A new repo can then be initialized and the package can be locally installed with `pip install -e <path_to_repo>`.

Because `.flaskenv` assigns and exports `FLASK_APP`, you just need to activate the virtual environment, CD to the repo and issue `flask run`.

## blueprints

The `flask_package_template/src/pkg/bp_1` directory is a sub-package that is a blueprint.  This directory can be copied and the `bp_1` replaced with a new name to create another blueprint; we'll call this *new name* for the remainder if this section.  If you need a base template for the blueprint, you can copy `pkg/src/pkg/templates/bp_1_base.html` and rename the file by replacing 'bp_1' with the new name.  After doing this, you can copy `pkg/src/pkg/templates/bp_1` and rename it to the new name.  The files in the copied directories will need to be modified using the 
new name, which can be done with `pyutils/recursively_replace.py --path <repo's root path> --old_string bp_1 --new_string <new name>`.

In `flask_package_template/src/pkg/bp_1/__init__.py`, a Blueprint class object is created, which is then imported in `flask_package_template/src/pkg/__init__.py`.  `flask_package_template/src/pkg/main` is a blueprint too but in `/flask_package_template/src/pkg/__init__.py`, the blueprint is registered without a `url_prefix` parameter and value so the index of that blueprint is in `flask_package_template/src/pkg/templates` rather than in a subdirectory of that 
directory.