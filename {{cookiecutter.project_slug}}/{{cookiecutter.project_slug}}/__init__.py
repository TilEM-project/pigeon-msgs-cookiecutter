from . import example

import importlib.metadata


__version__ = importlib.metadata.version("{{ cookiecutter.pypi_name }}")

topics = {
    "example.message": example.Message,
}


msgs = (topics, __version__)
