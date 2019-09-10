
def waterphase():
	# caculation of the usage of 0.01M Au
	cc = 0.25e-3
	vol = eval(input("The volume(mL) you want is:\n"))
	cc_muye = 0.01
	vol_muye = cc*vol/cc_muye
	print (f"the usage of 0.01M AuNP is :\t {vol_muye:.3f} mL")

	#caculation of Na3Ct
	Au_molar = cc_muye * vol_muye #molar of Au mM
	M = 294.10 #molar mass of Na3Ct
	ratio = eval(input("The ratio you want is:\n"))
	m_Na3Ct = Au_molar * M * ratio
	print (f"the mass of Na3Ct is {m_Na3Ct:.3f} mg")
	



def HA():
	M_HA = 101.193 #g/mol
	density = 0.77 #g/mL
	c_HA_vol = density/M_HA #mol/mL
	vol_Hexane = eval(input("The vol of n-Hexane is (mL):\t"))#mL
	c_Hexane = 1e-6 #mol/mL
	vol_HA = c_Hexane * vol_Hexane/ c_HA_vol# mol/mL * mL / mol * mL
	print (c_HA_vol)
	print (f" {vol_HA:.4f}mL HA in {vol_Hexane:.2f} mL Hexane can prepare {c_Hexane:.5f} mol/L\nAnd {vol_Hexane*2/4.5} mL solution is needed\n Acetone:{vol_Hexane*0.5/4.5}" )


def OctA():
	M_OctA = 129.24 #g/mol
	density = 0.782 #g/mL
	c_OctA_vol = density/M_OctA #mol/mL molar of 1mL OctA 
	vol_Hexane = eval(input("The vol of AuNP is (mL):\t"))#mL
	
	c_Hexane = 0.1e-6 #mol/mL
	vol_OctA = c_Hexane / c_OctA_vol * vol_Hexane# mmol/L * mL / mmol * L
	print (c_OctA_vol)
	print (f" {vol_OctA:.4f}mL OctA in {vol_Hexane:.2f} mL Hexane can prepare {c_Hexane:.5f} mol/L" )


def NA():
	M_NA = 143.27 #g/mol
	density = 0.782 #g/mL
	c_NA_vol = density/M_NA #mol/mL
	vol_Hexane = eval(input("The vol of n-Hexane is (mL):\t"))#mL
	c_Hexane = 0.1e-6 #mol/mL
	vol_NA = c_Hexane * vol_Hexane / c_NA_vol# mol/mL * mL / mol * mL
	print ("c_NA_vol = ",c_NA_vol)
	print (f" {vol_NA:.4f}mL OctA in {vol_Hexane:.2f} mL Hexane can prepare {c_Hexane:.5f} mol/L" )

def DDA():
	#DDA is solid 
	M_DDA = 185.35#g/mol
	vol_Hexane = eval(input("The vol of Hexane is:\t"))#mL
	c_DDA = 0.08e-6 # mol/mL
	m_DDA = M_DDA *  vol_Hexane * c_DDA #g/mol * mol/mL *mL
	print (f" {m_DDA:.5f}g DDA in {vol_Hexane:.2f} mL Hexane can prepare {c_DDA:.8f} mol/L" )
	



def ODA():
	M_ODA = 269.51#g/mol
	vol_Au = eval(input("The vol of AuNP is:\t"))#mL
	c_ODA = 0.00001 # mol/mL
	m_ODA = M_ODA *  vol_Au * c_ODA #g/mol * mol/mL *mL
	print (f"The mass of ODA should be {m_ODA:.4f}g in {vol_Au:.2f} mL ethanol" )

method = input("Enter the method you want:\nWaterphase\nHA for HA transfer\nOctA for OctA transfer\nNA for NA transfer\nDDA for DDA transfer\nODA for ODA transfer\n")

if method[0].lower == "w": #if method[0] == "w" or method[0] == "W": simplify the code
	waterphase()
elif method[0].lower == "o":
	ODA()
elif method[0].lower() == "h":
	HA()
elif method[0].lower() == 'd':
	DDA()
elif method[0:2].lower() == "oct":
	OctA()
from math import *
r = 8e-7#cm
e = 2.67e8#M-1cm-1
A450 = 0.60567
c = A450/e#mol/L
N = 6.02e23
density = 19.32#g/cm3
V=4/3*pi*pow(r,3)#cm3
cm = c*N*density*V#mol/L/mol*g/cm3*cm3


