# Auto generated from semqc.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-07-02 16:55
# Schema: semqc
#
# id: semqc
# description: A data model for describing semantic quality control metrics plus the results of evaluating these
#              metrics on a set of sources. This can be used to drive a dashboard. We incorporate aspects of PROV
#              into this
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from biolinkml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from biolinkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from includes.types import String

metamodel_version = "1.4.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
PROV = CurieNamespace('prov', 'http://example.org/UNKNOWN/prov/')
SEMQC = CurieNamespace('semqc', 'http://w3id.org/semqc')
DEFAULT_ = SEMQC


# Types

# Class references
class MetricId(extended_str):
    pass


class KnowledgeSourceId(extended_str):
    pass


class MetricCollectionId(extended_str):
    pass


class MetricResultCollectionId(extended_str):
    pass


class ActivityId(extended_str):
    pass


@dataclass
class Metric(YAMLRoot):
    """
    An operational criteria on which a KG or ontology can be evaluated.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEMQC.Metric
    class_class_curie: ClassVar[str] = "semqc:Metric"
    class_name: ClassVar[str] = "metric"
    class_model_uri: ClassVar[URIRef] = SEMQC.Metric

    id: Union[str, MetricId]

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MetricId):
            self.id = MetricId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class KnowledgeSource(YAMLRoot):
    """
    An ontology or KG or similar artefact
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEMQC.KnowledgeSource
    class_class_curie: ClassVar[str] = "semqc:KnowledgeSource"
    class_name: ClassVar[str] = "knowledge source"
    class_model_uri: ClassVar[URIRef] = SEMQC.KnowledgeSource

    id: Union[str, KnowledgeSourceId]

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, KnowledgeSourceId):
            self.id = KnowledgeSourceId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class MetricResult(YAMLRoot):
    """
    Result of executing a metric on a KS
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEMQC.MetricResult
    class_class_curie: ClassVar[str] = "semqc:MetricResult"
    class_name: ClassVar[str] = "metric result"
    class_model_uri: ClassVar[URIRef] = SEMQC.MetricResult

    has_messages: List[Union[dict, "Message"]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        self.has_messages = [v if isinstance(v, Message)
                             else Message(**v) for v in self.has_messages]
        super().__post_init__(**kwargs)


@dataclass
class Message(YAMLRoot):
    """
    A piece of information communicated by an agent evaluating a metric on a source
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEMQC.Message
    class_class_curie: ClassVar[str] = "semqc:Message"
    class_name: ClassVar[str] = "message"
    class_model_uri: ClassVar[URIRef] = SEMQC.Message

    evaluated_using: Optional[Union[str, MetricId]] = None
    has_source: Optional[Union[str, KnowledgeSourceId]] = None
    has_status: Optional[str] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.evaluated_using is not None and not isinstance(self.evaluated_using, MetricId):
            self.evaluated_using = MetricId(self.evaluated_using)
        if self.has_source is not None and not isinstance(self.has_source, KnowledgeSourceId):
            self.has_source = KnowledgeSourceId(self.has_source)
        super().__post_init__(**kwargs)


@dataclass
class MetricCollection(YAMLRoot):
    """
    A collection of metrics, e.g OBO principles
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEMQC.MetricCollection
    class_class_curie: ClassVar[str] = "semqc:MetricCollection"
    class_name: ClassVar[str] = "metric collection"
    class_model_uri: ClassVar[URIRef] = SEMQC.MetricCollection

    id: Union[str, MetricCollectionId]
    has_metrics: Union[str, MetricId] = empty_dict()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MetricCollectionId):
            self.id = MetricCollectionId(self.id)
        self.has_metrics = [v if isinstance(v, MetricId)
                            else MetricId(v) for v in self.has_metrics]
        super().__post_init__(**kwargs)


@dataclass
class MetricResultCollection(YAMLRoot):
    """
    A collection of metric results
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEMQC.MetricResultCollection
    class_class_curie: ClassVar[str] = "semqc:MetricResultCollection"
    class_name: ClassVar[str] = "metric result collection"
    class_model_uri: ClassVar[URIRef] = SEMQC.MetricResultCollection

    id: Union[str, MetricResultCollectionId]
    description: Optional[str] = None
    uses_metric_collection: List[Union[str, MetricCollectionId]] = empty_list()
    has_metric_results: List[Union[dict, MetricResult]] = empty_list()
    has_knowledge_sources: Union[str, KnowledgeSourceId] = empty_dict()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MetricResultCollectionId):
            self.id = MetricResultCollectionId(self.id)
        self.uses_metric_collection = [v if isinstance(v, MetricCollectionId)
                                       else MetricCollectionId(v) for v in self.uses_metric_collection]
        self.has_metric_results = [v if isinstance(v, MetricResult)
                                   else MetricResult(**v) for v in self.has_metric_results]
        self.has_knowledge_sources = [v if isinstance(v, KnowledgeSourceId)
                                      else KnowledgeSourceId(v) for v in self.has_knowledge_sources]
        super().__post_init__(**kwargs)


