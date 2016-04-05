from django.core.exceptions import MultipleObjectsReturned
from equity.models import UserSecuritySelectionModel, ClassificationNames, SecuritySelectionModels
from django.http import Http404
import logging

logger = logging.getLogger(__name__)

get = lambda node_id, SSMModel: UserSecuritySelectionModel.objects.get(ext_model_id=node_id, SSM_id=SSMModel)


def deleteNodes(nodesToDelete, SSMModel):
    try:
        for nodeId in nodesToDelete:
            nodeToDelete = get(nodeId, SSMModel).delete()
    except:
        return 1

    return 0
