class Template:
    """Template engine for rendering text with context"""
    def __init__(self, text: str):
        self._text = text

    def render(self, ctx: dict) -> str:
        return self._text