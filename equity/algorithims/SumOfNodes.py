from equity.models import UserSecuritySelectionModel


def returnPercentOfNodeRoot(SSM_id, ext_model_id, tgtWeight):
    passedNode = UserSecuritySelectionModel.objects.get(ext_model_id=ext_model_id, SSM_id=SSM_id)

    if passedNode.is_root():
        childNodes = passedNode.get_children()
        numberOfChildNodes = passedNode.get_children_count()
    else:
        rootSSMNode = passedNode.get_parent()  # get the root parent of the node for that part of the tree

        rootSSMNode.tgtWeight = 0
        passedNode.tgtWeight = float(tgtWeight)
        rootSSMNode.tgtWeight = passedNode.tgtWeight

        siblings = passedNode.get_siblings()  # get the nodes in the same class, row, sibling
        numOfChildNodes = rootSSMNode.get_children_count()

        valuesToAllocate = (100 - float(tgtWeight)) / (numOfChildNodes - 1)

        for sibling in siblings:
            if not (sibling.ext_model_id == int(ext_model_id)):
                sibling.tgtWeight = float(valuesToAllocate)
                rootSSMNode.tgtWeight += float(valuesToAllocate)

            sibling.save()
            rootSSMNode.save()

    passedNode.save()

    return UserSecuritySelectionModel.objects.filter(ext_model_id=ext_model_id, SSM_id=SSM_id)
