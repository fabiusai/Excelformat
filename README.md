# CSV-to-Excel Formatter Web App

Questa è una semplice web app in Flask che permette di caricare un file CSV e scaricare un file Excel formattato.

## Struttura del progetto

- **app.py**: server Flask con endpoint per upload e download.
- **formatta.py**: logica di formattazione CSV→Excel.
- **templates/index.html**: pagina HTML per l'upload.
- **requirements.txt**: dipendenze Python.
- **Procfile**: configurazione per deployment su Render/Heroku.

## Avvio in locale

```bash
git clone <repo-url>
cd my-web-app
pip install -r requirements.txt
flask run
```

Visita http://127.0.0.1:5000 per usare l'app.

## Deploy su Render

1. Crea un nuovo "Web Service" su Render.
2. Collega il tuo repository GitHub.
3. Imposta Branch (es. `main`) e Build Command (`pip install -r requirements.txt`).
4. Start Command: `gunicorn app:app`.
