Requisitos
• Docker ≥ 20.10
• Docker Compose ≥ 1.29

Pasos para poner en marcha
Clona este repositorio
git clone https://github.com/tu-usuario/tech_test_django.git
cd tech_test_django

Copia y edita el archivo de variables de entorno
cp .env.example .env
• Genera un valor seguro para DJANGO_SECRET_KEY:
openssl rand -base64 32
• Pega ese valor en la línea DJANGO_SECRET_KEY= de tu .env
• Asegúrate de que el resto de valores quede así:
DJANGO_DEBUG=True
POSTGRES_DB=tech_test_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_PASSWORD=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com

Construye las imágenes Docker
make build

Levanta los servicios en segundo plano
make up
• Arranca db (PostgreSQL) con volumen persistente
• Arranca web (Django + Gunicorn), aplica migraciones, crea superuser y recoge estáticos

Verifica que todo esté funcionando
docker compose ps
Debes ver los contenedores db y web en estado Up

Accede al panel de administración de Django
En el navegador, visita http://localhost:8000/admin/
• Usuario: admin
• Contraseña: admin

Comandos útiles
Tarea	Comando
Ver logs en tiempo real - make logs
Ejecutar migraciones manualmente - make migrate
Abrir shell de Django - make shell
Detener contenedores - make down
Detener y eliminar volúmenes - docker compose down -v

Estructura del proyecto:

tech_test_django/
├── core/ App vacía para tus modelos y vistas
├── tech_test_django/ Configuración de Django (settings, urls, wsgi, etc.)
├── Dockerfile
├── docker-compose.yml
├── entrypoint.sh
├── Makefile
├── requirements.txt
├── .env.example
└── README.md (este archivo)

Características destacadas

•Middleware de auditoría
•Validación de email único
•Auto-cálculo de fechas en ingresos