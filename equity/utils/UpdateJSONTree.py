
from django.core.exceptions import MultipleObjectsReturned
from equity.models import UserSecuritySelectionModel, ClassificationNames, SecuritySelectionModels
from django.http import Http404
import logging

logger = logging.getLogger(__name__)

get = lambda node_id, SSMModel: UserSecuritySelectionModel.objects.get(ext_model_id=node_id,SSM_id=SSMModel)

def UpdateSSM(topNode, SSMModel):
    if isinstance(topNode, list) == True:
        topNode = topNode.pop()

        try:
            # Get the rootNode in the datasource
            childOfRootNodes = UserSecuritySelectionModel.objects.get(ext_model_id=topNode['ext_model_id'])

            if childOfRootNodes.is_root():
                tempNode = childOfRootNodes.get_root()
                previousNode=childOfRootNodes

            if topNode['child']:

                if 'ext_model_id' in topNode:
                    previousNode = get(topNode['ext_model_id'], SSMModel)

                if 'child' in topNode:
                    for eachChildinTopNode in topNode['child']:
                        # if there is a node that is added but doesn't have an ext_model_id handle differently


                        if 'ext_model_id' in eachChildinTopNode:
                            ParentOfPreviousNode = UserSecuritySelectionModel.objects.get(
                                ext_model_id=eachChildinTopNode['ext_model_id'], SSM_id=SSMModel)
                        else:
                            # if you have an existing node => and an added Node we need to handle because this code moves on doesn't handle the
                            # next node
                            # ParentofPreviousNode should already be defined
                            classification = ClassificationNames.objects.get(
                                classificationName=eachChildinTopNode['classificationName'])
                            newNodeCreated = UserSecuritySelectionModel.create(False,
                                                                               SecuritySelectionModels.objects.get(
                                                                                   id=SSMModel), classification, 0, 0,
                                                                               False, classification.id)

                            tempNode.add_child(instance=newNodeCreated)  # tempNode is typically the root

                        # check to see if it is an actual child, if so and the hasChildNode is false set to True
                        allChildrenOfParentPreviousNode = returnChild(ParentOfPreviousNode, eachChildinTopNode, SSMModel)


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


def creatUSSMNoPrev(hasChildNode, id, SSMModel):
    newChild = UserSecuritySelectionModel()
    newChild.hasChildNode = hasChildNode
    newChild.tgtWeight = 0.0
    newChild.currWeight = 0.0

    classification = ClassificationNames.objects.get(id=id)

    newChild.classificationName = classification
    newChild.ext_model_id = classification.id
    newChild.SSM = SecuritySelectionModels.objects.get(id=SSMModel)

    newChild.isSSMNameNode = False

    return newChild


def returnChild(prev, childrenNodes, SSMModel):
    #TODO: Handle deletes and moves

    if 'child' in childrenNodes:
        # There is a child so test if the previous Node is set to True, if not set to True if fals
        if 'ext_model_id' in childrenNodes and childrenNodes['ext_model_id'] == prev.ext_model_id and not childrenNodes[
            'hasChildNode'] == prev.hasChildNode:
            prev.hasChildNode = childrenNodes['hasChildNode']
            prev.save()
            # Set it to true
            # If there is a remove then we need to test what that looks like and where that goes
        else:
            childrenNodes['hasChildNode'] = prev.hasChildNode

        for node in childrenNodes[
            'child']:  # if there are multiple children(LIST) then it will enumerate through each one
            if not 'ext_model_id' in node:
                # the first object in the dictionary is new. so we have to make an object
                print "In returnChild: Previous Node is  " + str(prev.classificationName)

                newUSSM = creatUSSMNoPrev(node['hasChildNode'], node['classificationName'], node['id'],
                                          SSMModel)  # Create a new SSM. This is the first node
                print "In returnChild: New Node is " + str(newUSSM.classificationName)

                prev.add_child(
                    instance=newUSSM)  # Prev is usually the RootNode. If the first child node doesn't exist, then Prev is the root node. We add it to the prev

                returnChild(newUSSM, node, SSMModel)

            returnChild(prev, node, SSMModel)