from dataclasses import dataclass


@dataclass
class Indenter:
    indent: int = -1

    def __enter__(self):
        self.indent += 1
        return self

    def print(self, text):
        print("    " * self.indent + text)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.indent -= 1


with Indenter() as indent:
    indent.print("Hi")
    with indent:
        indent.print("Talk is cheap!")
        with indent:
            indent.print("Show me the Code...")
    indent.print("Torvalds")
