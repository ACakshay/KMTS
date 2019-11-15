from SPARQLWrapper import SPARQLWrapper, JSON
import cgi
form = cgi.FieldStorage()
searchterm =  form.getvalue('searchbox')

# List all instances (eg. bands) with genre Metal
query = """
PREFIX db: <http://dbpedia.org/resource/>
PREFIX dbonto: <http://dbpedia.org/ontology/>
SELECT DISTINCT ?who
FROM <http://dbpedia.org>
WHERE {
    ?who dbonto:genre db:Metal .
}
""".format(searchterm)

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery(query)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(result["who"]["value"])
