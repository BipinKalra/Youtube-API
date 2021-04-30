# YOUTUBE API - PYTHON DJANGO

This project intends to fetch videos from Youtube based on a predefined search query (which can be user entered at a later stage). These videos are fetched from Youtube using the [Youtube Data API V3](https://developers.google.com/youtube/v3/getting-started). This api allows us to grab youtube videos in two simple steps -

- **[Search API](https://developers.google.com/youtube/v3/docs/search)** - This allows us to send a request with a given seach query and content requirement. The response contains a finite list of objects wherein each object contains basic information for each returned entity along with id.
- **[Video API](https://developers.google.com/youtube/v3/docs/videos)** - The video API returns detailed information for every video whose ID is recieved as a parameter in the request. These IDs can be collected from the response of the search API.

## BASIC WORKING

The main project folder has the following subfolders along with their individual purposes -

1. **"youtube_videos" Folder** - This is the main django project which holds all the major project settings. To keep the code both modular and easy to understand, most of the functionality resides within two different django apps installed in this django-project.
2. **"youtube" Folder** - This django application holds all the logic for fetching youtube videos every 1 minute and storing them inside the DB. This creates a cronjob in your system and thus, runs this process in the background.
3. **"api" Folder** - This contains an API made using Django Rest Framework which holds endpoints for both, requesting a paginated response for the search query and for searching videos on the basis of a search query.

## INSTALLATION

### Traditional Way

1. Clone the repository
2. Create a .env file using .env.sample and go on to add your YOUTUBE API KEY in the env file
3. Install [python](https://www.python.org/downloads/) and [pipenv](https://pypi.org/project/pipenv/) in your computer
4. Run "pipenv shell"
5. Run "pipenv install"
6. Run "python manage.py migrate"
7. Run "python manage.py crontab add"
8. Run "python manage.py runserver"
9. 6. Use the [Postman Collection](https://www.getpostman.com/collections/ff0912278d9bb3b84101) to interact with the two APIs

### Thats the way - **DOCKER WAY**

1. Clone the repository
2. Create a .env file using .env.sample and go on to add your YOUTUBE API KEY in the env file
3. Install [docker](https://www.docker.com/get-started) in your computer
4. Run "docker compose build"
5. Run "docker compose up"
6. Use the [Postman Collection](https://www.getpostman.com/collections/ff0912278d9bb3b84101) to interact with the two APIs

_If you are a windows user, I would highly recomment going the "Docker Way!" :)_

PS: Kindly let me know if you want me to send the API key that I used for development.
