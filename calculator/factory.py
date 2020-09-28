import factory
import factory.fuzzy
from .models import result

class resultFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = result
    '''    
    num1 = factory.fuzzy.FuzzyInterger(0,100)
    num2 = factory.fuzzy.FuzzyInterger(0,100)
    result =  factory.fuzzy.FuzzyInterger(0,100)
    '''