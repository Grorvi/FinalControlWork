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

### Задание 3

Подключить дополнительный репозиторий MySQL. Установить любой пакет
из этого репозитория

**Решение**

```
user@docker-server1:~$ sudo apt-get update
user@docker-server1:~$ sudo apt-get install mysql-server

done!
update-alternatives: используется /var/lib/mecab/dic/ipadic-utf8 для предоставления /var/lib/mecab/dic/debian (mecab-dictionary) в автоматическом режиме
Настраивается пакет libhtml-parser-perl:amd64 (3.76-1build2) …
Настраивается пакет libhttp-message-perl (6.36-1) …
Настраивается пакет mysql-server-8.0 (8.0.32-0ubuntu0.22.04.2) …
update-alternatives: используется /etc/mysql/mysql.cnf для предоставления /etc/mysql/my.cnf (my.cnf) в автоматическом режиме
Renaming removed key_buffer and myisam-recover options (if present)
mysqld will log errors to /var/log/mysql/error.log
mysqld is running as pid 12277
Created symlink /etc/systemd/system/multi-user.target.wants/mysql.service → /lib/systemd/system/mysql.service.
Настраивается пакет libcgi-pm-perl (4.54-1) …
Настраивается пакет libhtml-template-perl (2.97-1.1) …
Настраивается пакет mysql-server (8.0.32-0ubuntu0.22.04.2) …
Настраивается пакет libcgi-fast-perl (1:2.15-1) …
Обрабатываются триггеры для man-db (2.10.2-1) …
Обрабатываются триггеры для libc-bin (2.35-0ubuntu3.1) …
Scanning processes...                                                                                                                                           
Scanning linux images...                                                                                                                                        

Running kernel seems to be up-to-date.

No services need to be restarted.

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on this host.
```

### Задание 4

Установить и удалить deb-пакет с помощью dpkg.

**Решение**

````
sudo wget https://download.docker.com/linux/ubuntu/dists/jammy/pool/stable/amd64/docker-ce-cli_20.10.13~3-0~ubuntu-jammy_amd64.deb
sudo dpkg -i docker-ce-cli_20.10.133-0ubuntu-jammy_amd64.deb
sudo dpkg -r docker-ce-cli
````

**Задание 5**

Выложить историю команд в терминале ubuntu.

**Решение**

[Задача 1](#Задание-1)

[Задача 2](#Задание-2)

[Задача 3](#Задание-3)

[Задача 4](#Задание-4)
