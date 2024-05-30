The idea with this repo is to have a template for a Flask app that exists in a package.  The package will, therefore, be pip installable.

## make a new repo/package from this repo

1. `git clone git@github.com:umrosbrian/flask_package_template`
2. Rename the `flask_package_template` directory to the name of the package you'll be creating; we'll call this *package name*.
3. Remove the `.git` directory with `rm -rf <package name>/.git`.
4. The directory `src/pkg` needs to be renamed to the package name along with the imports in `start_server.py`, the line `src/pkg.egg-info` in `.gitignore`, `src/pkg/__init__.py` and `src/pkg/routes.py`.  This can all be done using ` python <path to pyutils/recursively_replace.py> --path <package name> --old_string pkg --new_string <package name> --all --dry_run`.  Remove `--dry_run` to do the actual replacements if all looks good.
5. Locally install the package with `pip install -e ./<package name>`.
6. A new repo can then be initialized if needed.

Because `.flaskenv` assigns and exports `FLASK_APP`, you just need to activate the virtual environment, CD to the package directory and issue `flask run`.

## blueprints

The `<package name>/src/pkg/bp_1` directory is a sub-package that is a blueprint.  The directory is a template for creating new blueprints.  Here's how you'd do that:
1. Copy `<package name>/src/<package name>/bp_1` and give it a new name; we'll call this *new name* for the remainder if this section.
2. Copy `<package name>/src/<package name>/templates/bp_1`, giving it the new name.
3. If you need a base template for the blueprint, you can copy `<package name>/src/<package name>/templates/bp_1_base.html` and rename the file by replacing 'bp_1' with the new name.
4. The files in the copied directories will need to be modified using the new name.  CD to the <package name> root and issue `pyutils/recursively_replace.py --path <repo's root path> --old_string bp_1 --new_string <new name> --dry_run`.  Remove `--dry_run` if everything looks good.
5. `flask run` to test that things are working after adding the blueprint.

In `flask_package_template/src/pkg/bp_1/__init__.py`, a Blueprint class object is created, which is then imported in `flask_package_template/src/pkg/__init__.py`.  `flask_package_template/src/pkg/main` is a blueprint too but in `/flask_package_template/src/pkg/__init__.py`, the blueprint is registered without a `url_prefix` parameter and value so the index of that blueprint is in `flask_package_template/src/pkg/templates` rather than in a subdirectory of that 
directory.