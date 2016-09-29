import falcon
from quicksearch import Searcher
import json

 
class SearchOnceResource(object):
    def on_get(self, req, resp, user_dir="redis-unstable"):
	resp.set_header('Content-Type', 'text/plain')
        resp.status = falcon.HTTP_200
        resp.body = 'You want to traverse %s' %user_dir
        q1 = Searcher(user_dir)
        if req.get_param("query"):
            q1.query = req.get_param("query")
        info = q1.allonce()
        resp.body = json.dumps(info, encoding='utf-8')

class SearchPartOne(object):
    def on_get(self, req, resp, user_dir="redis-unstable"):
        resp.set_header('Content-Type', 'text/plain')
        resp.status = falcon.HTTP_200
        resp.body = 'You want to traverse %s' %user_dir
        q1 = Searcher(user_dir)
        if req.get_param("query"):
            q1.query = req.get_param("query")
        info = q1.twostep0()
        resp.body = json.dumps(info, encoding='utf-8')

class SearchPartTwo(object):
    def on_get(self, req, resp, filepath="README.md"):
        resp.set_header('Content-Type', 'text/plain')
        resp.status = falcon.HTTP_200
        q1 = Searcher(filepath)
        if req.get_param("query"):
            q1.query = req.get_param("query")
	if req.get_param("filepath"):
            q1.sfile = req.get_param("filepath")
        if req.get_param("searchtype"):
	    q1.searchtype = req.get_param("searchtype")
            if q1.searchtype == 'function':
                q1.query = "^void|^int|^float|^char "+q1.query+"\(*\)"
        info = q1.twostep1()
        resp.body = json.dumps(info, encoding='utf-8')
 
wsgi_app = api = falcon.API()
 
search_all = SearchOnceResource()
search_part_one = SearchPartOne()
search_part_two = SearchPartTwo()
 
api.add_route('/searchall/{user_dir}', search_all)
api.add_route('/search01/{user_dir}', search_part_one)
api.add_route('/search02', search_part_two)
