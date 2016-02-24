import json

from equity.models import UserSecuritySelectionModel, SecuritySelectionModels, ClassificationNames

get = lambda node_id: UserSecuritySelectionModel.objects.get(pk=node_id)

def JSONtoTreeBeard(obj):
    id = None;

    if (isinstance(obj, dict)) == True:
        treeString = obj
        root = SecuritySelectionModels.objects.filter(pk=treeString[0]['id'])

    elif isinstance(obj, list) == True:
        treeString = obj.pop()

        root = SecuritySelectionModels.objects.filter(pk=treeString['id'])
    else:
        treeString = json.loads(obj)
        root = SecuritySelectionModels.objects.filter(pk=treeString[0]['id'])

    if root:
        rootNode = UserSecuritySelectionModel()
        rootNode.currWeight = 0
        rootNode.isSSMNameNode = True
        rootNode.SSM = SecuritySelectionModels.objects.get(pk=treeString[0]['id'])
        id = treeString[0]['id']

        rootNode.classificationName = None
        rootNode.ext_model_id = treeString[0]['id']
        rootNode.hasChildNode = treeString[0]['hasChildNode']
        rootNode.tgtWeight = 0
        root = UserSecuritySelectionModel.add_root(instance=rootNode)

    if treeString[0]['child']:

        tempChild = treeString[0]['child']

        for child in tempChild:

            node = createChildObj(child, root)

            if not node.is_child_of(root):
                root.add_child(instance=node)



def createChildObj(child, root):
    childObj = UserSecuritySelectionModel()
    childObj.classificationName = ClassificationNames.objects.get(classificationName=child['classificationName'])
    childObj.ext_model_id = child['id']
    childObj.hasChildNode = child['hasChildNode']
    childObj.SSM = root.SSM
    childObj.tgtWeight = 0
    childObj.currWeight = 0
    childObj.isSSMNameNode = False

    if child['hasChildNode'] == True:
        root.add_child(instance=childObj)
        childChildObj = createChildObj(child['child'][0], childObj)

        if not childChildObj.is_child_of(childObj):
            childObj.add_child(instance=childChildObj)
    # add the child to the object

    return childObj
