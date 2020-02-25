# Grupo 16

## Integrantes

- Gonzalo Bilbao 13317/1
- Federico Gasquez 13598/6
- Agustin Vanzato 14499/8

## Iniciar Base de datos

En el directorio raiz del proyecto se debe cambiar el nombre de `db-docker-compose.yml` por `docker-compose.yml` y ejecutar
```bash 
    $ docker-compose up
 ```

Para acceder a la administracion de la DB, en la direccion `localhost:5000`

    - Usuario: root
    - Password: pass

    - Usuario: user
    - Password: userpass

## Dependencias

 - Para reinstalar nuevas dependencias sin rebuildear el dockerfile, correr el comando
    ```bash
        $ docker-compose exec web pip install -r requirements.txt
    ```

Posibles errores: 

- La contraseña no es correcta
    - En el directorio raiz del proyecto y con el docker levantado, correr el siguiente comando

    ```bash 
        $ docker-compose exec db '/usr/bin/mysqladmin' -u root password 'pass'
    ```