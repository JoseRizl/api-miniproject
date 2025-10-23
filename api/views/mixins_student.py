from ..serializer import StudentSerializer
from rest_framework import mixins, generics
from students.models import Student


class Students(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView): # Ge inherit ang mga functions gikan sa mixins ug generics
    queryset = Student.objects.all() # queryset para sa Student model
    serializer_class = StudentSerializer # tawgagon ang serializer class para sa Student model

    def get(self, request): 
        return self.list(request) 
    
    def post(self, request): 
        return self.create(request) 
    
class StudentDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all() # Ge fetch tanan data sa student
    serializer_class = StudentSerializer 

    def get (self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)