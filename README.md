# Итогова аттестация

## Задание

### Задание 1

Используя команду cat в терминале операционной системы Linux, создать
два файла Домашние животные (заполнив файл собаками, кошками,
хомяками) и Вьючные животными заполнив файл Лошадьми, верблюдами и
ослы), а затем объединить их. Просмотреть содержимое созданного файла.
Переименовать файл, дав ему новое имя (Друзья человека).

**Решение**

```
user@docker-server1:~/GB$ cat > home_amimals
dogs, cats, hamsters

user@docker-server1:~/GB$ cat > pack_animals
Horses, camels and donkeys

user@docker-server1:~/GB$ ls
home_amimals  pack_animals

user@docker-server1:~/GB$ cat home_amimals pack_animals > Mans_friends
user@docker-server1:~/GB$ cat Mans_friends 
dogs, cats, hamsters
Horses, camels and donkeys
```

### Задание 2

Создать директорию, переместить файл туда.

**Решение**

```
user@docker-server1:~$ mkdir dir_file
user@docker-server1:~$ ls
dir_file  file_1

user@docker-server1:~$ mv file_1 dir_file/
user@docker-server1:~$ ls
dir_file

user@docker-server1:~$ ls dir_file/
file_1

```