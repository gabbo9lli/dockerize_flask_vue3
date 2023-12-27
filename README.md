# dockerize_flask_vue3
dockerize flask vuejs3 single page app

# comandi backend
docker-compose build

docker-compose up -d

Questi comandi avviano il container flask + nginx + gunicorn

# comandi frontend vuejs3

cd services/client

npm run dev

Poi ci si collega all'indirizzo http://localhost:5173/ e si naviga la single page app.

La guida di riferimento è a questo indirizzo

https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/