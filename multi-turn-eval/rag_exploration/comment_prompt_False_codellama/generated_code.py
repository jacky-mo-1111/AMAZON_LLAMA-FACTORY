import os
import fnmatch

def search_files(dir_path, extension):
    files = os.listdir(dir_path)
    matching_files = []
    for file in files:
        if fnmatch.fnmatch(file, '*.' + extension):
            matching_files.append(file)
    return matching_files

# Example usage:
print(search_files('path/to/directory', 'txt'))

import requests
from bs4 import BeautifulSoup

def crawl_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    html = soup.prettify()
    with open('output.html', 'w') as f:
        f.write(html)

import requests
from bs4 import BeautifulSoup

def scrape_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = ' '.join([tag.text for tag in soup.find_all(text=True)])
    with open('output.txt', 'w') as f:
        f.write(text)

import subprocess
import pwd

def create_user(username):
    home_dir = pwd.getpwnam(username).pw_dir
    subprocess.check_call(['useradd', '--home-dir', home_dir, username])

import hashlib

def password_manager(app_name):
    passwords = {
        'gmail': 'password123',
        'facebook': 'password456',
        'twitter': 'password789',
    }
    password = passwords.get(app_name)
    if password:
        return hashlib.sha256(password.encode('utf-8')).hexdigest()
    else:
        return None