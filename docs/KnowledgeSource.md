
# Type: knowledge source


An ontology or KG or similar artefact

URI: [semqc:KnowledgeSource](http://w3id.org/semqcKnowledgeSource)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Referenced by class

 *  **None** *[has knowledge sources](has_knowledge_sources.md)*  <sub>0..*</sub>  **[KnowledgeSource](KnowledgeSource.md)**
 *  **None** *[has source](has_source.md)*  <sub>OPT</sub>  **[KnowledgeSource](KnowledgeSource.md)**

## Attributes


### Inherited from activity:

 * [id](id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)
 * [started at time](started_at_time.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
    * inherited from: None
 * [ended at time](ended_at_time.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
    * inherited from: None
 * [was associated with](was_associated_with.md)  <sub>OPT</sub>
    * range: [Agent](Agent.md)
    * inherited from: None
 * [used](used.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
    * inherited from: [Activity](Activity.md)

### Inherited from metric result collection:

 * [description](description.md)  <sub>OPT</sub>
    * Description: A description
    * range: [String](types/String.md)
 * [uses metric collection](uses_metric_collection.md)  <sub>0..*</sub>
    * range: [MetricCollection](MetricCollection.md)
    * inherited from: None
 * [has metric results](has_metric_results.md)  <sub>0..*</sub>
    * range: [MetricResult](MetricResult.md)
    * inherited from: None
 * [has knowledge sources](has_knowledge_sources.md)  <sub>0..*</sub>
    * range: [KnowledgeSource](KnowledgeSource.md)
    * inherited from: None
