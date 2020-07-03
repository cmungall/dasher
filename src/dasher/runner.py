
from dataclasses import dataclass, field
from .config import Config
from .syncer import Syncer
from .loader import Loader
from .semqc_datamodel import Registry, MetricCollection, Metric, KnowledgeSource
from .registry_util import RegistryUtil
from typing import Optional, Set, List, Union, Dict, Any
import subprocess
import logging

@dataclass
class Runner():
    """
    runs a set of QC checks
    """

    config: Config


    def run(self) -> None:
        """
        runs all QC checks (metrics) on all knowledge sources in registry
        """
        registry = self.config.registry
        syncer = Syncer()
        syncer.sync(registry)
        loader = Loader(config)
        loader.load()

        for s in registry.has_knowledge_sources:
            for m in self.config.metric_collection.has_metrics:
                self.run_metric(m, s)

    def run_metric(self, metric: Metric, source: KnowledgeSource):
        """
        Note that this can be over-ridden to provide specific implementations
        :param metric:
        :param source:
        :return:
        """
        None



