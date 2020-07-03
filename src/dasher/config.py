
from .semqc_datamodel import Registry, MetricCollection
from dataclasses import dataclass, field
from typing import Optional, Set, List, Union, Dict, Any
import subprocess
from rdflib import Graph, Namespace
import logging

URL = str

@dataclass
class Config():
    """
    configuration for a dashboard.

    This can be subclasses OR composition can be employed
    """

    registry: Optional[Registry] = None
    metric_collection: Optional[MetricCollection] = None

