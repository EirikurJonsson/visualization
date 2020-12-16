# Visualization Project

## To run our dashboard

If you decide to test our dashboard, please follow these steps:

1. Clone the repo to a location on you local computer
2. _Recommended_: Create a virtual environment and install packages in the requirements.txt file using
    - pip install -r requirements.txt
3. The repo contains all data files used, so you only need to run the main.py file
    - In a terminal, navigate to the location where you cloned the project and in that terminal run:__python main.py__.

The last step can take some time since the visualizations are all interactive and are running on a rather large dataset. 

Thank you for testing and we hope you enjoy!

TODO:

- [x] Init git repo
- [x] Init virtual env for python with requirement.txt
- [x] Start bare-bones dash app
- [x] Time series graph in daily change of new cases with dropdown
- [x] Plot comparison countries 
- [x] Find a color scheme that works for this project
- [x] Bubble graph - interactive
- [x] World heat map - interactive
- [x] Combine long lat to main data file
- [x] Create a more concrete TODO list for visualizations

## Ready visualizations

What we have now is a single graph showing daily changes in new cases per million - this allows us to compare the countries we have in the graph.
We also have a table that highlights the two country closest to the chosen country in Human Development Index. 
