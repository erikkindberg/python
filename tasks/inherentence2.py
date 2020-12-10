

"""
Change the class CustomParser so that the pipe_parse() runs.

restrictions:
1)  you are not allowed to change anything in the classes PosTagger and DependencyParser. You are neither allowed
    to change CustomParser.pipe_parse()

"""

class PosTagger:

    def tag_pos(self):
        return "tagging POS"
    

class DependencyParser:

    def parse_dep(self):
        return "parsing dependencies"

# CustomParser now inherits PosTagger, DependencyParsers and their methods.
class CustomParser(PosTagger, DependencyParser):
    # pipe_parse now runs when CustomParser is instantiated
    def __init__(self, fname, lname):
        print("CustomParser instantiated. Running pipe_parse()")
        self.pipe_parse()

    def pipe_parse(self):
        return self.tag_pos(), self.parse_dep()

parser = CustomParser("Erik", "Kindberg")