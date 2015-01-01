__author__ = 'instancetype'


def tag(name, **attributes):
    """Create a void HTML tag with attributes.

    Example:

       tag('img', src="jitsu.jpg", alt="Yet another cat picture")
    """
    result = '<' + name
    for key, value in attributes.items():
        result += ' {k}="{v}"'.format(k=key, v=str(value))
    result += ' />'
    return result

