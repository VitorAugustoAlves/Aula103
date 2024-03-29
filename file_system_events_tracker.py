import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir="C:/Users/tamir/Downloads"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Olá, {event.src_path} foi criado!")

    def on_deleted(self, event):
        print(f"Opa! Alguem excluiu {event.src_path}!")

    def on_moved(self, event):
        print(f"Opa! Alguem moveu {event.src_path}!")

    def on_modified(self, event):
        print(f"Opa! Alguem modificou {event.src_path}!")


#Professora Não estou conseguindo fazer o Observer

event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print('executando......')

except KeyboardInterrupt:
    print("interrompido!")
    observer.stop()