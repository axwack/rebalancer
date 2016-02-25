
from django.core.exceptions import MultipleObjectsReturned
from equity.models import UserSecuritySelectionModel, ClassificationNames, SecuritySelectionModels
from django.http import Http404

get = lambda node_id, SSMModel: UserSecuritySelectionModel.objects.get(ext_model_id=node_id,SSM_id=SSMModel)

def UpdateSSM(topNode, SSMModel):

    if isinstance(topNode, list)==True:
        topNode = topNode.pop()

        try:
            childOfRootNodes = UserSecuritySelectionModel.objects.get(ext_model_id=topNode['ext_model_id']) #Get the rootNode in the datasource

            if childOfRootNodes.is_root():
                tempNode = childOfRootNodes.get_root()
                previousNode=childOfRootNodes

                #if not tempNode.id==childOfRootNodes.id:
                #    tempNode.add_child(instance=childOfRootNodes)

            if topNode['child']:
                    for child in topNode['child']:
                        #child = getChildNodes(indexofChildNode)
                        if child.has_key('ext_model_id'):
                            previousNode = get(child['id'], SSMModel)
                        else:
                            #the node isn't in the model so add it.
                            newChild = UserSecuritySelectionModel()
                            newChild.hasChildNode=False
                            newChild.tgtWeight = 0.0
                            newChild.currWeight = 0.0

                            classification = ClassificationNames.objects.get(classificationName=child['classificationName'])

                            newChild.classificationName = classification
                            newChild.ext_model_id = classification.id
                            newChild.SSM = SecuritySelectionModels.objects.get(id=tempNode.ext_model_id)

                            newChild.isSSMNameNode=False

                            if previousNode is None:
                                previousNode=tempNode

                            previousNode.add_sibling(pos='sorted-sibling',instance=newChild )

        except MultipleObjectsReturned:
            raise Http404("More than one Security Selection Model was returned. Is there only one?")

def getChildNodes(child):

    return child['child']
    # add the child to the object

    return childObj


