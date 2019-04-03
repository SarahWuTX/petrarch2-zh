import sys
from argparse import Namespace

from FromCorenlpConverter import FromCorenlpConverter
from petrarch2.petrarch2 import main as petrarch2_main


if __name__ == "__main__":
    # If you are using python2, the first two lines are needed.
    reload(sys)
    sys.setdefaultencoding('utf-8')

    input_path = 'input/news.txt'
    output_path = 'output/news'
    corenlp_path = ''
    port = 8000

    converter = FromCorenlpConverter(input_path, '', corenlp_path, port)
    converter.run()
    args = Namespace(command_name='batch', config=None, inputs=converter.output_path,
                     nullactors=False, nullverbs=False, outputs=output_path)
    petrarch2_main(args)



