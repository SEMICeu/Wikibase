# Testing if we can read from Wikibase

import pywikibot
from SPARQLWrapper import SPARQLWrapper, JSON

wikibase = pywikibot.Site("my", "my")
wikibase_repo = wikibase.data_repository()
wikibase_repo.login()

item = pywikibot.ItemPage(wikibase_repo, "Q1")
item.get()
print(item.labels['en']) # should print "Semantic Interoperability Community"

fr_label = "Communauté d'interopérabilité sémantique"
new_label_data = {'fr': fr_label}
item.editLabels(new_label_data, summary=u'Added French label')
