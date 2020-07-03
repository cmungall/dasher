
# Type: metric collection


A collection of metrics, e.g OBO principles

URI: [semqc:MetricCollection](http://w3id.org/semqcMetricCollection)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Metric]<has%20metrics%200..*-%20[MetricCollection&#124;id:string;description:string%20%3F])

## Referenced by class

 *  **None** *[uses metric collection](uses_metric_collection.md)*  <sub>0..*</sub>  **[MetricCollection](MetricCollection.md)**

## Attributes


### Own

 * [has metrics](has_metrics.md)  <sub>0..*</sub>
    * range: [Metric](Metric.md)

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
