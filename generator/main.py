from name_provider.random_name_provider import RandomNameProvider
from build_file_generator.python_build_file_generator import PythonBuildFileGenerator
from code_generator.python_code_generator import PythonCodeGenerator
from structure.structure import *
from anytree import PostOrderIter
import argparse

default_depth = 4
default_width = 2


def main(path, depth, width):
    tree = create_tree(depth, width)
    label_tree(tree)
    generate_build_files(tree, path)
    generate_code_files(tree, path)
    print_tree(tree)


def generate_build_files(tree, path):
    PythonBuildFileGenerator(path, tree).generate()


def generate_code_files(tree, path):
    PythonCodeGenerator(path, tree).generate()


def label_tree(root):
    name_provider = RandomNameProvider()
    names = {}
    for node in PostOrderIter(root):
        label = name_provider.get_name()
        while label in names:
            label = name_provider.get_name()

        node.label = label


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Bazel project generator')
    parser.add_argument('-d', '--depth', type=int,
                        help='depth of the generated project')
    parser.add_argument('-w', '--width', type=int,
                        help='width of the generated project')
    parser.add_argument('path', metavar='path',
                        help='output path of the generator')

    args = parser.parse_args()
    main(args.path, args.depth or default_depth, args.width or default_width)
