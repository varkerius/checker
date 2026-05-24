# 🌦️ Travel & Weather App

Eine Flask + Streamlit Anwendung für Benutzerverwaltung, Wetterdaten und Routenplanung.  
Das Projekt ist mit Blueprints strukturiert und folgt einer modularen Backend-Architektur.

---

# 🚀 Funktionen

- 👤 Benutzerregistrierung, Login und Logout  
- 🔐 Passwort-zurücksetzen Funktion  
- 🌍 Verwaltung des Benutzerstandorts  
- 🧭 Routenplanungssystem  
- 🌤️ Wetterinformationen und Empfehlungen  
- ⚙️ Benutzerpräferenzen-System  
- 📊 Modulare Flask Blueprint-Architektur  
- 🖥️ Streamlit-Frontend-Oberfläche  

---

# ⚙️ Implementiert
- UC-10 Standort feststellen und ändern
- UC-20 Sprache anpassen
- UC-30 Transport- und Ausrüstungsempfehlung abgeben
- UC-40 Reise planen
- UC-50 Neu registrieren
- UC-60 Präferenzen einrichten
- UC-90 Passwort zurücksetzen


# 📦 Project Structure


```bash

.
├── main.py                 # Einstiegspunkt der Flask-Anwendung (Backend-Server, API)
├── app.py                  # Einstiegspunkt für Streamlit (Frontend/UI)
├── auth.py                 # Authentifizierung: Login, Registrierung, Logout, Passwort-Reset
│
├── services/               # Business-Logik (keine HTTP-Routen)
│   ├── routing_service.py  # Logik für Routenplanung und Reiseberechnung
│   ├── user_service.py     # Benutzerverwaltung und Nutzeroperationen
│   ├── weather_service.py  # Verarbeitung und Abruf von Wetterdaten
│
├── routes/                 # API-Endpunkte (Flask Blueprints)
│   ├── user_routes.py      # Benutzer-Endpunkte (Profil, Sprache, Standort)
│   ├── route_routes.py     # Routenplanung-Endpunkte
│   └── weather_routes.py   # Wetter-Endpunkte und Empfehlungen
│
├── recommendation.py       # Präferenzen-System und personalisierte Empfehlungen
│
├── static/                 # Statische Dateien (CSS, Bilder, JS)
│
└── README.md               # Projektdokumentation (Beschreibung, Installation, Nutzung)


Endpoint                             Methods    Rule                          
-----------------------------------  ---------  ------------------------------
UC-10 Standort feststellen und ändern in routes/user_routes.py:
   user_routes.standort_aendern         PUT        /users/standort               
   user_routes.standort_feststellen     GET        /users/standort

UC-40 Reise planen in routes/route_routes.py and routes/user_routes.py: 
   route_routes.route_planen            GET        /route/plan                   
   user_routes.add_user                 POST       /users

UC-50 Neu Regestrieren, UC-90 Passwort zurücksetzen in auth.py: 
   auth.get_users                       GET        /auth/users                   
   auth.login                           GET, POST  /auth/login                   
   auth.logout                          GET        /auth/logout                  
   auth.register                        POST       /auth/register                
   auth.reset_password                  POST       /auth/reset-password

UC-60 Präferenzen einrichten in recommendation.py: 
   recommendations.get_recommendations  GET        /recommendations/<int:user_id>
   recommendations.update_preferences   POST       /recommendations/<int:user_id>   
