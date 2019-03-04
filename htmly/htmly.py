"""
HTMLy
=====

Elm inspired HTML generator for Python.

Creating a tag.

>>> tag = div([], [])
>>> render(tag)
'<div ></div>'

Creating a self closing tag.
>>> render(hr([]))
'<hr />'

Tag can have a content.
>>> render(div([], [text('content')]))
'<div >content</div>'
>>> render(text('content'))
'content'

You can use some attributes for the tag.
>>> render(div([lang('tr'), id_('content'), class_('bar'), attribute('data-value', 'foo')], []))
'<div lang="tr" id="content" class="bar" data-value="foo"></div>'

You can have them both.
>>> render(div([lang('tr')], [text('content')]))
'<div lang="tr">content</div>'

You can have more content.
>>> render(div([], [ nav([], []), text('Hello'), hr([])]))
'<div ><nav ></nav>Hello<hr /></div>'

You can now start having composable abstractions as below.
You can have your own list item which takes content, without need of extra attributes and list syntax for content.
>>> _li = lambda item: li([], [text(item)])
>>> litems = lambda items: [_li(item) for item in items ]

Abstracting again just because we can.
>>> _ul = lambda items: ul([], litems(items))
>>> render(_ul(['Bob', 'Mary', 'Joe']))
'<ul ><li >Bob</li><li >Mary</li><li >Joe</li></ul>'

Nested Elements
>>> render(div([], [div([], [p([], [text('a paragraph')])])]))
'<div ><div ><p >a paragraph</p></div></div>'

>>> render(html([],
...             [ head([],
...                    [ title([],
...                            [text('Awesome Website')]),
...                      script([src('/script.js')], [])
...                    ]),
...               body([],
...                    [ header([],
...                             [ img([src('/logo.png')]) ]),
...                      div([], [text('Content Here')]),
...                      footer([],
...                             [hr([]),
...                              text('Copyright 2019')])
...                      ])
...               ]))
'<html ><head ><title >Awesome Website</title><script src="/script.js"></script></head><body ><header ><img src="/logo.png"/></header><div >Content Here</div><footer ><hr />Copyright 2019</footer></body></html>'
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
Element = NamedTuple('Element', [('name', AnyStr), ('attrs', Attributes), ('children', List['Node'])])
SelfClosingElement = NamedTuple('SelfClosingElement', [('name', AnyStr), ('attrs', Attributes)])
Text = NamedTuple('Text', [('data', AnyStr)])
Node = Union[Element, Text, SelfClosingElement]

def write_to_stream(node:Node, io:io.IOBase, indentation=0, indentation_level=INDENTATION_LEVEL):
    if type(node) == Element:
        io.write(f'<{node.name} {attrs(node)}>')
        for child in node.children:
            write_to_stream(child, io, indentation+indentation_level)
        io.write(f'</{node.name}>')
    elif type(node) == SelfClosingElement:
        io.write(f'<{node.name} {attrs(node)}/>')
    else:
        io.write(node.data)
        

def render(node: Node):
    output = io.StringIO()
    write_to_stream(node, output)
    return output.getvalue()

text = Text
self_closing_element = lambda name: lambda attributes: SelfClosingElement(name, attributes)
hr = self_closing_element('hr')
img = self_closing_element('img')
element = lambda name: lambda attributes, children: Element(name, attributes, children)
html = element('html')
head = element('head')
title = element('title')
script = element('script')
body = element('body')
header = element('header')
footer = element('footer')
div = element('div')
p = element('p')
ul = element('ul')
li = element('li')
nav = element('nav')
attrs = lambda node: ' '.join([f'{attr.name}="{attr.value}"' for attr in node.attrs])
attribute = lambda name, value: Attribute(name, value)
attribute_ = lambda name: lambda value: Attribute(name, value)
lang = attribute_('lang')
id_ = attribute_('id')
class_ = attribute_('class')
src = attribute_('src')

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    
