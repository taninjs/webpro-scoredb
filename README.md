# webpro-scoredb
Simple API and report for final exam testing (WEB PROGRAMMING 2018)

## Installation with Docker
```
# Download
git clone https://github.com/taninjs/webpro-scoredb.git

# Start the server
cd webpro-scoredb
docker-compose up -d

# View mysql log (hit ctrl-c to exit)
docker-compose logs -f db

# View django console (hit ctrl-c to exit)
docker-compose logs -f app

# If there is any error, try restarting the server.
docker-compose down
docker-compose up -d

# Migrate database
docker-compose exec app python manage.py migrate

# Create superuser
docker-compose exec app python manage.py createsuperuser

# Stop server
docker-compose down
```

## View Report
Visit [http://localthost:8888/admin](http://localhost:8888/admin)

## API for create score record
Find Postman examples in **postman/** folder
![Postman example 1](https://github.com/taninjs/webpro-scoredb/blob/master/postman1.png?raw=true)
![Postman example 2](https://github.com/taninjs/webpro-scoredb/blob/master/postman2.png?raw=true)

## Export CSV
Visit [http://localhost:8888/scores/report/](http://localhost:8888/scores/report/)

## Access Mysql Database
- HOST: localhost
- PORT: 33006
- ROOT_PASSWORD: secret
