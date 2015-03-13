# Problem
We want to visualize and determine the strength of an artist's [familiarity] over the
artist's active years.

# Question
1. What kind of data does the [familiarity] attribute provide?
2. How can we determine how long an artist has been active?
3. Can we use [matplotlib] to visualize data we have?
4. How can we compare and contrast the "strength" of each artist?


# Resources
1. [familiarity]
2. [Echo Nest Artist API]
3. [artist.py]
4. [matplotlib]


### 1. Mini-abstract and relevance of [familiarity]:
Familiarity corresponds to how well known the artist is. For example, if you were to survey a
thousand people and ask them who has heard of Michael Jackson and Hot Rod Shopping Cart, the
numbers for Michael are going to be much higher than the Hot Rod Shopping Car. Echo Nest does
not show share their algorithm for [familiarity], but it is based on upon the total activity
they see for artists on thousands of websites they crawl. The [familiarity] attribute is a
floating-point value between 0 and 1.0, where 1.0 is the most "familiar" or "famous".

```python
from pyechonest import artist

a = artist.Artist("Lupe Fiasco")
a.familiarity
```
The [familiarity] of the artist "Lupe Fiasco" is a floating-point decimal value of 0.779026.
This shows that the artist is very well-known, but not overwhelmingly "famous". The 'hotttness'
attribute gives a floating-point decimal value that displays the "hype" or "buzz" an artist is
getting currently. The 'hotttnesss' attribute causes some biased algorithm, only because it is
information that is in the present and will be much different than artist in the past. There is
not much blog posts, website articles, or other website information about popular artists decades
ago. The [familiarity] attribute is an easier value to analyze the strength between different
artists, especially when it comes to different time periods. 

### 2. Mini-abstract and relevance of [Echo Nest Artist API]:


```python
from pyechonest import artist

a = artist.Artist("Lupe Fiasco")
a.get_years_active()
```

### 3. Mini-abstract and relevance of [artist.py]:


### 4. Mini-abstract and relevance of [matplotlib]:




[familiarity]: http://developer.echonest.com/forums/thread/839
[Echo Nest Artist API]: http://developer.echonest.com/docs/v4/artist.html
[artist.py]: https://github.com/echonest/pyechonest/blob/master/pyechonest/artist.py  
[matplotlib]: http://matplotlib.org/

