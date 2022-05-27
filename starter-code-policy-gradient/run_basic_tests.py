import unittest
import sys, os
sys.path.append(os.path.join(sys.path[0],'pg'))

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('tests')
    unittest.TextTestRunner(verbosity=2).run(suite)