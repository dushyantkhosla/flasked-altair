def Div(children, **kwargs):
    '''
    Generate content to fill the Jinja templates
    '''
    if 'class_' in kwargs.keys():
        kwargs['class'] = kwargs['class_']
        del(kwargs['class_'])
    return {
        'tag': 'div',
        'attributes': kwargs,
        'content': children if children is not None else ''
        }
