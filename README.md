# 🗺️ Travel Planner API & Streamlit App

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-lightgrey)](https://flask.palletsprojects.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red)](https://streamlit.io/)

## 📖 About the Project

This project is a travel planning web application that combines a **Flask backend** (REST API) and a **Streamlit frontend**.  

It supports user registration, login, password reset, location management, route planning, preferences setup, weather information, and personalized recommendations.

The following use cases have been implemented:

- UC‑10: Determine & change location  
- UC‑40: Plan a route  
- UC‑50: Register new user  
- UC‑90: Reset password  
- UC‑60: Set up preferences  

---

## 🚀 Installation

### Prerequisites

Make sure you have **Python 3.8+** installed.

### Install required packages

You can install Flask and Streamlit using `pip`:


✅ Bereits implementierte Use Cases
UC‑10 – Standort feststellen und ändern (in routes/user_routes.py)
Methode	Endpunkt	Beschreibung
PUT	/users/standort	Standort ändern
GET	/users/standort	Standort feststellen
UC‑40 – Reise planen (in routes/route_routes.py und routes/user_routes.py)
Methode	Endpunkt	Beschreibung
GET	/route/plan	Route planen
POST	/users	Benutzer hinzufügen
UC‑50 & UC‑90 – Neu registrieren / Passwort zurücksetzen (in auth.py)
Methode	Endpunkt	Beschreibung
GET	/auth/users	Alle Benutzer anzeigen
GET, POST	/auth/login	Anmelden
GET	/auth/logout	Abmelden
POST	/auth/register	Neuen Benutzer registrieren
POST	/auth/reset-password	Passwort zurücksetzen
UC‑60 – Präferenzen einrichten (in recommendation.py)
Methode	Endpunkt	Beschreibung
GET	/recommendations/<int:user_id>	Empfehlungen abrufen
POST	/recommendations/<int:user_id>	Präferenzen aktualisieren
🌐 Weitere Endpoints
Methode	Endpunkt	Beschreibung
GET	/route/plan	Route planen (siehe UC‑40)
GET	/static/<path:filename>	Statische Dateien ausliefern
POST	/users	Benutzer hinzufügen
GET	/users/sprache	Sprache abrufen
PUT	/users/sprache	Sprache ändern
GET	/users/empfehlungen	Empfehlungen abgeben (Wetter)
GET	/wetter	Wetter abrufen

```bash
pip install flask
