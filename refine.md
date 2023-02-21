# Using OpenRefine for reconciliation and batch ingestion

First download the latest version of [OpenRefine](https://openrefine.org/download) (currently 3.7.0).
Unzip the folder and follow the instructions depending on your operating system.

## Exploration

Launch OpenRefine in your browser on the [localhost](http://127.0.0.1:3333/) (not Internet access required).
Download the [vloca.csv file](/data/vloca.csv) and load it into OpenRefine:

![OR1](/images/or1.png)

![OR2](/images/or2.png)

![OR3](/images/or3.png)

## Reconciliation

The Wikibase extension is included in OpenRefine, as you can see in the top-right corner.
It offers two default services, Wikidata and Wikimedia Commons:

![OR WB services](/images/or_wb_services.png)

However, you can choose to add your own Wikibase to the list by specifying a manifest. You can use [this file](manifest.json) or find [more examples](https://github.com/OpenRefine/wikibase-manifests) on GitHub. You will also need to set up a [reconciliation service](http://reconci.link/) (currently not active here).

![OR manifest](/images/or_manifest.png)

The new Wikibase will then become available in the list:

![OR SEMIC WB](/images/or_semic_wb.png)
