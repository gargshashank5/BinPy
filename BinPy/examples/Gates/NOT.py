from __future__ import print_function
from BinPy.Gates import *
""" Examples for NOT class """
print ("\n---Initializing the NOT class--- ")
print ("gate = NOT(0)")
gate = NOT(0)
print ("\n---Output of the NOT gate----")
print ("gate.output()")
print (gate.output())
print ("\n---Input changes---")
print ("gate.setInput(1) #Input ischanged to 0")
gate.setInput(1)
print ("\n---To get the input states---")
print ("gate.getInputStates()")
print (gate.getInputStates())
print ("\n---New Output of the NOT gate---")
print (gate.output())
print ("\n\n---Using Connectors as the input lines---")
print ("Take a Connector")
print ("conn = Connector()")
conn = Connector()
print ("\n---Set Output of gate to Connector conn---")
print ("gate.setOutput(conn)")
gate.setOutput(conn)
print ("\n---Put this connector as the input to gate1---")
print ("gate1 = NOT(conn)")
gate1 = NOT(conn)
print ("\n---Output of the gate1---")
print ("gate1.output()")
print (gate1.output())
