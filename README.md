# Scrape YouTube Video

### Project Setup
1. `git clone https://github.com/tahmid-tanzim/scrape-youtube-video.git`
2. `cd scrape-youtube-video`
3. `cp .env.example .env`
4. `vim .env`
5. update environment variable i.e. YOUTUBE_API_KEY 
6. `docker-compose up -d`
7. `docker exec -it syv-backend python manage.py makemigrations`
8. `docker exec -it syv-backend python manage.py migrate`
9. `docker exec -it syv-backend python manage.py process_tasks`


### API Documentation
| #   | HTTP Verb | Request URL                                                  | Remarks                                             |
|:---:|:----------|:-------------------------------------------------------------|:----------------------------------------------------|
| 1   | GET       | http://localhost:8000/api/tags                               | Get all tags                                        |
| 2   | GET       | http://localhost:8000/api/videos?score_order=ASC&tags=4,5,7  | Filter videos by tags and sort by performance score | 


### Web Application
URL - http://localhost:3000


### TIPS: 
If background task runs multiple times per second after setting up schedule and repeat
```doctest
docker exec -it syv-backend python manage.py shell
from background_task.models import Task
Task.objects.all().delete()
exit()
```