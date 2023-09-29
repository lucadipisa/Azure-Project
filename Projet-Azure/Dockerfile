# Utilisez une image Python pour votre application
FROM python:3.11

# Créez un répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers de votre application dans le conteneur
COPY . .

# Installez les dépendances
RUN pip install -r requirements.txt

# Exécutez votre application Flask
CMD ["python", "app.py"]
