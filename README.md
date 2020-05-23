# fpd-reana

To run a workflow:

	./run.sh workflow.yaml

Available workflow:
	- simple_scatter.yaml is a mutli stage workflow that passes all input param cards to echoflow.yml
	- echoflow.yaml is a single stage workflow that outputs input param card into new output file in ma5 docker image 
	- ma5_scatter.yaml performs a full madanalysis5 scan using the given param cards
	- ma5.yaml is one run of an end-to-end madanalyis5 workflow (madgraph, pythia, ma5)