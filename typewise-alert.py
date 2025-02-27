# Daniel Meza
# Embedded SW Developer
# Typewise Alert.py
##The objective of the code is to monitor battery temperature and prevent damage:


def infer_breach(value, lowerLimit, upperLimit):
    if value < lowerLimit:
        return 'TOO_LOW'
    if value > upperLimit:
        return 'TOO_HIGH'
    return 'NORMAL'

def classify_temperature_breach(coolingType, temperatureInC):
    #Now uses a dictionary to store temperature limits by cooling type, 
    ##making the code more readable and easier to maintain.
    cooling_limits = {
        'PASSIVE_COOLING': {'lowerLimit': 0, 'upperLimit': 35},
        'HI_ACTIVE_COOLING': {'lowerLimit': 0, 'upperLimit': 45},
        'MED_ACTIVE_COOLING': {'lowerLimit': 0, 'upperLimit': 40}
    }
    limits = cooling_limits.get(coolingType, {'lowerLimit': 0, 'upperLimit': 0})
    return infer_breach(temperatureInC, limits['lowerLimit'], limits['upperLimit'])

def check_and_alert(alertTarget, batteryChar, temperatureInC):
  #The check_and_alert function decides whether to send the classification to the controller or by email, 
  ##depending on the purpose of the alert. 
  ###This fulfills the requirement to transmit the classification appropriately.
    breachType = classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
    if alertTarget == 'TO_CONTROLLER':
        send_to_controller(breachType)
    elif alertTarget == 'TO_EMAIL':
        send_to_email(breachType)

def send_to_controller(breachType):
    header = 0xfeed  #The value 0xfeed in decimal is 65261
    print(f'{header}, {breachType}') #Print NORMAL If the temperature is within normal limits

def send_to_email(breachType):
    recepient = "daniel_Test01@bosch.com"
    if breachType == 'TOO_LOW':
        print(f'To: {recepient}')
        print('Hi, the temperature is too low')
    elif breachType == 'TOO_HIGH':
        print(f'To: {recepient}')
        print('Hi, the temperature is too high')
