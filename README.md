# Problem
We want to visualize and determine the strength of an artist's [familiarity] over the
artist's active years.

# Questions
1. What kind of data does the [familiarity] attribute provide?
2. How can we determine how long an artist has been active?
3. How can we compare and contrast the "strength" of each artist?
4. Can we use [matplotlib] to visualize data we have?

# Resources
1. [familiarity]
2. [Echo Nest Artist API]
3. [matplotlib]


### 1. Mini-abstract and relevance of [familiarity]:
[Familiarity] corresponds to how well-known an artist is. For example, if you were to survey a
thousand people and ask them, "who has heard of *Michael Jackson* and *Japanese Cartoon*?", the
numbers for *Michael Jackson* are going to be much higher than *Japanese Cartoon*. The [familiarity]
attribute is a floating-point value between 0 and 1.0, where 1.0 is the most "familiar" or
"famous" an artist can be. Echo Nest does not share their implementation of their algorithm for [familiarity],
but it is based on upon the total activity they see for artists on the copious amounts of websites they
actively crawl. 

```python
from pyechonest import artist

a = artist.Artist("Lupe Fiasco")
a.familiarity
```
The [familiarity] for the artist, *Lupe Fiasco* has a floating-point decimal value of 0.779026.
This shows that the artist is very well-known, but not overwhelmingly "famous".

On the other hand, the 'hotttness' attribute gives a floating-point decimal value that displays the
"hype" or "buzz" an artist is getting currently. The 'hotttnesss' attribute is biased, in the sense
that the attribute computes the "hype" currently; therefore, this does not accurately reflect the
"hype" that some artists' receive if it was years ago such as *The Beatles*. In other words, if *The Beatles*
were still a band today with the same amount of "buzz" as they had in the 1960s than the 'hotttnesss'
attribute would return a higher floating-point value. There are not much blog posts, website articles, or
other website information (Echo Nest algorithm for 'hotttnesss') about famous artists who were active several
years ago or even decades ago. *The way they implement the 'hotttnesss' attribute is on the same link as
[familiarity]*.

The [familiarity] attribute is an easier value to compare the "strength value" ([familiarity] rate multiplied
by the amount of years an artist has been active) against different artists, especially when it comes to
different time periods. 

*This answers question 1*

### 2. Mini-abstract and relevance of [Echo Nest Artist API]:
There is a function in the [Echo Nest Artist API] called ```get_years_active()``` and it returns
the *start* and *end* year (if there is an *end*) of the artist's years active. In our case, we are
inputting *Lupe Fiasco* as our artist into the ```Artist()``` function from the ```pyechonest``` module.
By calling the ```get_years_active()``` function on this particular artist, it does not show the *end*
date because he is currently active as an artist. 

```python
from pyechonest import artist

a = artist.Artist("Lupe Fiasco")
a.get_years_active()
```
"Lupe Fiasco" started his career in ```[{u'start': 1999}]```. We can see that there is no *end* date
when the ```get_years_active()``` function was returned, which concludes that he is still a working
artist.

On the other hand, when I inputted "Jimi Hendrix" into the ```Artist()``` function ```[{u'start': 1963, u'end': 1970}]```
was returned after calling the function ```get_years_active()```. Again, this proves that this function
returns a list of a *start* date and an *end* date if the artist is not considered an artist anymore.

We need to compare artist's who have a high [familiarity] rate while being active for a short amount of
time (in *years*) against artist who have a lower [familiarity] rate while being active for a longer
period of time (in *years*). We can determine the "strength" of the artist's [familiarity] rate using
an algorithm I implemented below:

```python
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

strength = familiarity * yrs_active
```
When I inputted *Chance, The Rapper* into the ```Artist()``` function, the ouput of his years being
active are ```[{u'start': 2011}]``` until now, with a [familiarity] of ```0.576622``` and an area
or "strength" of ```2.306488``` whereas, *Tower of Power* has been active from ```[{u'start': 1968}]```
until now with a [familiarity] of ```0.624398``` and an area or "strength" of ```29.346706```. The
[familiarity] between the two artists are not too far apart; whereas, their "strength" attribute differs
dramatically, due to the fact that *Tower of Power* has been active for 47 years and running. *Chance,
The Rapper* has been active for only 4 years and running.

*This answers questions 2 and 3*

### 3. Mini-abstract and relevance of [matplotlib]:
Using the [matplotlib] API, I was able to analyze the data explained from above visually. I plotted a
scatter plot from the program I created, called [familiarity.py].

```python
plt.xlim(xmin=0, xmax=yrs_active + 5)
"""Need to figure out how to get actual years up there,
instead of just the amount of years active..."""
plt.scatter(yrs_active, familiarity)
plt.title("Familiarity Over Years They Have Been Active")
plt.xlabel("Years Active")
plt.ylabel('Familiarity')
    
plt.savefig("Familiarity of an Artist")
plt.show()
```
When I run this snippet of code it displays the ```yrs_active``` for the x-axis because the ```scatter()```
function will only accept an ```int```. The ```get_years_active()``` function from the ```pyechonest``` module
is a list with only one index that has a *start* and an *end* value. Earlier in the program, I was interested
in analyzing the *strength* attribute I implemented where I saved the *end* date minus the *start* date into the
```yrs_active``` variable, in order to figure out how many years the artist has been active. In the future, I need
to display the actual years they were active as opposed to the number of years they were active. Also, this would
be better visualized in a bar plot when I start to compare multiple artist at a time.

*This answers question 4*

[familiarity]: http://developer.echonest.com/forums/thread/839
[Echo Nest Artist API]: https://github.com/echonest/pyechonest/blob/master/pyechonest/artist.py 
[matplotlib]: http://matplotlib.org/
[familiarity.py]: https://github.com/JoePaxton/familiarity/blob/master/familiarity.py
