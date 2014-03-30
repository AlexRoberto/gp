# -*- coding: utf-8 -*-
import sys

from genetic_programming.gp import Genetic_Programming
from genetic_programming.utils import Utils


def main():
    util = Utils()
    gp = Genetic_Programming(util.args(sys.argv[1]))
    gp.gp_facade()
    gp.basic_information()
if __name__ == '__main__':
    main()