# HTMLy
Elm inspired HTML generator for Python.

## Create a new tag.

    >>> tag = div([], [])
    >>> render(tag)
    '<div ></div>'

## Create a self closing tag.
    
    >>> render(hr([]))
    '<hr />'

## Tags having content.

    >>> render(div([], [text('content')]))
    '<div >content</div>'
    >>> render(text('content'))
    'content'

## Tags having attributes.

    >>> render(div([lang('tr'), id_('content'), class_('bar'), attribute('data-value', 'foo')], []))
    '<div lang="tr" id="content" class="bar" data-value="foo"></div>'

## Tags with attributes and content.

    >>> render(div([lang('tr')], [text('content')]))
    '<div lang="tr">content</div>'

## Nested tags.

    >>> render(div([], [ nav([], []), text('Hello'), hr([])]))
    '<div ><nav ></nav>Hello<hr /></div>'
    
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


## Composing tags for templating.
You can now start having composable abstractions as below.
You can have your own list item which takes content, without need of extra attributes and list syntax for content.
    
    >>> _li = lambda item: li([], [text(item)])
    >>> litems = lambda items: [_li(item) for item in items ]

Abstracting again just because we can.

    >>> _ul = lambda items: ul([], litems(items))
    >>> render(_ul(['Bob', 'Mary', 'Joe']))
    '<ul ><li >Bob</li><li >Mary</li><li >Joe</li></ul>'


