import unittest

from one_of_eleven_board.ring.ring import RingController


class RingTest(unittest.TestCase):
    def test_step_fade_out(self):
        with RingController(24, .05) as ring_controller:
            self.assertEqual(ring_controller.step_fade_out((255, 0, 0), .05, 2), (229.5, 0, 0))

    def test_create_trail(self):
        with RingController(24, .05) as ring_controller:
            self.assertEqual(ring_controller.get_index_seq(0, 7), (0, 1, 2, 3, 4, 5, 6))


if __name__ == '__main__':
    unittest.main()