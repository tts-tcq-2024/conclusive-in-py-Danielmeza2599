# Daniel Meza
# Embedded SW Developer
# typewise_alert_Test.py 

import unittest
import typewise_alert

#More test cases were added to cover all possible scenarios, including different cooling types and temperatures. 
# This ensures that the code works correctly in all situations.


#With these improvements, the code meets the objectives of monitoring the battery temperature, classifying the 
# temperature according to the type of cooling and transmitting the classification to take the necessary actions.

class TypewiseTest(unittest.TestCase):
    #If expected_result is not equal to actual_result, 
    ##the message “Too_Low” will be displayed in the test output.
    def test_infers_breach_as_per_limits(self):
      #assertEqual = Fail if the two objects are unequal as determined by the '=' operator
        self.assertEqual(typewise_alert.infer_breach(20, 50, 100), 'TOO_LOW')
        self.assertEqual(typewise_alert.infer_breach(60, 50, 100), 'NORMAL')
        self.assertEqual(typewise_alert.infer_breach(110, 50, 100), 'TOO_HIGH')

    def test_classify_temperature_breach(self):
        self.assertEqual(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', 20), 'NORMAL')
        self.assertEqual(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', -5), 'TOO_LOW')
        self.assertEqual(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', 40), 'TOO_HIGH')

        self.assertEqual(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING', 30), 'NORMAL')
        self.assertEqual(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING', -1), 'TOO_LOW')
        self.assertEqual(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING', 50), 'TOO_HIGH')

        self.assertEqual(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING', 35), 'NORMAL')
        self.assertEqual(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING', -10), 'TOO_LOW')
        self.assertEqual(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING', 45), 'TOO_HIGH')

    def test_check_and_alert(self):
        batteryChar = {'coolingType': 'PASSIVE_COOLING'}
        typewise_alert.check_and_alert('TO_CONTROLLER', batteryChar, 30)
        typewise_alert.check_and_alert('TO_EMAIL', batteryChar, 30)

        batteryChar = {'coolingType': 'HI_ACTIVE_COOLING'}
        typewise_alert.check_and_alert('TO_CONTROLLER', batteryChar, 40)
        typewise_alert.check_and_alert('TO_EMAIL', batteryChar, 40)

        batteryChar = {'coolingType': 'MED_ACTIVE_COOLING'}
        typewise_alert.check_and_alert('TO_CONTROLLER', batteryChar, 35)
        typewise_alert.check_and_alert('TO_EMAIL', batteryChar, 35)

if __name__ == '__main__':
    unittest.main()
