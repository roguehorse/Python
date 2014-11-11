#!/usr/bin/perl
#changing.py
#from CodeAcademy tutorial
#Scott DuBois
#10/3/2014

# key - animal_name : value - location
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']

zoo_animals['Rockhopper Penguin'] = 'Alaska Exhibit'

print zoo_animals
