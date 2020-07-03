
from typing import Optional, Set, List, Union, Dict, Any
from .semqc_datamodel import KnowledgeSource, Registry
import subprocess
import logging

ReturnCode = int

class Syncer():
    """
    Syncs local cash with files in registry
    """

    def sync(self, r: Registry) -> ReturnCode:
        for src in r.has_knowledge_sources:
            self.sync_file(src)

    def sync_file(self, src: KnowledgeSource) -> ReturnCode:
        """
        Syncs a file with an upstream URL
        :param src:
        :return:
        """
        local_path = self.get_local_path(src)
        p = subprocess.run(f"curl -L -s {src.url} > {local_path}.tmp && mv {local_path}.tmp {local_path}")
        return p.returncode
