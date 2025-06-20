from setuptools import setup

APP = ['Model/data_visualizer.py']  # Einstiegspunkt anpassen!
OPTIONS = {
    'argv_emulation': True,
    'packages': ['tkinter'],
    'compressed': False,  # <- wichtig!
    'optimize': 0,
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)