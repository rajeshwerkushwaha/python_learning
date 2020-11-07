This simple Python project shows hows to use Docker Compose. 
The app uses Flask framework and stores the data in Redis database.

## Prerequisites
Make sure you have already installed both [Docker Engine](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)

#### To start the project run this command:
```
$ docker-compose up -d
```

#### To see the result
Enter http://localhost:5000/ on your browser

#### To stop the project run this command:
```
$ docker-compose stop
```

#### To remove the Redis data as well run this command:
```
$ docker-compose down --volumes
```

### Huge thanks to Docker source:
https://docs.docker.com/compose/gettingstarted/
