# Testing if we can read from Wikibase

import pywikibot
from SPARQLWrapper import SPARQLWrapper, JSON

wikibase = pywikibot.Site("my", "my")
wikibase_repo = wikibase.data_repository()
#wikibase_repo.login()

item = pywikibot.ItemPage(wikibase_repo, "Q1")
item.get()
print(item.labels['en']) # should print "Semantic Interoperability Community"
