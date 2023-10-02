from abc import abstractmethod
from flask_restx import Resource
from flask import request
from sqlalchemy import desc
import math

Object = lambda **kwargs: type("Object", (), kwargs)

class GridSuperController(Resource):
    
    @abstractmethod
    def search(self, data, search_str):
        ...
    
    def filter_sort_paginate(self, data):
        if (request.form.get('page')):
            page = int(request.form.get('page'))
        else:
            page = 1
          
        if (request.form.get('items_per_page')):
            items_per_page = int(request.form.get('items_per_page'))
        else:
            items_per_page = 10  
        sort = request.form.get('sort')
        order = request.form.get('order')
        search_str = request.form.get('search')
        # search
        data = self.search(data, search_str)
        # sort
        if order and sort:
            if (order == 'desc'):
                data = data.order_by(desc(sort))
            else:
                data = data.order_by(sort)
        
        total_count = data.count()
        
        # paginate
        data = data.paginate(page=page, per_page=items_per_page)
        
        pagination = {}
        pagination['itemsPerPage'] = items_per_page
        pagination['order'] = order
        pagination['sort'] = sort
        pagination['page'] = page
        pagination['totalCount'] = total_count
        pagination['pagesCount'] = math.ceil(total_count / items_per_page)
        pagination['search'] = search_str
        
        result = {}
        result['data'] = data.items
        result['pagination'] = pagination
        
        # print(result['pagination'])
                
        return result
        
        
        
        
        