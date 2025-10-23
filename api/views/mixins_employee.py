from ..serializer import EmployeeSerializer
from rest_framework import mixins, generics
from employees.models import Employee


class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView): # Ge inherit ang mga functions gikan sa mixins ug generics
    queryset = Employee.objects.all() # queryset para sa Employee model
    serializer_class = EmployeeSerializer # tawgagon ang serializer class para sa Employee model

    def get(self, request): 
        return self.list(request) 
    
    def post(self, request): 
        return self.create(request) 
    
class EmployeeDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all() # Ge fetch tanan data sa employee
    serializer_class = EmployeeSerializer 

    def get (self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)