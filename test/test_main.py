from unittest import TestCase

from main import main


class TestMain(TestCase):
    def test_main(self):
        data_path = "data.txt"

        with open(data_path, "r") as f:
            data_list = [x.strip() for x in f.read().split("\n")]

        data_len = len(data_list)

        chain = main(data_list)
        _ = [print(f"block# {block[1]}, block {block}") for block in chain]
        self.assertEqual(len(chain), data_len)
        for block in chain:
            if block[1] == 0:
                self.assertEqual(block[0], 0)
                self.assertEqual(
                    block,
                    (
                        0,
                        0,
                        data_list[0],
                        "69066afb0e1825d6de7a47385d92e3dec64783421e316ab38ee7c68c17220992",
                    ),
                )
            else:
                self.assertEqual(block[0], chain[block[1] - 1][3])


if __name__ == "__main__":
    unittest.main()
