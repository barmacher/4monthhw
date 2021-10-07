from rest_framework import serializers
from products.models import Product, Review, Tag


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = Product
        fields = ['id','title','discription','price','reviews']

    # def get_filtered(self, products, is_active):
    #     reviews = Review.objects.filter(is_active)
    #     return ReviewSerializer(reviews, many=True).data
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
class ActiveTagSerializer(serializers.ModelSerializer):
    active_tags = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['title','active_tags']

    def get_active_tags(self,product):
        tags = Tag.objects.filter(products=product).exclude(is_active=False)
        return TagSerializer(tags, many=True).data
