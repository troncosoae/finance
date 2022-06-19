# finance

Brief description.

## Index 

* Link to other Readmes

## Idea

The point behind creating this is to have many simple reutilizable modules that can be integrated in order to analyze Portfolios. 

## Arquitecture

### Kernel

An *Index* is the atomic piece, it cannot be divided. 
Many *Index*es may be combined into *IndexGroup*s. 
In turn, *IndexGroup*s may be combined with other *Index*es or *IndexGroup*s to create an *IndexGroup*. 

### Data Extractors

*DataExtractors* can retrieve data from a source into an *Index*. 
When extracting data for an *IndexGroup*, it must be done recursively.

### Analyzers

*Analyzer*s operate over *IndexGroup*s, and execute a shallow analysis. This means that components included in the *IndexGroup* are treated as undivisible. 

### User Interface

Ideas:
* Command line. 
* JSON reader and executer. This JSON file must be delt with in a greedy manner. Meaning that every time something has changed (buy/sell), you must not need to start writing it from scratch again. 
* Gmail API. 

### Todo


