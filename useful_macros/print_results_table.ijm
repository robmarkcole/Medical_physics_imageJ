  headings = split(String.getResultsHeadings);
  for (row=0; row<nResults; row++) {
     line = "";
     for (col=0; col<lengthOf(headings); col++)
        line = line + getResult(headings[col],row) + "  ";
     print(line);
  }