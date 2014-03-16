# -*- coding: utf-8 -*-
import sys

from genetic_programming.gp import Genetic_Programming
from genetic_programming.utils import Utils


def main():
    util = Utils()
    args = util.args(sys.argv[1])
    gp = Genetic_Programming(args)
    gp.test()
    gp.gp()
if __name__ == '__main__':
    main()