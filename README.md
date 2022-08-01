# Scrape YouTube Video


```doctest
docker-compose up -d
docker exec -it syv-backend python manage.py makemigrations
docker exec -it syv-backend python manage.py migrate
docker exec -it syv-backend python manage.py process_tasks
```
