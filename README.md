# python-oop: Python object-oriented programming

## Core but nonetheless an add-on

[collections.namedtuple](https://docs.python.org/2/library/collections.html#collections.namedtuple) is often forgotten about. However, it is preferable to the use of dictionaries in many cases. [Discusssion](https://www.reddit.com/r/Python/comments/3qw7m4/improving_your_code_readability_with_namedtuples/)

# Add-ons

* [Schematics](http://schematics.readthedocs.io)
* [attrs](https://attrs.readthedocs.io/en/stable/) - [Tutorial article](https://glyph.twistedmatrix.com/2016/08/attrs.html)
* [traitlets](https://github.com/ipython/traitlets)
* [Elk](https://github.com/frasertweedale/elk)
* [Enthought's Traits Package](https://docs.enthought.com/traits/)
* [Atom](https://github.com/nucleic/atom)
* [Yuppy](https://github.com/kuujo/yuppy)
* [strait](https://pypi.python.org/pypi/strait)
* [BasicProperty](http://basicproperty.sourceforge.net/)
* [PEAK Rules](https://pypi.python.org/pypi/PEAK-Rules)
* [metaparams](https://github.com/mementum/metaparams)
* [Zope interfaces](https://pypi.python.org/pypi/zope.interface) 

# Method Munging

* [pyhooks](https://github.com/Shir0kamii/pyhooks) - pre and post hooks for your methods.
* [Connectible](https://github.com/timothycrosley/connectable#readme) - the Observer pattern 
* [forwardable](https://pypi.python.org/pypi/forwardable/) - delegation 

## Multimethods

* [multimethods](https://pypi.python.org/pypi/multimethods/) Robert Kende
* [multimethods](https://github.com/weissjeffm/multimethods) Jeff Weiss
* [PEAK Rules](https://pypi.python.org/pypi/PEAK-Rules) Philip Eby
* [multimethodic](https://github.com/danwerner/multimethodic) by Dan Werner
* [generic](https://pythonhosted.org/generic/) by Andrey Popp

### Generic Functions / ML-Style Pattern Matching / Lisp-Style CLOS 

* [Reg](http://reg.readthedocs.io/)
* [Pythfun](https://github.com/sminez/Pythfun)
* [PyPatt](http://www.grantjenks.com/docs/pypatt-python-pattern-matching/#) by Grant Jenks
* [PyFPM](https://github.com/martinblech/pyfpm)
* [PyFNC](https://github.com/jldupont/pyfnc)
* [Paco](https://github.com/h2non/paco) - coroutine-driven, asynchronous-based generic programming in Python +3.4


# Dependency Injection

(as discussed in [the python wiki](https://wiki.python.org/moin/DependencyInjectionPattern), we see that [there are quite a few on PyPi](https://pypi.python.org/pypi?%3Aaction=search&term=dependency+injection). The ones listed below appear to have active userbases and code maintainers.


* Dependencies [github](https://github.com/proofit404/dependencies)
* Autowired [github](https://github.com/allrod5/injectable), [discussion](https://www.reddit.com/r/Python/comments/7vwi61/injectable_autowired_decorator_for_di_and_lazy/)
* Serum [github](https://github.com/suned/serum)
* Picobox: [Discussion](https://www.reddit.com/r/Python/comments/7l0yfr/picobox_opinionated_dependency_injection/?utm_content=comments&utm_medium=hot&utm_source=reddit&utm_name=Python), [Docs](http://picobox.readthedocs.com)
* Injector [Docs](http://injector.readthedocs.io/en/latest/)
* [Dependency Injector](http://python-dependency-injector.ets-labs.org/en/stable/)
* [Siringa](https://github.com/h2non/siringa)
* [Give Me](https://github.com/steinitzu/giveme)
* [ainject](https://github.com/pohmelie/ainject)
* [autowire](https://github.com/Hardtack/Autowire)

## Design Patterns

* [Design Pattern Templates for Python.](https://github.com/tylerlaberge/PyPattyrn)
* [A collection of design patterns/idioms in Python](https://github.com/faif/python-patterns)
* [Factory design pattern snippet](https://gist.github.com/1099559)


# Web Development / HTML Generation

100% Python-based object-oriented web development from front to back (database processing to html/js/css rendering) is a possibility in Python thanks to thse libraries. The database side is typically done with SQLAlchemy. The "HTML Alchemy" is done with the libraries below.

* [Nagare](http://naga.re) 
* [flybywire](https://github.com/thomasantony/flybywire)
* [Remi](https://github.com/dddomodossola/remi)
* [PyJS](http://pyjs.org/)
* [PyBee](https://pybee.org/)
* [Flexx](https://flexx.readthedocs.io/en/latest/)
* [Anpylar](https://www.anpylar.com/)
* [Reahl](http://www.reahl.org/)
* [Engel](https://github.com/Dalloriam/engel)
* [Muntjac](https://github.com/rwl/muntjac) - a (defunct) port of [Vaadin](https://vaadin.com) from Java to Python.
* [Enaml](http://nucleic.github.io/enaml/docs/get_started/introduction.html)
* [TheDom](https://github.com/timothycrosley/thedom) by Timothy Crosley
* [Dominate](https://github.com/Knio/dominate)
* [Funky Bomb](https://pythonhosted.org/funkybomb/)

# Data Structure-ish

* [Addict](https://github.com/mewwts/addict)
* [ObjectPath](http://objectpath.org/)
* [JSObject](https://pypi.python.org/pypi/jsobject/) - Javascript style objects in Python
* [glom](https://github.com/mahmoud/glom)


## Dictionary Wrappers

Providing OO access to Python dictionaries can be important so you can override access to attributes. It is becoming a hotly contested topic in the Python community.

You may read [a comprehensive comparison of them](https://github.com/pohmelie/skin#benchmark).

* [Skin](https://www.reddit.com/r/Python/comments/7ev2lc/suit_yet_another_attributelike_access_to/)
* [DotMap](https://pypi.python.org/pypi/dotmap) by Chris Redford - [heated discussion](https://www.reddit.com/r/Python/comments/5xn562/dotmap_rocks/)
* [Box](https://github.com/cdgriffith/Box) by Chris Griffith - [heated discussion](https://www.reddit.com/r/Python/comments/611zmj/introducing_box_python_dictionaries_with/)
* [dot_access](https://www.reddit.com/r/Python/comments/71u3fd/dot_access_makes_going_through_nested_python/)

# Literature

## Books

* [Python in Practice: Create Better Programs Using Concurrency, Libraries and Patterns](https://www.amazon.com/Python-Practice-Concurrency-Libraries-Developers/dp/0321905636)

## Articles

* [Objects and classes in Python](http://jfine-python-classes.readthedocs.io/en/latest/index.html) by J Fine.
* [Classes and Objects III: Metaclasses, Abstract Base Classes and Class Decorators](http://intermediatepythonista.com/metaclasses-abc-class-decorators)
* [Python Decorator for Simplifying Delegate Pattern](https://programmingideaswithjake.wordpress.com/2015/05/23/python-decorator-for-simplifying-delegate-pattern/) by Jacob Zimmerman
 
## Discussion

* [Best Practices: OOP in Python](https://www.reddit.com/r/Python/comments/6xs6od/best_practices_oop_in_python/)
* [Would you consider method chaining to be Pythonic?](https://redd.it/7798ub)

# History

I intially made [a reddit post](https://www.reddit.com/r/Python/comments/2d9f7i/survey_of_python_object_systems/) followed by [a post to comp.lang.python](https://groups.google.com/forum/#!topic/comp.lang.python/vW9JTTI1GBA) on this subject. 

When [metaparams was posted to the Python reddit](https://github.com/mementum/metaparams) I figured it was about time to have a central directory of such systems.
