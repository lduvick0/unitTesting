import unittest
import unitTester
class testTime(unittest.TestCase):
    def testroyalflush(self):
        self.assertEqual(unitTester.check_royal_flush('S2', 'S3', 'S4'), 0)

    def testStraight(self):
        self.assertEqual(unitTester.check_straight('S3', 'S4','S5'), 5)

    def testThreePair(self):
        self.assertEqual(unitTester.check_3ofa_kind('S8','S8', 'S8'),8)

    def testfailstraight(self):
        self.assertEqual(unitTester.check_straight('S8','S2','S3'), 0)


    def testfailThreePair(self):
        self.assertEqual(unitTester.check_3ofa_kind('S3','S2','S3'),0)

    def testfailFlush(self):
        self.assertEqual(unitTester.check_royal_flush('SQ','SK','SA'),14)

    def testGame(self):
        self.assertEqual(unitTester.play_cards('S2','S3','S3', 'SQ','SK','SA'),1)

    def testGame2(self):
        self.assertEqual(unitTester.play_cards('S3','S3','S3', 'SQ','SK','SK'), -1)
    def testGameTie(self):
        self.assertEqual(unitTester.play_cards('S3','S3','S3', 'S3','S3','S3'),0)