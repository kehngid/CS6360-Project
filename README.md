# CS6360-Project

Running the code:
  Everything can be run through main, included in main are several testing datasets used by DeepEye and us.

  For running partial order:
  Inputs:
    1) Pick csv to use
      - Uncomment one of the ones listed on the top
      - Import your own by placing in data folder and using the relative name in place of filename in partial order function call
    2) Choose k, how many top visualization you want to see
      - set k equal to an integer, n, for the top n visualizations
      - set k equal to 'all', for all generated visualizations

  Output:
    - List of visuzalization nodes, including visualization data that contains what columns, aggregate functions, and type of graph is used,
      score of the graph, the bigger the score the better the graph is considered to be,
      and the list of nodes pointing to that node on the the 'graph' (list in incoming edges essentially)
    - Pop ups of a chart for each of the chosen visualizations

    Partial Order Evaluations: Can view difference in top 10 graphs of specific datasets in evaluations file in Partial Order. 
      - Outputs: Prints list of scores, the difference between each visualization. Compares our number 1 graph to DeepEyes and so one.
          - The higher the score the more different they are, a point is added to the score for each major difference. 
