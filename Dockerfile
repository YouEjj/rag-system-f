# Utiliser l'image de base de Python 3.12.0
FROM python:3.12.0

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le répertoire de travail
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source dans le conteneur
COPY . .

# Copier le dossier data dans le conteneur
COPY /src/data /app/data

# Spécifier la commande par défaut pour exécuter votre programme
CMD ["python", "src/main.py"]

