
# Type: message


A piece of information communicated by an agent evaluating a metric on a source

URI: [semqc:Message](http://w3id.org/semqcMessage)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[KnowledgeSource]<has%20source%200..1-%20[Message&#124;has_status:string%20%3F;description:string%20%3F],%20[Metric]<evaluated%20using%200..1-%20[Message])

## Referenced by class

 *  **None** *[has messages](has_messages.md)*  <sub>0..*</sub>  **[Message](Message.md)**

## Attributes


### Own

 * [evaluated using](evaluated_using.md)  <sub>OPT</sub>
    * range: [Metric](Metric.md)
 * [has status](has_status.md)  <sub>OPT</sub>
    * Description: The status of either an entire metric result, or an individual message with a metric result
    * range: [String](types/String.md)

### Inherited from download problem:

 * [has source](has_source.md)  <sub>OPT</sub>
    * range: [KnowledgeSource](KnowledgeSource.md)

### Inherited from problem:

 * [description](description.md)  <sub>OPT</sub>
    * Description: A description
    * range: [String](types/String.md)
