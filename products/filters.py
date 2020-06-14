from . models import Product
import django_filters
from django_filters.filters import RangeFilter

# creting product filters
class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    price = RangeFilter()


    class Meta:
        model = Product
        fields = ['name', 'price']




# In this file, we are creating a class called ProductFilter which inherits 
# FilterSet from django filter. Then we have created two fields one is for name which is Charfield. 
# Another one is price which I used RangeField cause I think people can filter products based on their budget.