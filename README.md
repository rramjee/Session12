# Session 12 Assignment

## Lazy Iterator and Iterables

Lazy Iterators are iterators that do not load entire dataset in memory but load only required information at every iteration. This is such a useful feature that has plenty of uses in real world implementations.

As part of this assignment we are building two classes. One Polygon and One Custom Polygon classes. We have built the classes as part of earlier assignments session 10 and session 11.

This assignment has 2 goals

##Goal 1
Refactor the Polygon class so that all the calculated properties are lazy properties, i.e. they should still be calculated properties, but they should not have to get recalculated more than once (since we made our Polygon class "immutable").

##Goal 2
Refactor the Polygons (sequence) type, into an iterable. Make sure also that the elements in the iterator are computed lazily - i.e. you can no longer use a list as an underlying storage mechanism for your polygons.

