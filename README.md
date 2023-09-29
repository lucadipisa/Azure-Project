
# Azure - Project

Problèmatique : Comment gérer un grand flux d'utilisateur sur une application de réservation pour un restaurant ?
## Fonctionnement application

![App Screenshot](https://i.postimg.cc/m2Yq4p1W/image.png)
## App Services

![App Screenshot](https://i.postimg.cc/yNvmLRd2/photo-2023-09-29-14-00-47.jpg)
J'ai commencé par créér un App Services afin de déployer mon application Python.
J'ai utilisé Docker pour la création de l'image que j'ai ensuite indiqué dans App Services grâce à Docker Hub :

![App Screenshot](https://i.postimg.cc/rmdKkRVd/image.png)

## Application (arborescence et codes)

![App Screenshot](https://i.postimg.cc/VNkgPwJS/image.png)

Résultat : 
![App Screenshot](https://i.postimg.cc/9MdTSNc8/image.png)

## Azure SQL

- Création d'une BDD SQL avec Azure portal
- Création de la table emails

## Modification du code 

![App Screenshot](https://i.postimg.cc/L4WKNz9P/image.png)

Erreur lors du push : 
![App Screenshot](https://i.postimg.cc/zfHRHwGk/image.png)

## Identification problème

![App Screenshot](https://i.postimg.cc/xTs0Ydz2/image.png)
Pour la connexion, on va utiliser pyodb qui et bien installé

Logs :
![App Screenshot](https://i.postimg.cc/1Rk4gBRz/image.png)

