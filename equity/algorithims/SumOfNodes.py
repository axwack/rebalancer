from equity.models import UserSecuritySelectionModel


def returnPercentOfNodeRoot(SSM_id, ext_model_id, tgtWeight):
    passedNode = UserSecuritySelectionModel.objects.get(ext_model_id=ext_model_id, SSM_id=SSM_id)

    if passedNode.is_root():
        childNodes = passedNode.get_children()
        numberOfChildNodes = passedNode.get_children_count()
    else:
        parentSSMNode = passedNode.get_parent()  # get the root parent of the node for that part of the tree

        parentSSMNode.tgtWeight = 0
        passedNode.tgtWeight = float(tgtWeight)
        parentSSMNode.tgtWeight = passedNode.tgtWeight

        siblings = passedNode.get_siblings()  # get the nodes in the same class, row, sibling
        numOfChildNodes = parentSSMNode.get_children_count()


        if not parentSSMNode.parent_id is None:
            parentSSMNode.tgtWeight = 0
            passedNode.tgtWeight = float(tgtWeight)
            parentSSMNode.tgtWeight = passedNode.tgtWeight

            siblings = passedNode.get_siblings()  # get the nodes in the same class, row, sibling
            numOfChildNodes = parentSSMNode.get_children_count()

            valuesToAllocate = (100 - float(tgtWeight)) / (numOfChildNodes - 1)

        else: #We are in a root node so allocate the percentage to the bottom of the rows
             childNodes = passedNode.get_children()

             for child in childNodes:
                 child.tgtWeight = passedNode.tgtWeight / passedNode.get_children_count()
                 child.save()

             valuesToAllocate = (100 - float(tgtWeight)) / numOfChildNodes

        for sibling in siblings:
            if not (sibling.ext_model_id == int(ext_model_id)):
                sibling.tgtWeight = float(valuesToAllocate)
                parentSSMNode.tgtWeight += float(valuesToAllocate)

            sibling.save()
            parentSSMNode.save()

        passedNode.save()

    # test the root node children which should be the branches
    rootNode = passedNode.get_root()

    branches = rootNode.get_root_nodes()
    


    return UserSecuritySelectionModel.objects.filter(ext_model_id=ext_model_id, SSM_id=SSM_id)
