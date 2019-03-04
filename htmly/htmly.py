"""
HTMLy
=====

Elm inspired HTML generator for Python.

Creating a tag.

>>> tag = div([], [])
>>> render(tag)
'<div></div>'
"""
from typing import ( NamedTuple,
                     List,
                     AnyStr,
                     Union,
                     Dict
)
AttributeName = NamedTuple('AttributeName', [('name', AnyStr)])
AttributeValue = AnyStr
Attribute = NamedTuple('Attribute', [('name', AttributeName), ('value', AttributeValue)])
Attributes = Union[List[Attribute], Dict[AttributeName, AttributeValue]]                       
Element = NamedTuple('Element', [('name', AnyStr), ('attrs', Attributes), ('children', 'ElementList')])
ElementList = List[Element]
Text = NamedTuple('Text', [('data', AnyStr)])
Node = Union[Element, Text]

def render(node: Node):
    return '<%s></%s>' % (node.name, node.name)

def div(attributes, children):
    return Element('div', attributes, children)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    
