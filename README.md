# SNS template

![image](https://user-images.githubusercontent.com/23653134/42412252-874dccd6-8243-11e8-84a4-4c5d1b8ff15a.jpg)

SNS template written in Python

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

