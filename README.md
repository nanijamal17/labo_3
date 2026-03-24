# WebRTC Video Streaming avec Python

## Description du projet

Ce projet consiste à développer un système de streaming vidéo en temps réel entre deux programmes Python en utilisant la technologie **WebRTC**. Le serveur capture le flux vidéo provenant d'une webcam et le transmet au client via une connexion WebRTC. Le client reçoit ensuite les trames vidéo et les affiche dans une fenêtre graphique.

L'objectif principal de ce laboratoire est de comprendre les bases de la technologie **WebRTC**, la communication **client-serveur**, ainsi que la transmission de flux multimédia en temps réel.

---

# Technologies utilisées

Le projet utilise les technologies et bibliothèques suivantes :

- **Python**
- **aiortc** : implémentation WebRTC pour Python
- **OpenCV (opencv-python)** : capture et affichage du flux vidéo
- **asyncio** : gestion de la programmation asynchrone

---

# Architecture du système

Le système suit une architecture **client-serveur**.

Le serveur capture les images de la webcam et les transmet au client via WebRTC. Le client reçoit ces images et les affiche dans une fenêtre graphique.

Schéma de fonctionnement :

Webcam  
↓  
Serveur Python (OpenCV)  
↓  
WebRTC (aiortc)  
↓  
Client Python  
↓  
Affichage vidéo

---

# Structure du projet

PythonProject/

server.py  
client.py  
main.py  
README.md  

### server.py

Le serveur est responsable de :

- capturer les images de la webcam
- convertir les images en trames vidéo WebRTC
- négocier la connexion WebRTC avec le client
- transmettre les trames vidéo

### client.py

Le client est responsable de :

- initier la connexion avec le serveur
- recevoir les trames vidéo
- afficher la vidéo dans une fenêtre graphique

---

# Installation

## 1. Installer Python

Installer **Python 3.10 ou 3.11** recommandé.

---

## 2. Installer les dépendances

Dans un terminal :

```
pip install opencv-python
pip install aiortc
```

---

# Exécution du projet

## Étape 1 : lancer le serveur

Dans un premier terminal :

```
python server.py
```

Le serveur va :

- ouvrir la webcam
- attendre la connexion du client

---

## Étape 2 : lancer le client

Dans un second terminal :

```
python client.py
```

Le client va :

- se connecter au serveur
- recevoir les trames vidéo
- afficher la vidéo dans une fenêtre OpenCV

---

# Paramètres de connexion

Le projet utilise par défaut :

IP : 127.0.0.1  
Port : 9999  

Cela permet de tester le projet sur un seul ordinateur.

Pour utiliser deux ordinateurs différents sur le même réseau, il faut modifier l'adresse IP du serveur dans **client.py**.

Exemple :

```
server_ip = "192.168.1.10"
```

---

# Fonctionnement du serveur

Le serveur :

1. Capture les images de la webcam avec **OpenCV**
2. Convertit les images en trames vidéo compatibles WebRTC
3. Attend la connexion d'un client
4. Négocie la connexion WebRTC
5. Transmet les trames vidéo en continu

---

# Fonctionnement du client

Le client :

1. Se connecte au serveur
2. Négocie les paramètres WebRTC
3. Reçoit les trames vidéo
4. Convertit les trames en images
5. Affiche la vidéo avec OpenCV

---

# Problèmes rencontrés et solutions

### Problème : connexion refusée

Erreur :

```
ConnectionRefusedError
```

Cause possible :

- le serveur n'était pas lancé avant le client
- l'adresse IP ou le port étaient incorrects

Solution :

- lancer d'abord **server.py**
- vérifier que le client utilise la même IP et le même port.

---

# Améliorations possibles

Plusieurs améliorations peuvent être apportées :

- transmission audio
- interface graphique plus avancée
- support de plusieurs clients
- amélioration de la qualité vidéo
- compression vidéo plus efficace

---

# Auteur

NANA WANDA FRANCK
Baccalauréat en informatique
Université