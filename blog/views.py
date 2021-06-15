from django.shortcuts import render, HttpResponse
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework import generics
from rest_framework import mixins



# ////////Generic APIView & Mixins///////FIRST AND BEST WAY////////


class ArticleList(generics.GenericAPIView,mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    # Getting the list of all the articles
    def get(self, request):
        return self.list(request)

    # Adding article 
    def post(self, request):
        return self.create(request)


# Creating the specific model where you can look for an article by id, updating and removing the artiles. but first we need to add all the mixins inside the artcialedetails class

class ArticleDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):


    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    # After running the details functions getting an error of using pk. we can fix that by adding the lookup_field=id
    lookup_field = 'id'


    # LOOK for an article by ID
    def get(self,request,id):
        return self.retrieve(request, id=id)


    # UPDATING an article
    def put(self, request, id):
        return self.update(request, id=id)


    # DELETING and article
    def delete(self, request, id):
        return self.destroy(request, id=id)

# ///////////Class Based API Views///////SECOND WAY//////////

# class ArticleList(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)


#     def post(self,request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # Adding put and delete functions
# class ArticleDetails(APIView):

#     def get_object(self, id):
#         try:
#             return Article.objects.get(id=id)
#         except Article.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     # GET a single article by the ID

#     def get(self, request, id):
#         article = self.get_object(id)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     # Update the article 

#     def put(self, request, id):
#         article = self.get_object(id)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # Delete the Article 

#     def delete(self, request, id):
#         article = self.get_object(id)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# ///////Function Bases API View////////THIRD WAY/////////////////////


# @api_view (['GET', 'POST'])
# def article_list(request):

# # get the list of all articles

#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

# # Creating an article ///////////////////

#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # using rest apit
# @api_view (['GET', 'PUT', 'DELETE'])

# def article_details(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)

#     except Article.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)


# # UPDATING Article //////////////

#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # DELETING AN ARTICLE///////////////////

#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# # now we are adding the routes to urls.py file ////////////////////
