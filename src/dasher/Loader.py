
from typing import Optional, Set, List, Union, Dict, Any
import subprocess
import logging

Source = str
ReturnCode = int

class Loader():
    """
    loads a set of files into a database, such as a triplestore
    """

    def load(self, src: Source) -> ReturnCode:
        """
        Syncs a file with an upstream URL
        :param src:
        :return:
        """
        local_path = self.get_local_path(src)
        url = self.get_url(src)
        p = subprocess.run(f"curl -L -s {url} > {local_path}.tmp && mv {local_path}.tmp {local_path}")
        return p.returncode
