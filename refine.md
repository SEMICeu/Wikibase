# Using OpenRefine for reconciliation and batch ingestion

First download the latest version of [OpenRefine](https://openrefine.org/download) (currently 3.7.0).
Unzip the folder and follow the instructions depending on your operating system.

## Exploration

Launch OpenRefine in your browser on the [localhost](http://127.0.0.1:3333/) (not Internet access required).
Download the [vloca.csv file](/data/vloca.csv) and load it into OpenRefine:

![OR1](/images/or1.png)

![OR2](/images/or2.png)

![OR3](/images/or3.png)

You can now start exploring the VLOCA data with facets and filters. For instance, if you open the menu of the "Class" column and select Facet > Text facet, then sort by count in the left pane you will get this overview of the distribution of the classes used:

![OR VLOCA classes](/images/or_vloca_class.png)

Continue exploring the data to get familiar with the different data types (text, numbers, URLs, etc.).

## Reconciliation

The Wikibase extension is included in OpenRefine, as you can see in the top-right corner.
It offers two default services, Wikidata and Wikimedia Commons:

![OR WB services](/images/or_wb_services.png)

However, you can choose to add your own Wikibase to the list by specifying a manifest. You can use [this file](manifest.json) or find [more examples](https://github.com/OpenRefine/wikibase-manifests) on GitHub. You will also need to set up a [reconciliation service](http://reconci.link/) (currently not active here).

![OR manifest](/images/or_manifest.png)

The new Wikibase will then become available in the list:

![OR SEMIC WB](/images/or_semic_wb.png)

For now, let's test the reconciliation service with Wikidata. On the "Organisatie" column menu, choose Reconcile > Start reconciling... Select the Wikidata service and it will autodetect the most promising entity type, in this case [municipality of Belgium](https://www.wikidata.org/wiki/Q493522):

![OR municipalities](/images/or_municipality.png)

Confirm to launch the reconciliation process, then filter on the left for "matched" values:

![OR matched](/images/or_matched.png)

The strings "Antwerp", "Mechelen", "Aalst" etc. have now been reconciled to their respective Wikidata items and all additional information about these cities (images, geolocation, website...) can be reused.

For more details on reconciliation, see [this manual](https://openrefine.org/docs/manual/reconciling).

## Ingestion

OpenRefine can also be used to ingest data in a semi-automated way.
