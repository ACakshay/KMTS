from django.shortcuts import render
from SPARQLWrapper import SPARQLWrapper, JSON
import cgi
# Create your views here.

def index(request):
    return render(request,'index.html')


def show(request):
    if request.method == 'POST':
        searchterm = request.POST.get('searchbox')
        print(searchterm)

    if (searchterm == 'Sentimental'):
        query = """
        PREFIX db: <http://dbpedia.org/resource/>
        PREFIX dbonto: <http://dbpedia.org/ontology/>
        SELECT DISTINCT ?who
        FROM <http://dbpedia.org>
        WHERE {
            ?who dbonto:genre db:Vocal .
        }
        """

    elif (searchterm == 'Fiery'):
        query = """
        PREFIX db: <http://dbpedia.org/resource/>
        PREFIX dbonto: <http://dbpedia.org/ontology/>
        SELECT DISTINCT ?who
        FROM <http://dbpedia.org>
        WHERE {
            ?who dbonto:genre db:Jazz .
        } LIMIT 10
        """

    elif (searchterm == 'Witty'):
        query = """
        PREFIX db: <http://dbpedia.org/resource/>
        PREFIX dbonto: <http://dbpedia.org/ontology/>
        SELECT DISTINCT ?who
        FROM <http://dbpedia.org>
        WHERE {
            ?who dbonto:genre db:Rap .
        }
        """

    elif (searchterm == 'Silly'):
        query = """
        PREFIX db: <http://dbpedia.org/resource/>
        PREFIX dbonto: <http://dbpedia.org/ontology/>
        SELECT DISTINCT ?who
        FROM <http://dbpedia.org>
        WHERE {
            ?who dbonto:genre db:Comedy .
        }
        """
    elif (searchterm == 'Wistful'):
        query = """
        PREFIX db: <http://dbpedia.org/resource/>
        PREFIX dbonto: <http://dbpedia.org/ontology/>
        SELECT DISTINCT ?who
        FROM <http://dbpedia.org>
        WHERE {
            ?who dbonto:genre db:Folk .
        }
        """
    elif (searchterm == 'Fun'):
        query = """
        PREFIX db: <http://dbpedia.org/resource/>
        PREFIX dbonto: <http://dbpedia.org/ontology/>
        SELECT DISTINCT ?who
        FROM <http://dbpedia.org>
        WHERE {
            ?who dbonto:genre db:Electronica .
        }
        """
    elif (searchterm == 'Joyous'):
        query = """
        PREFIX db: <http://dbpedia.org/resource/>
        PREFIX dbonto: <http://dbpedia.org/ontology/>
        SELECT DISTINCT ?who
        FROM <http://dbpedia.org>
        WHERE {
            ?who dbonto:genre db:Gospel .
        }
        """
    elif (searchterm == 'Rousing'):
        query = """
        PREFIX db: <http://dbpedia.org/resource/>
        PREFIX dbonto: <http://dbpedia.org/ontology/>
        SELECT DISTINCT ?who
        FROM <http://dbpedia.org>
        WHERE {
            ?who dbonto:genre db:Latin .
        }
        """
    elif (searchterm == 'Theatrical'):
        query = """
        PREFIX db: <http://dbpedia.org/resource/>
        PREFIX dbonto: <http://dbpedia.org/ontology/>
        SELECT DISTINCT ?who
        FROM <http://dbpedia.org>
        WHERE {
            ?who dbonto:genre db:Soundtrack .
        }
        """
    elif (searchterm == 'Druggy'):
        query = """
        PREFIX db: <http://dbpedia.org/resource/>
        PREFIX dbonto: <http://dbpedia.org/ontology/>
        SELECT DISTINCT ?who
        FROM <http://dbpedia.org>
        WHERE {
            ?who dbonto:genre db:Reggae .
        }
        """
    elif (searchterm == 'Confident'):
        query = """
        PREFIX db: <http://dbpedia.org/resource/>
        PREFIX dbonto: <http://dbpedia.org/ontology/>
        SELECT DISTINCT ?who
        FROM <http://dbpedia.org>
        WHERE {
            ?who dbonto:genre db:World .
        }
        """
    elif (searchterm == 'Volatile'):
        query = """
        PREFIX db: <http://dbpedia.org/resource/>
        PREFIX dbonto: <http://dbpedia.org/ontology/>
        SELECT DISTINCT ?who
        FROM <http://dbpedia.org>
        WHERE {
            ?who dbonto:genre db:Avant-Garde .
        }
        """

    print(searchterm)

    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    a=[]
    for result in results["results"]["bindings"]:
        a.append(result["who"]["value"])


    return render (request,'result.html',{"results":results["results"]["bindings"],"input":searchterm,"a":a})

    # else:
    #     return redirect('ftp:admin_projects')
