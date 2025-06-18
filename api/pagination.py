from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size_query_param = 'page_size' # allows the client to dynamically set the page by adding page_size ?page_size=10
    page_query_param = 'page-num' # 
    max_page_size = 1 # limtis the max number of items per page to 1
    
    def get_paginated_response(self, data): # basically override the method that returns that paginated response
        return Response({
            'next':self.get_next_link(),
            'previous':self.get_previous_link(),
            'count':self.page.paginator.count,
            'page_size':self.page_size, # gives the total data in that particular page
            'results':data
            
        }) 
    