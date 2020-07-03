
# Type: metric result


Result of executing a metric on a KS

URI: [semqc:MetricResult](http://w3id.org/semqcMetricResult)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Message]<has%20messages%200..*-++[MetricResult&#124;has_status:string%20%3F;description:string%20%3F],%20[KnowledgeSource]<has%20source%200..1-%20[MetricResult],%20[Metric]<evaluated%20using%200..1-%20[MetricResult])

## Referenced by class

 *  **None** *[has metric results](has_metric_results.md)*  <sub>0..*</sub>  **[MetricResult](MetricResult.md)**

## Attributes


### Own

 * [has messages](has_messages.md)  <sub>0..*</sub>
    * range: [Message](Message.md)

### Inherited from message:

 * [evaluated using](evaluated_using.md)  <sub>OPT</sub>
    * range: [Metric](Metric.md)
 * [has source](has_source.md)  <sub>OPT</sub>
    * range: [KnowledgeSource](KnowledgeSource.md)
 * [has status](has_status.md)  <sub>OPT</sub>
    * Description: The status of either an entire metric result, or an individual message with a metric result
    * range: [String](types/String.md)

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
