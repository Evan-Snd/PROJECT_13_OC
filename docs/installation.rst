Installation
============

Prerequisites
-------------

Before you begin, ensure you have met the following requirements:

- You have installed `Python 3.8+`_
- You have a `GitHub`_ account.
- You have installed `Docker`_ and `Docker Compose`_.
- You have installed `PostgreSQL`_ if you're not using Docker for the database.

Steps
-----

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/shmuel-bitan/Python-OC-Lettings-FR.git
      cd your-repository-name

2. Create a virtual environment and activate it:

   .. code-block:: bash

      python -m venv venv
      source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`

3. Install the dependencies:

   .. code-block:: bash

      pip install -r requirements.txt

4. Run the migrations and start the development server:

   .. code-block:: bash

      python manage.py migrate
      python manage.py runserver

5. (Optional) If you want to use Docker, build and run the Docker containers:

   .. code-block:: bash

      docker-compose up --build

Your project should now be running at `http://localhost:8000`.

