# Utilisation de l'image Python officielle depuis Docker Hub
FROM python:3.14.0a4-bullseye

# Configuration des variables d'environnement
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV dsn='https://dad493db3071b33b9f98468411458e50@o4507339445895168.ingest.de.sentry.io/4507696103489616'
# Définir le répertoire de travail
WORKDIR /code

# Installation des dépendances
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copier le projet
COPY . /code/

# Collecte des fichiers statiques
RUN python manage.py collectstatic --noinput

# Exposer le port 8000
EXPOSE 8000

# Commande pour démarrer l'application
CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]
