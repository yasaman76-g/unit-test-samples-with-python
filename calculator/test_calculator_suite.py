import unittest
import test_calculator
import test_calculator_v2

loader = unittest.TestLoader()

suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test_calculator))
suite.addTests(loader.loadTestsFromTestCase(test_calculator_v2.TestsCalculatorV2))


runner = unittest.TextTestRunner()
#for show mor details : runner = unittest.TextTestRunner(verbosity=2)

runner.run(suite)

#to get details from runner
# runner_result = runner.run(suite)
# total_ran = runner_result.testsRun
# total_skiped = runner_result.skipped
# total_errors = runner_result.errors
# total_fails = runner_result.failures
# print("total ran ",total_ran)
# print("total skipped ",total_skiped)
# print("total errors ",total_errors)
# print("total fails ",total_fails)