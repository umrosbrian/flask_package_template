The idea with this repo is to have a template for a Flask app that exists in a package.  The package will, therefore, be pip installable.

After cloning the repo with `git clone git@github.com:umrosbrian/flask_package_template`, the `.git` directory can be removed with `rm -rf .git`.  A new repo can then be initialized.

Because `.flaskenv` assigns and exports `FLASK_APP`, you just need to activate the virtual environment, CD to the repo and issue `flask run`.