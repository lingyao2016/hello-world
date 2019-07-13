import pstats

'''
python -m cProfile -o profile.stats del.py
'''

infile = 'profile.stats'

p = pstats.Stats(infile)
# p.strip_dirs().sort_stats(-1).print_stats()

p.strip_dirs().sort_stats('cumulative', 'name').print_stats(0.5)
