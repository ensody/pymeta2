"""
Public interface to OMeta, as well as the grammars used to compile grammar
definitions.
"""
from .builder import TreeBuilder, moduleFromGrammar
from .boot import BootOMetaGrammar
from .bootbase import BootBase

class OMeta(BootBase):
    """
    Base class for grammar definitions.
    """
    metagrammarClass = BootOMetaGrammar

    @classmethod
    def makeGrammar(cls, grammar, globals, name="Grammar"):
        """
        Define a new subclass with the rules in the given grammar.

        @param grammar: A string containing a PyMeta grammar.
        @param globals: A dict of names that should be accessible by this
        grammar.
        @param name: The name of the class to be generated.
        """
        g = cls.metagrammarClass(grammar)
        tree = g.parseGrammar(name, TreeBuilder)
        return moduleFromGrammar(tree, name, cls, globals)
