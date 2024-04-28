#libira by fuflik

import platform  # Platform detection / Обнаружение платформы
import random  # Random number generation / Генерация случайных чисел
import libira  # Custom module / Пользовательский модуль
import shutil  # File operations / Операции с файлами
import socket  # Network operations / Сетевые операции
import subprocess  # Subprocess execution / Выполнение подпроцессов
import os  # Operating system operations / Операции с операционной системой
import time  # Time-related operations / Операции, связанные со временем
import psutil  # Process utilities / Утилиты процессов
import pygetwindow  # Window management / Управление окнами
import webbrowser  # Web browser control / Управление веб-браузером

class RandomNum:  # Random number generator class / Класс генератора случайных чисел
    def __init__(self):
        self.num = random.randint(1, 100)

def init():  # Initialization function / Функция инициализации
    libira.rn = RandomNum()

def rn():  # Random number getter function / Функция получения случайного числа
    if not hasattr(libira, 'rn'):
        init()
    return libira.rn

def run(file_path):  # Execute Python file / Выполнить файл Python
    try:
        subprocess.run(['python', file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the file: {e}")

def cmd(command):  # Execute shell command / Выполнить команду оболочки
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing the command: {e}")

def copy(source_path):  # Copy file / Скопировать файл
    try:
        shutil.copy(source_path, "temp_copy")
    except FileNotFoundError:
        print(f"File not found: {source_path}")
    except PermissionError:
        print("Permission denied to copy the file.")

def paste(destination_path):  # Paste file / Вставить файл
    try:
        shutil.move("temp_copy", destination_path)
    except FileNotFoundError:
        print(f"Destination directory not found: {destination_path}")
    except PermissionError:
        print("Permission denied to paste the file.")

def system_info():  # Get system information / Получить информацию о системе
    info = {}
    info['system'] = platform.system()
    info['node'] = platform.node()
    info['release'] = platform.release()
    info['version'] = platform.version()
    info['machine'] = platform.machine()
    info['processor'] = platform.processor()
    info['ip_address'] = socket.gethostbyname(socket.gethostname())
    return info

def shutdown_system():  # Shutdown the system / Выключить систему
    if platform.system() == "Windows":
        try:
            subprocess.run(["shutdown", "/s", "/t", "0"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while shutting down the system: {e}")
    else:
        print("Shutdown command is not supported on this operating system.")

def screate(file_name, content):  # Create file with content / Создать файл с содержимым
    try:
        with open(file_name, 'w') as f:
            f.write(content)
        print(f"File '{file_name}' created successfully.")
    except IOError:
        print(f"")

def block(application_name):  # Block application / Заблокировать приложение
    try:
        with open("blocked_apps.txt", "a") as file:
            file.write(application_name + '\n')
        print(f"Application '{application_name}' has been blocked.")
    except Exception as e:
        print(f"Error occurred while blocking application: {e}")

def unblock(application_name):  # Unblock application / Разблокировать приложение
    try:
        with open("blocked_apps.txt", "r") as file:
            lines = file.readlines()
        with open("blocked_apps.txt", "w") as file:
            for line in lines:
                if line.strip() != application_name:
                    file.write(line)
        print(f"Application '{application_name}' has been unblocked.")
    except Exception as e:
        print(f"Error occurred while unblocking application: {e}")

def delete(file_path):  # Delete file / Удалить файл
    try:
        os.remove(file_path)
        print(f"File '{file_path}' has been deleted.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except PermissionError:
        print(f"Permission denied to delete the file: {file_path}")

def off(time_to_shutdown):  # Shutdown system after specified time / Выключить систему через определенное время
    try:
        time_to_shutdown = int(time_to_shutdown)
        if time_to_shutdown <= 0:
            print("Please provide a positive integer value for time.")
            return
        print(f"System will shutdown in {time_to_shutdown} seconds.")
        time.sleep(time_to_shutdown)
        shutdown_system()
    except ValueError:
        print("Invalid input. Please provide an integer value for time.")

def open_url(url):  # Open URL in default web browser / Открыть URL в браузере по умолчанию
    try:
        webbrowser.open(url)
        print(f"Opening URL: {url}")
    except Exception as e:
        print(f"Error occurred while opening URL: {e}")

def close_url(url):  # Close browser tab by URL / Закрыть вкладку браузера по URL
    try:
        for window in pygetwindow.getAllWindows():
            if "chrome" in window.title.lower() or "firefox" in window.title.lower():
                window.activate()
                time.sleep(0.5)
                window.close()
        print(f"Closing browser tab with URL: {url}")
    except Exception as e:
        print(f"Error occurred while closing URL: {e}")

# Example usage of screate function
libira.screate("", "")

# This code will only be executed when the file is run directly, not when imported
if __name__ == "__main__":
    # Example usage of shutdown_system function
    shutdown_system()
