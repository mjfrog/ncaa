#list sorter
from operator import itemgetter

upsets_by_year = [[1985, 18], [1986, 18], [1987, 18], [1988, 17], [1989, 20], [1990, 20], [1991, 16], [1992, 15], [1993, 12], [1994, 18], [1995, 14], [1996, 15], [1997, 16], [1998, 18], [1999, 23], [2000, 19], [2001, 21], [2002, 16], [2003, 21], [2004, 16], [2005, 19], [2006, 21], [2007, 12], [2008, 13], [2009, 16], [2010, 20], [2011, 20], [2012, 17], [2013, 20], [2014, 22], [2015, 12], [2016, 20], [2017, 14], [2018, 20], [2019, 20], [2021, 19]]
print(sorted(upsets_by_year, key=itemgetter(1)))