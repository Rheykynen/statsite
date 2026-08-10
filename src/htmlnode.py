

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # der HTML-Tag (p, a, h1, etc.)
        self.value = value  # der Text des HTML-Tags
        self.children = children # eine Liste von HTMLNode objects
        self.props = props # k,v -Paare des HTML-Tags wie z.B. {"href": "https://www.google.com"} oder
        # {
        # "href": "https://www.google.com",
        # "target": "_blank",
        # }

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f'{prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
