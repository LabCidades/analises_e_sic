import os
import requests

def solve_dir(dir_name):
    '''Returns absolut path of dir. If dir does'nt exits,
    creates it.'''

    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    return os.path.abspath(dir_name)

def full_file_path(file, parent_dir):
    '''Returns full file path. If parent dir
    doest not exists, creates it.'''

    if parent_dir:
        parent_dir = solve_dir(parent_dir)

    file_path = os.path.join(parent_dir, file)

    return os.path.abspath(file_path)

def download_bin_file(url, file_name, save_dir):
    '''Downloads and save binary content from a url.
    Returns the full path of the saved file'''

    with requests.get(url) as r:

        content = r.content

    file_path = full_file_path(file_name, save_dir)
    with open(file_path, 'wb') as f:
        f.write(content)

    return file_path