# Djitter

SNS template based on Djitter(https://github.com/tat3/djitter)

## Usage

```bash
git clone https://github.com/tat3/sns-template.git 
echo SECRET_KEY="anything" > .env
docker-compose build
docker-compose run app ./manage.py migrate
docker-compose up
docker exec -it sns-template_app_1 ./manage.py migrate
```
Then open http://localhost.

