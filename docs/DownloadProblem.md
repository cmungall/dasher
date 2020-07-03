
# Type: download problem


A problem in downloading a knowledge source

URI: [semqc:DownloadProblem](http://w3id.org/semqcDownloadProblem)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[KnowledgeSource]<has%20source%200..1-%20[DownloadProblem&#124;description(i):string%20%3F],%20[Problem]^-[DownloadProblem])

## Parents

 *  is_a: [Problem](Problem.md) - An object representing an error or problem encountered

## Attributes


### Own

 * [has source](has_source.md)  <sub>OPT</sub>
    * range: [KnowledgeSource](KnowledgeSource.md)

### Inherited from problem:

 * [description](description.md)  <sub>OPT</sub>
    * Description: A description
    * range: [String](types/String.md)
    * inherited from: None
