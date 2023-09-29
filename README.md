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