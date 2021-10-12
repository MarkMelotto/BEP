# BEP
Bachelor end project

Hi,
In this python project I keep my data and simulations.
I am a bachelor student bla bla bla

This project might look cluttered and messy, probably because it is, but I'll do my best to guide you through it.

This readme file will have the same directory stuff as the project, so you can find stuff like that.
Sources will be directly linked underneath the explanation.

- calculations
  
  this folder contains some data and fits to calculate a fit for useful functions
  
    - air_density_calculator:
      This takes air density data at 1 atm that I got from engineeringtools [1], makes a fit and plots it, 
      this data is later used in functions.functions calculate_air_density

      - 1 (https://www.engineeringtoolbox.com/air-density-specific-weight-d_600.html?vA=-5&units=C#)

    - Humidity_calculator:
      This takes water saturation data at 1 atm that I got from engineeringtools [1], makes a fit and plots it, 
      this data is later used in functions.functions calculate_water_saturation

      - [1] https://www.engineeringtoolbox.com/maximum-moisture-content-air-d_1403.html
    
  
- downloads

  downloads has some preview code, for me to learn stuff, basically, I won't elaborate

    - lines3d_demo
    
    - surface3d_demo
    
    - wire3d_demo
    

- foute boel
  
  this folder has stuff in it that got abandoned or was just wrong
  
    - FOUT TEST absorptie:
      the data I got from here [1], but it was wrong.
      the mu_ data are attenuation coefficients, after that the percentages of the gasses in the air.
      after that I calculate the low and high percentage of water in the air attenuation coefficients.
      from this I can calculate the intensity that remains after said path length with beer lamberts law [2]
      
      - [1] https://physics.nist.gov/PhysRefData/XrayMassCoef/ElemTab/z07.html
      - [2] just google: beer lamberts law


- functions

  This is a vital folder, it has basic/specialized functions and data sets from different sources
  
    - functions:
    
    - HITRAN_data:
    
    - HITRAN_functions:
    
    - WIKI_data:
    
    - WIKI_functions:


- HITEMP


- HITRAN_DATA_TESTS


- MAIN


- venv


- WIKIPEDIA_DATA_TESTS
