# Wikidata-Wikibase Workshops

Material for the SEMIC workshops on Wikidata and Wikibase

## Preliminary steps

A playground Wikibase instance is running on <https://wikibase.semic.eu/>. Credentials will be provided during the workshop.

## Manual ingestion from the browser

You can access a list of all available actions on <https://wikibase.semic.eu/wiki/Special:SpecialPages>. For instance, you can create a new item manually on <https://wikibase.semic.eu/wiki/Special:NewItem>:

![New Item](/images/wb_new_item.png)

Specify a language, a title, a description, and optional aliases. The QID is auto-incremented and the resulting item can be accessed on <https://wikibase.semic.eu/wiki/Item:Q1> (replace Q1 with the generated QID):

![Q1](/images/wb_q1.png)

At this stage, the new item has no statements attached to it. You can add some by clicking "add statements" à the bottom right:

![Add statement](/images/wb_add_statement.png)

First select the property by typing its name or PID. If the property does not exist yet, you need to create it first on <https://wikibase.semic.eu/wiki/Special:NewProperty>:

![New Property](/images/wb_new_prop.png)

Then back on the item page, specify the value which can be of various types (QID, number, string...) and an optional qualifier or reference, and finally save.
For instance, we can specify that [DG CNECT](https://wikibase.semic.eu/wiki/Item:Q2) is an [instance of](https://wikibase.semic.eu/wiki/Property:P1) [Directorate-General](https://wikibase.semic.eu/wiki/Item:Q3):

![instance of DG](/images/wb_dg.png)

## Batch ingestion with OpenRefine

See [this tutorial](refine.md).

## Automated ingestion with Pywikibot

See the dedicated [Jupyter notebook](https://colab.research.google.com/github/SEMICeu/Wikibase/blob/main/explore.ipynb).
