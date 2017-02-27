# djangolunch
## LunchBar backend (django version)

---
# Requirements

Python 3.5

# Environment Setup

Create virtual environment and activate it:

    python3.5 -m venv <your developing directory>
    source <your developing directory>/bin/activate

Initialize Git submodule:

    git submodule init

Put this repo in your developing directory.
Enter top directory:

    cd djangolunch/

Install Dependencies:

    pip install -r requirements.txt

Enter src directory:

    cd src/

Migrate the database:

    python manage.py migrate

Load fake data:

    python manage.py loaddata restaurants polls users orders

Enter vuelunch directory：

    cd vuelunch/

Install frontend dependencies:

    npm install

Build frontend files:

    npm run build

Go back to src directory:

    cd ../

Collect static files:

    python manage.py collectstatic

Now, run server:

    python manage.py runserver

And go to `127.0.0.1:8000/` to take a look!
Note that you can go to `127.0.0.1:8000/api/` to get full API list.

