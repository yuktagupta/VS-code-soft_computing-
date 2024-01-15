import numpy as np
#pip install -U scikit-fuzzy 
import skfuzzy as fuzz 
from skfuzzy import control as ctrl
tipping =[]
view=[]

quality =ctrl.antecendent(np.arange(0,11,1),'quality')
service =ctrl.antecendent(np.arange(0,11,1),'service')
tip =ctrl.antecendent(np.arange(0,26,1),'tip')

quality.automf(3)
service.automf(3)

tip['low']=fuzz.trimf(tip.universe,[0,0,13])
tip['medium']=fuzz.trimf(tip.universe,[0,13,25])
tip['high']=fuzz.trimf(tip.universe,[13,25,25])

quality['average'],view()
service.view()
tip.view()

rule1 =ctrl.rule(quality['poor'] | service['poor'] | tip['poor'])
rule2 =ctrl.rule(quality['medium'] | service['midum'] | tip['medium'])
rule3 =ctrl.rule(quality['high'] | service['high'] | tip['high'])

rule1.view()

tipping_crtl =ctrl.contrlsystem([rule1,rule2,rule3])
tipping_crtl =ctrl.controlsystemsimulation(tipping_crtl)

tipping_crtl['quality']=6.5
tipping_crtl['service']=9.5


tipping.computer()

print(tipping.output['tip'])

tip.view(sim=tipping)
