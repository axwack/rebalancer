class Node(object):
    # example from Telerik:
    # [{"classificationName":"sdsd","id":0,"hasChildNode":true,"child":[{"classificationName":"MBS","id":14,"hasChildNode":false},{"classificationName":"Common Stock","id":15,"hasChildNode":true,"child":[{"classificationName":"Money Market","id":17,"hasChildNode":false},{"classificationName":"Europe","id":27,"hasChildNode":false}]}]}]

    def __init__(self, classificationName, id, hasChildNode, child):
        self.classificationName = classificationName
        self.id = id
        self.hasChidNode = hasChildNode
        self.child = child
