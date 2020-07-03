
from .semqc_datamodel import Registry, KnowledgeSource
from dataclasses import dataclass, field
from typing import Optional, Set, List, Union, Dict, Any
import subprocess
from rdflib import Graph, Namespace
import logging

DCAT = Namespace('http://www.w3.org/ns/dcat#')

URL = str

@dataclass
class RegistryUtil():
    """
    wraps a registry
    """

    local_path : str
    registry_graph : Optional[Graph] = None

    def get_registry_graph(self) -> Graph:
        if self.registry_graph is None:
            self.registry_graph = Graph()
            self.registry_graph.parse(self.local_path, format='ttl') # TODO: do not hardcode format
        return self.registry_graph

    def sources(self) -> List[KnowledgeSource]:
        """
        returns a list of sources
        """
        g = self.get_registry_graph() # Graph
        srcs = []
        # TODO: allow for other schemas
        for _, _, url in g.triples((None, DCAT.distribution, None)):
            urlstr = str(url)
            ks = KnowledgeSource(id=urlstr,
                               url=urlstr)
            srcs.append(ks)
        return srcs

