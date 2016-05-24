from rest_framework import serializers
from equity.models import Account, ClassificationNames, AllocationNodes, AllocationModels, AccountFilters, \
    SecuritySelectionModels, UserSecuritySelectionModel, Feeds, Securities


class AccountSerializer(serializers.Serializer):
    acctCd = serializers.CharField(read_only=False, required=True)
    shortName = serializers.CharField(required=False, allow_blank=True, max_length=100)
    cashSegregated = serializers.FloatField()
    cashUnSegregated = serializers.FloatField()
    totCash = serializers.FloatField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Account.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.acctCd = validated_data.get('acctCd', instance.acctCd)
        instance.shortName = validated_data.get('shortName', instance.shortName)
        instance.cashSegregated = validated_data.get('cashSegrated', instance.cashSegregated)
        instance.cashUnSegregated = validated_data.get('cashUnsegregated', instance.cashUnSegregated)
        instance.totCash = validated_data.get('totCash', instance.totCas)
        instance.save()

        return instance

    class Meta:
        model = Account
        fields = ('acctCd', 'shortName', 'cashSegregated', 'cashUnSegregated', 'totCash')


class ClassificationNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassificationNames
        fields = ('id', 'classificationName', 'classificationLevel', 'hasChildNode')


class AllocationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllocationModels
        fields = ('id', 'modelName', 'created_by', 'edited_by')


class AllocationNodesSerializer(serializers.ModelSerializer):
    allocationModel = AllocationModelSerializer(many=True, required=True)
    classificationName = ClassificationNamesSerializer(many=True, required=True)

    class Meta:
        model = AllocationNodes
        fields = ('allocationModel', 'classificationName', 'level')


class AccountFilterSerializer(serializers.ModelSerializer):
    account = AccountSerializer(many=True)

    class Meta:
        model = AccountFilters()
        fields = ('acctFilterName', 'accountName', 'account', 'created_by', 'edited_by', 'createDate', 'updateDate',)


class SecuritySelectionModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = SecuritySelectionModels()
        fields = ('id', 'securitySelectionModelName', 'classificationNames',)


class SecuritiesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Securities()
        fields = ('secId', 'secName')


class UserSecuritySelectionModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserSecuritySelectionModel()
        fields = '__all__'
        depth = 1


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeds
        fields = ('feed_cd', 'entity_to_run', 'enable', 'run_date')
