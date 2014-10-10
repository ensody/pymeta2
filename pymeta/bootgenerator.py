# Generates a boot grammar and stores it in boot_generated.py. If everything looks OK you can
# replace your boot.py with the generated module.
if __name__ == '__main__':
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    from pymeta.builder import TreeBuilder, writeBoot
    from pymeta.grammar_definition import OMetaGrammar, ometaGrammar
    ometa_grammar = OMetaGrammar(ometaGrammar)
    tree = ometa_grammar.parseGrammar('BootOMetaGrammar', TreeBuilder)
    path = os.path.join(os.path.dirname(__file__), 'boot_generated.py')
    with open(path, 'w') as fp:
        fp.write(writeBoot(tree))
