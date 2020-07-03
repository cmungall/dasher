
from .semqc_datamodel import Registry
from typing import Optional, Set, List, Union, Dict, Any
import subprocess
import logging

class Loader():
    """
    loads a set of files into a database, such as a triplestore
    """

    def load(self, registry: Registry) -> None:
        """
        currently only BG supported
        """
        None
