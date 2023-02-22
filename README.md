# Wikidata-Wikibase Workshops

Material for the SEMIC workshops on Wikidata and Wikibase.

A playground Wikibase instance is running on <https://wikibase.semic.eu/>. Credentials will be provided during the workshop.

## Manual ingestion from the browser

You can access a list of all available actions on <https://wikibase.semic.eu/wiki/Special:SpecialPages>. For instance, you can create a new item manually on <https://wikibase.semic.eu/wiki/Special:NewItem>:

![New Item](/images/wb_new_item.png)

Specify a language, a title, a description, and optional aliases. The QID is auto-incremented and the resulting item can be accessed on <https://wikibase.semic.eu/wiki/Item:Q1> (replace Q1 with the generated QID):

![Q1](/images/wb_q1.png)

At this stage, the new item has no statements attached to it. You can add some by clicking "add statements" at the bottom right:

![Add statement](/images/wb_add_statement.png)

First select the property by typing its name or PID. If the property does not exist yet, you need to create it first on <https://wikibase.semic.eu/wiki/Special:NewProperty>:

![New Property](/images/wb_new_prop.png)

Then back on the item page, specify the value which can be of various types (QID, number, string...) and an optional qualifier or reference, and finally save.
For instance, we can specify that [DG CNECT](https://wikibase.semic.eu/wiki/Item:Q2) is an [instance of](https://wikibase.semic.eu/wiki/Property:P1) [Directorate-General](https://wikibase.semic.eu/wiki/Item:Q3):

![instance of DG](/images/wb_dg.png)

### Exercise

Now generate your first triple by:

1. creating two new items, one being the subject and the other the object
2. inventing one new property (note: on Wikidata this would require a [review process](https://www.wikidata.org/wiki/Wikidata:Property_proposal/EU_Knowledge_Graph_ID))
3. attaching the object to the subject through the property (new statement)

### Synchronisation with Wikidata

To avoid redefining existing concepts from scratch in your Wikibase, you can instead pull them from Wikidata. This can be achieved thanks to the [WikibaseSync](https://github.com/the-qa-company/WikibaseSync) library.

As this is technically more advanced, it will be demonstrated through a live demo. A graphical interface on top of WikibaseSync is also being developed.

For instance, find a concept that is present in Wikidata, like [PwC](https://www.wikidata.org/wiki/Q488048), but not in the [EU Knowledge Graph](https://linkedopendata.eu/). To import this concept into the EU KG, simply use the following command:

`python import_one.py Q488048`

It will pull all statements from Wikidata and create a new item in the EU KG. The two items can then be kept in sync.

## Batch ingestion with OpenRefine

See [this tutorial](refine.md).

## Automated ingestion with Pywikibot

See the dedicated [Jupyter notebook](https://colab.research.google.com/github/SEMICeu/Wikibase/blob/main/explore.ipynb).
