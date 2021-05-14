#!/usr/bin/env python3
import os
import requests
import argparse
from config.config import *


def core():
       config_creacion = argparse.ArgumentParser( description="Crear repos desde el CLI !!!")
       config_creacion.add_argument("--nombre", "-n", type=str, dest="nombre", required=True, help="Nombre del repo a crear.")
       config_creacion.add_argument("--privado", "-priv", dest="es_privado", action="store_true", help="Indicamos si queremos que sea Privado agregando --privado o -priv solamente.")
       config_creacion.add_argument("--descripcion", "-d", type=str, dest="descripcion", required=False, help="Descripcion breve del repo a crear.")
       configs     = config_creacion.parse_args()
       repo_nombre = configs.nombre
       es_privado  = configs.es_privado
       descripcion = configs.descripcion


       if es_privado:
           enviar_carga = '{"name": "' + repo_nombre + '", "private": true, "description": "'+ descripcion +'" }'
       else:
           enviar_carga = '{"name": "' + repo_nombre + '", "private": false,"description": "'+ descripcion +'" }'

       cabeceras = {
           "Authorization": "token " + TOKEN,
           "Accept": "application/vnd.github.v3+json"
       }

       try:
           r = requests.post( API_URL + "/user/repos", headers=cabeceras, data=enviar_carga )
           r.raise_for_status()
       except requests.exceptions.RequestException as error:
           raise SystemExit(error)

       try:
           os.chdir(UBICACION_REPOSITORIO)
           os.system("mkdir " + PREFIJO + repo_nombre)
           os.chdir( UBICACION_REPOSITORIO + PREFIJO + repo_nombre )
           os.system("git init")
           os.system("echo '# Creado de manera automatica para el repositorio : " + repo_nombre +"' >> README.md")
           os.system("git add . && git commit -m Automatico")
           os.system("git branch -M main")
           os.system("git remote add origin git@github.com:" + USUARIO + "/" + repo_nombre + ".git")
           os.system("git push -u origin main")
           os.system("git branch dev && git branch test && git branch qa")

       except FileExistsError as error:
           raise SystemExit(error)



if __name__ == "__main__":
    core()
