# HTMLy
Elm inspired HTML generator for Python.

## From the doctest.
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
