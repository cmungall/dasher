
# Type: node annotation change


A node change where the change alters node properties/annotations. TODO

URI: [ocl:NodeAnnotationChange](http://w3id.org/oclNodeAnnotationChange)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[NodeAnnotationChange&#124;about(i):string%20%3F;old_value(i):string%20%3F;new_value(i):string%20%3F]^-[NodeAnnotationReplacement],%20[NodeChange]^-[NodeAnnotationChange])

## Parents

 *  is_a: [NodeChange](NodeChange.md) - A simple change where the change is about a node

## Children

 * [NodeAnnotationReplacement](NodeAnnotationReplacement.md) - A node annotation change where the change replaces a particular property value. TODO

## Referenced by class


## Attributes


### Inherited from node change:

 * [node change➞about](node_change_about.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
    * inherited from: [NodeChange](NodeChange.md)

### Inherited from node rename:

 * [node rename➞old value](node_rename_old_value.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
    * inherited from: [NodeRename](NodeRename.md)
 * [node rename➞new value](node_rename_new_value.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
    * inherited from: [NodeRename](NodeRename.md)
