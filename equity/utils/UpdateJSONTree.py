
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

            if topNode['child']:

                if topNode.has_key('ext_model_id'):
                    previousNode = get(topNode['child']['ext_model_id'], SSMModel)

                childNodeOfNode = returnChild(node)

                if not childNodeOfNode is None:
                    childOfPreviousNode = createUserSecuritySelectionModel(childNodeOfNode, SSMModel)
                    previousNode.add_child(instance=childOfPreviousNode)

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

def createUserSecuritySelectionModel(childOfPreviousNode, SSMModel):

    if isinstance(childOfPreviousNode, list)==True:
        childOfPreviousNode = childOfPreviousNode.pop()

    newChild = UserSecuritySelectionModel()

    newChild.hasChildNode = childOfPreviousNode['hasChildNode']

    newChild.tgtWeight = 0.0
    newChild.currWeight = 0.0

    classification = ClassificationNames.objects.get(classificationName=childOfPreviousNode['classificationName'])

    newChild.classificationName = classification
    newChild.ext_model_id = classification.id
    newChild.SSM = SecuritySelectionModels.objects.get(id=SSMModel)

    newChild.isSSMNameNode = False

    return newChild

def returnChild(node):
    if isinstance(node,list):
        node.pop()

    if isinstance(node, dict):
        for k, v in node.iteritems():
            if 'child' in k:
                return v
            else:
                return returnChild(v)
