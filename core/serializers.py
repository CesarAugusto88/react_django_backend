from .models import List, Item
from rest_framework import serializers


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'done']


class ListSerializer(serializers.HyperlinkedModelSerializer):
    # item_set objeto dentro de dir() buscado em shell
    # >>> from core.models import List                                        
    # >>> l = List.objects.first()
    # >>> l
    # <List: Primeira Lista>
    # >>> dir(l) 
    # Itens que pertence a esta lista
    item_set = ItemSerializer(many=True)

    class Meta:
        model = List
        fields = ['id', 'name', 'owner', 'url', 'item_set']

