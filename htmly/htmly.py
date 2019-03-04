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
import io
INDENTATION_LEVEL = 2
AttributeName = NamedTuple('AttributeName', [('name', AnyStr)])
AttributeValue = AnyStr
Attribute = NamedTuple('Attribute', [('name', AttributeName), ('value', AttributeValue)])
Attributes = Union[List[Attribute], Dict[AttributeName, AttributeValue]]                       
Element = NamedTuple('Element', [('name', AnyStr), ('attrs', Attributes), ('children', 'ElementList')])
ElementList = List[Element]
Text = NamedTuple('Text', [('data', AnyStr)])
Node = Union[Element, Text]

def write_to_stream(node:Node, io:io.IOBase, indentation=0, indentation_level=INDENTATION_LEVEL):
    io.write(' ' * indentation)
    io.write(f'<{node.name}></{node.name}>')

def render(node: Node):
    output = io.StringIO()
    write_to_stream(node, output)
    return output.getvalue()

def div(attributes, children):
    return Element('div', attributes, children)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    