@dataclass
class Activity(YAMLRoot):
    """
    a provence-generating activity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEMQC.Activity
    class_class_curie: ClassVar[str] = "semqc:Activity"
    class_name: ClassVar[str] = "activity"
    class_model_uri: ClassVar[URIRef] = SEMQC.Activity

    id: Union[str, ActivityId]
    started_at_time: Optional[str] = None
    ended_at_time: Optional[str] = None
    was_associated_with: Optional[Union[dict, "Agent"]] = None
    used: Optional[str] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ActivityId):
            self.id = ActivityId(self.id)
        if self.was_associated_with is not None and not isinstance(self.was_associated_with, Agent):
            self.was_associated_with = Agent(**self.was_associated_with)
        super().__post_init__(**kwargs)


@dataclass
class Agent(YAMLRoot):
    """
    a provence-generating agent
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEMQC.Agent
    class_class_curie: ClassVar[str] = "semqc:Agent"
    class_name: ClassVar[str] = "agent"
    class_model_uri: ClassVar[URIRef] = SEMQC.Agent

    acted_on_behalf_of: Optional[Union[dict, "Agent"]] = None
    was_informed_by: Optional[Union[str, ActivityId]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.acted_on_behalf_of is not None and not isinstance(self.acted_on_behalf_of, Agent):
            self.acted_on_behalf_of = Agent(**self.acted_on_behalf_of)
        if self.was_informed_by is not None and not isinstance(self.was_informed_by, ActivityId):
            self.was_informed_by = ActivityId(self.was_informed_by)
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.id = Slot(uri=SEMQC.id, name="id", curie=SEMQC.curie('id'),
                      model_uri=SEMQC.id, domain=None, range=URIRef)

slots.description = Slot(uri=SEMQC.description, name="description", curie=SEMQC.curie('description'),
                      model_uri=SEMQC.description, domain=None, range=Optional[str])

slots.evaluated_using = Slot(uri=SEMQC.evaluated_using, name="evaluated using", curie=SEMQC.curie('evaluated_using'),
                      model_uri=SEMQC.evaluated_using, domain=None, range=Optional[Union[str, MetricId]])

slots.has_source = Slot(uri=SEMQC.has_source, name="has source", curie=SEMQC.curie('has_source'),
                      model_uri=SEMQC.has_source, domain=None, range=Optional[Union[str, KnowledgeSourceId]])

slots.has_metrics = Slot(uri=SEMQC.has_metrics, name="has metrics", curie=SEMQC.curie('has_metrics'),
                      model_uri=SEMQC.has_metrics, domain=None, range=Union[str, MetricId])

slots.has_messages = Slot(uri=SEMQC.has_messages, name="has messages", curie=SEMQC.curie('has_messages'),
                      model_uri=SEMQC.has_messages, domain=None, range=List[Union[dict, Message]])

slots.has_knowledge_sources = Slot(uri=SEMQC.has_knowledge_sources, name="has knowledge sources", curie=SEMQC.curie('has_knowledge_sources'),
                      model_uri=SEMQC.has_knowledge_sources, domain=None, range=Union[str, KnowledgeSourceId])

slots.has_metric_results = Slot(uri=SEMQC.has_metric_results, name="has metric results", curie=SEMQC.curie('has_metric_results'),
                      model_uri=SEMQC.has_metric_results, domain=None, range=List[Union[dict, MetricResult]])

slots.uses_metric_collection = Slot(uri=SEMQC.uses_metric_collection, name="uses metric collection", curie=SEMQC.curie('uses_metric_collection'),
                      model_uri=SEMQC.uses_metric_collection, domain=None, range=List[Union[str, MetricCollectionId]])

slots.has_status = Slot(uri=SEMQC.has_status, name="has status", curie=SEMQC.curie('has_status'),
                      model_uri=SEMQC.has_status, domain=None, range=Optional[str])

slots.started_at_time = Slot(uri=SEMQC.started_at_time, name="started at time", curie=SEMQC.curie('started_at_time'),
                      model_uri=SEMQC.started_at_time, domain=None, range=Optional[str], mappings = [PROV.startedAtTime])

slots.ended_at_time = Slot(uri=SEMQC.ended_at_time, name="ended at time", curie=SEMQC.curie('ended_at_time'),
                      model_uri=SEMQC.ended_at_time, domain=None, range=Optional[str], mappings = [PROV.endedAtTime])

slots.was_informed_by = Slot(uri=SEMQC.was_informed_by, name="was informed by", curie=SEMQC.curie('was_informed_by'),
                      model_uri=SEMQC.was_informed_by, domain=None, range=Optional[Union[str, ActivityId]], mappings = [PROV.wasInformedBy])

slots.was_associated_with = Slot(uri=SEMQC.was_associated_with, name="was associated with", curie=SEMQC.curie('was_associated_with'),
                      model_uri=SEMQC.was_associated_with, domain=None, range=Optional[Union[dict, Agent]], mappings = [PROV.wasAssociatedWith])

slots.acted_on_behalf_of = Slot(uri=SEMQC.acted_on_behalf_of, name="acted on behalf of", curie=SEMQC.curie('acted_on_behalf_of'),
                      model_uri=SEMQC.acted_on_behalf_of, domain=None, range=Optional[Union[dict, Agent]], mappings = [PROV.actedOnBehalfOf])

slots.was_generated_by = Slot(uri=SEMQC.was_generated_by, name="was generated by", curie=SEMQC.curie('was_generated_by'),
                      model_uri=SEMQC.was_generated_by, domain=None, range=Optional[Union[str, ActivityId]], mappings = [PROV.wasGeneratedBy])

slots.used = Slot(uri=SEMQC.used, name="used", curie=SEMQC.curie('used'),
                      model_uri=SEMQC.used, domain=Activity, range=Optional[str], mappings = [PROV.used])
