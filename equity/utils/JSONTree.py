import json

from equity.models import UserSecuritySelectionModel, SecuritySelectionModels, ClassificationNames

get = lambda node_id: UserSecuritySelectionModel.objects.get(pk=node_id)

def JSONtoTreeBeard(obj):
    id = None;

    if (isinstance(obj, dict)) == True:
        treeString = obj
    else:
        treeString = json.loads(obj)

        # hierarchy = dict(treeString)

        root = SecuritySelectionModels.objects.filter(pk=treeString[0]['id'])

        if root:
            rootNode = UserSecuritySelectionModel()
            rootNode.currWeight = 0

            rootNode.SSM = SecuritySelectionModels.objects.get(pk=treeString[0]['id'])
            id = treeString[0]['id']

            rootNode.classificationNameNode = None
            rootNode.ext_model_id = treeString[0]['id']
            rootNode.hasChildnode = treeString[0]['hasChildNode']
            rootNode.tgtWeight = 0
            root = UserSecuritySelectionModel.add_root(instance=rootNode)

        if treeString[0]['child']:

            tempChild = treeString[0]['child']

            for child in tempChild:

                node = createChildObj(child, root)

                if not node.is_child_of(root):
                    root.add_child(instance=node)
                    # root.add_child(instance=node)

                    # if child:
                    #    if child['child'] and isinstance(child['child'], dict):

                    #       tempNode = createChildObj(child['child'], rootNode)

                    #   elif child['child'] and isinstance(child['child'], list):

                    #      tempNode = createChildObj(child['child'][0], rootNode)

                    # node.add_child(instance=tempNode)

def createChildObj(child, root):
    childObj = UserSecuritySelectionModel()
    childObj.classificationNameNode = ClassificationNames.objects.get(classificationName=child['classificationName'])
    childObj.ext_model_id = child['id']
    childObj.hasChildnode = child['hasChildNode']
    childObj.SSM = root.SSM
    childObj.tgtWeight = 0
    childObj.currWeight = 0

    if child['hasChildNode'] == True:
        root.add_child(instance=childObj)
        childChildObj = createChildObj(child['child'][0], childObj)

        if not childChildObj.is_child_of(childObj):
            childObj.add_child(instance=childChildObj)
    # add the child to the object

    return childObj
