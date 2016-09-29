Install & Running:
1. Please make sure the requirements.txt has been run
2. This is a very simple architecture, so please keep the app.py, quicksearch.py and the directory which you want to search through in the same directory on the same level.
3. Run the app.py using the command to start the uwsgi and perform get requests  or curl requests:
   uwsgi --http :8080 --wsgi-file app.py --callable wsgi_app
4. Parameterization has been given to only to 2 routes, and not for the route which does the search and match all at once.


Directory Name: redis-unstable

Endpoint 1 [search and match in one shot: http://<IP address>:<port>/searchall/<directory name>

Endpoint 2 [search and match generalized]: http://<IP address>:<port>/search01/<directory name>

Endpoint 3 [search and match individual files that you get from endpoint 2]:
http://<IP address>:<port>/search02?filepath=<absolute file path>&searchtype=<variable or function>&query=<your query>

Has been tested for the below with best query execution time:
Endpoint 1

http://192.168.1.6:8080/searchall/redis-unstable?query=stdio

On external connect : 1.9 sec approx [best of 3]
On local curl : 1.8 sec approx [best of 3]

2 step search Endpoint 2:

Step 1 of 2:
http://192.168.1.6:8080/search01/redis-unstable

On external connect:0.11 sec approx [best of 3]
On local curl : 0.1 sec approx [best of 3]

Step 2 of 2 [Example with variable parameter/no parameter]:
Get required path, create query and run

http://192.168.1.6:8080/search02?filepath=/root/redis-unstable/deps/lua/src/lvm.c&searchtype=value&query=stdio

On external connect : 0.009 sec approx [best of 3]
On local curl: 0.007 sec approx [best of 3]

2 step search [Another example with function parameter]:

Step 2 of 2:

http://192.168.1.6:8080/search02?filepath=/root/redis-

unstable/src/modules/helloworld.c&searchtype=function&query=HelloPushNative_RedisCommand

On external connect : 0.009 sec approx [best of 3]
On local curl: 0.008 approx [best of 3]

