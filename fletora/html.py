class Tag:
    def __init__(self, tag_name: str, *children, **attrs):
        self.tag_name = tag_name
        self.attrs = {("class" if k == "klass" else k): v for k, v in attrs.items()}
        self.children = []

        for child in children:
            if isinstance(child, (Tag, str)):  # Allow Tag objects and strings
                self.children.append(child)
            else:
                raise TypeError("Children must be of type Tag or str")

    def render(self) -> str:
        """Generate HTML from the Tag structure."""
        attrs = " ".join(f'{key}="{value}"' for key, value in self.attrs.items())
        attrs = f" {attrs}" if attrs else ""  # Add space before attributes if any
        children_html = "".join(
            child.render() if isinstance(child, Tag) else str(child)
            for child in self.children
        )
        return f"<{self.tag_name}{attrs}>{children_html}</{self.tag_name}>"

    def __str__(self):
        self.render()
