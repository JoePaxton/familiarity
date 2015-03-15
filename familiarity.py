__author__ = 'Joe Paxton'
"""
familiarity.py

Plots the familiarity of an artist over the years they have been active.
There is also a 'strength' variable that calculates the area of the familiarity
multiplied by the years they have been active and will be used in a later program.
For now, it was used to test different artists and to compare different artists who
have been active for a long period or short period of time (in years) with a high
or low familiarity rate.

You can input any artist into the Artist function as long as if Echo Nest has
found the particular artist you are searching for.
"""
from pyechonest import artist
import echonest.remix.audio as audio
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Use different artists to see the different values.
    a = artist.Artist("Chance, The Rapper")
    x = a.get_years_active()

    familiarity = a.familiarity

    start = x[0].get('start')
    end = x[0].get('end')
    
    if end is None:
        end = 2015
        
    startValue = int(start)
    endValue = int(end)
    yrs_active = endValue - startValue
    print "The artist has been active for" , yrs_active, "years"
    
    strength = familiarity * yrs_active
    print "The strength of the artist is a decimal value of", strength, "which is the familiarity rate multiplied by the years active."

    plt.xlim(xmin=0, xmax=yrs_active + 5)
    """Need to figure out how to get actual years up there,
    instead of just the amount of years active..."""
    plt.scatter(yrs_active, familiarity)
    plt.title("Familiarity Over Years They Have Been Active")
    plt.xlabel("Years Active")
    plt.ylabel('Familiarity')
    
    plt.savefig("Familiarity of an Artist")
    plt.show()

if __name__ == '__main__':
    main()
