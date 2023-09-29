### Запуск проекта

Выполнить команду

```git
git clone https://github.com/Ivandrobyshevv/Animal-registration-system/tree/web-project
```

В корне проекта создать файл .env

```dotenv
MONGO_USER=root
MONGO_PASS=password
MONGO_DB=rootDB
MONGODB_URL=mongodb://root:rootDB@mongodb/?retryWrites=true&w=majority
```

Запустить проект в докере

```docker
docker-compose up -d --build
```