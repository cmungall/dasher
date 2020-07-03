
# Type: metric result collection


A collection of metric results

URI: [semqc:MetricResultCollection](http://w3id.org/semqcMetricResultCollection)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[KnowledgeSource]<has%20knowledge%20sources%200..*-%20[MetricResultCollection&#124;id:string;description:string%20%3F],%20[MetricResult]<has%20metric%20results%200..*-++[MetricResultCollection],%20[MetricCollection]<uses%20metric%20collection%200..*-%20[MetricResultCollection])

## Attributes


### Own

 * [has metric results](has_metric_results.md)  <sub>0..*</sub>
    * range: [MetricResult](MetricResult.md)
 * [uses metric collection](uses_metric_collection.md)  <sub>0..*</sub>
    * range: [MetricCollection](MetricCollection.md)

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

### Inherited from problem:

 * [description](description.md)  <sub>OPT</sub>
    * Description: A description
    * range: [String](types/String.md)

### Inherited from registry:

 * [has knowledge sources](has_knowledge_sources.md)  <sub>0..*</sub>
    * range: [KnowledgeSource](KnowledgeSource.md)
