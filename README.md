# Scrape YouTube Video

### Project setup
1. `git clone https://github.com/tahmid-tanzim/scrape-youtube-video.git`
2. `cd scrape-youtube-video`
3. `cp .env.example .env`
4. `vim .env`
5. update YOUTUBE_API_KEY environment variable
6. `docker-compose up -d`
7. `docker exec -it syv-backend python manage.py makemigrations`
8. `docker exec -it syv-backend python manage.py migrate`
9. `docker exec -it syv-backend python manage.py process_tasks`


### API Doc
```doctest
http://localhost:8000/api/tags
http://localhost:8000/api/videos/DESC/<tags>
```


### TIPS: 
If background task runs multiple times per second after setting up schedule and repeat
```doctest
docker exec -it syv-backend python manage.py shell
from background_task.models import Task
Task.objects.all().delete()
exit()
```