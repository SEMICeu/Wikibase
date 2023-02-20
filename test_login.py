# Testing if bot login works properly

import pywikibot
from SPARQLWrapper import SPARQLWrapper, JSON

wikibase = pywikibot.Site("my", "my")
wikibase_repo = wikibase.data_repository()
wikibase_repo.login()

item = pywikibot.ItemPage(wikibase_repo, "Q1")
item.get()
print(item.labels['en'])
