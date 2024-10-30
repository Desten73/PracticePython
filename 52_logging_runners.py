import logging
from unittest import TestCase, skipIf
from rt_with_exceptions import Runner


class RunnerTest(TestCase):
    is_frozen = False

    @skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:
            runner = Runner("Max", -5)
            for _ in range(10):
                runner.walk()
        except:
            logging.warning("Неверная скорость для Runner")
        else:
            logging.info("test_walk выполнен успешно")
        finally:
            self.assertEqual(runner.distance, 50)


    @skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            runner = Runner(13)
            for _ in range(10):
                runner.run()
        except:
            logging.warning("Неверный тип данных для объекта Runner")
        else:
            logging.info("test_run выполнен успешно")
        finally:
            self.assertEqual(runner.distance, 100)

    @skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runnerfirst = Runner("Max")
        runnersecond = Runner("Dag")
        for _ in range(10):
            runnerfirst.run()
            runnersecond.walk()
        self.assertNotEqual(runnerfirst.distance, runnersecond.distance)


logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="UTF-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")
