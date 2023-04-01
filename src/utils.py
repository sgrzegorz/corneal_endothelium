import os

def root_dir():
  return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# path from project root
def path_root(*args):
  return os.path.abspath(os.path.join(root_dir(),*args))

# path from current dir
def path(*args):
  return os.path.abspath(os.path.join(*args))
