import unittest

class TestUser(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    print("class: start")

  @classmethod
  def tearDownClass(cls):
    print("class: stop")

  def setUp(self):
    print("case: start")
  
  def tearDown(self):
    print("case: stop")

  def test_01(self):
    print("case: test_01")

  def test_02(self):
    print("case: test_02")

if __name__ == '__main__':
  # unittest.main()
  suite = unittest.TestSuite()
  suite.addTest(TestUser('test_01'))
  suite.addTest(TestUser('test_02'))
  unittest.TextTestRunner().run(suite)