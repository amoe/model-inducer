# model-inducer

This is a tiny tool that will take in a data set and get the possible values to
form a structure that's labelled as a 'domain table'.  This can be populated
through other tools such as my `semja` tool.

The way that it should work is as follows:

1.  Input is a row and column based format.
2.  The file may contain multiple entities.
3.  The tool should suggest entities to be extracted through normalization,
based on duplication.
4.  The tool should detect variance in the data types, for instance strings vs
numbers.
5.  The tool should identify extremes, in e.g. string length or number magnitude.
6.  When values repeat the tool should suggest cases where a domain table can
be extracted.
7.  The tool should produce DML scripts for population of said domain tables.
