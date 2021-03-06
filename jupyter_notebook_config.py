# Reference: https://svds.com/jupyter-notebook-best-practices-for-data-science/
import os
from subprocess import check_call
from pathlib import Path

def post_save(model, os_path, contents_manager):
    """post-save hook for converting notebooks to html scripts"""
    if model['type'] != 'notebook':
        return # only do this for notebooks
    d, fname = os.path.split(os_path)
    name, ext = os.path.splitext(fname) 
    check_call(['jupyter', 'nbconvert', '--to', 'html', fname, '--template=ga.tpl'], cwd=d)

c.FileContentsManager.post_save_hook = post_save
