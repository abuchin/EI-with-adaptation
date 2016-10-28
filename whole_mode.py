# -*- unicode:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

""" study of what happens if we include the dynamic fo Nai in the Nap neuron """

def equation(s1, s2, s3, s4, s5, s6, parameters):
	gamma1, tau, beta, gNa, gK, gahp, gkl, gnal, gcil, phi, Vcl, gCa, VCa, beta, rho, Gglia, epsilon, k0inf, cli, cl0 = parameters


	Na0 = 144. - beta*(s5-18.)
	Ki = 140. + 18. - s5

	alpham = 0.1*(s1+30.)/(1.-np.exp(-0.1*(s1+30.)))
	betam = 4.*np.exp(-(s1+55.)/18.)
	alphan = 0.01*(s1+34.)/(1.-np.exp(-0.1*(s1+34.)))
	betan = 0.125*np.exp(-(s1+44.)/80.)
	alphah = 0.07*np.exp(-(s1+44.)/20.)
	betah = 1./(1.+np.exp(-0.1*(s1+14.)))

	minf = alpham/(alpham+betam)
	VNa = 26.64 * np.log(Na0/s5)
	Vk = 26.64 * np.log(s6/Ki)
	Vcl = 26.64 * np.log(cli/cl0)

	INa = gNa*(minf**3)*s3*(s1-VNa) + gnal*(s1-VNa)
	IK = (gK*(s2**4) + gahp*s4/(1+s4))*(s1-Vk) + gkl*(s1-Vk)
	ICl = gcil*(s1-Vcl)

	Ipump = rho/(1+np.exp((25.-s5)/3.)) * 1./(1.+np.exp(5.5-s6))
	Iglia = Gglia / (1. + np.exp((18.-s6)/2.5))
	Idiff = epsilon * (s6-k0inf)

	#V
	ds1 = - INa - IK - ICl
	#n
	ds2 = phi*(alphan*(1-s2) - betan*s2)
	#h
	ds3 = phi*(alphah*(1-s3) - betah*s3)
	#Cai
	ds4 = -0.002 * gCa * (s1-VCa)/(1+np.exp(-(s1+25.)/2.5)) -s4/80.
	#Nai
	ds5	=1./tau*( -gamma1* INa - 3*Ipump)
	#K0
	ds6 =1./tau*( gamma1*beta*IK - 2. * beta * Ipump - Iglia - Idiff)

	return (ds1, ds2, ds3, ds4, ds5, ds6)

def euler(s1, s2, s3, s4, s5, s6, ds1, ds2, ds3, ds4, ds5, ds6, dt):
	return(s1+ds1*dt, s2+ds2*dt, s3+ds3*dt, s4+ds4*dt, s5+ds5*dt, s6+ds6*dt)


def main():
	dt = 0.01
	y1 = []
	y2 = []
	y3 = []
	y4 = []
	y5 = []
	y6 = []

	s1 = -50.
	s2 = 0.08553
	s3 = 0.96859
	s4 = 0.0
	s5 = 15.5
	s6 = 7.8
	ds1 = 0.
	ds2 = 0.
	ds3 = 0.
	ds4 = 0.
	ds5 = 0.
	ds6 = 0.

	# gL, EL, gNa, gK, Vm, km, Vn, kn
	gamma1 = 0.044494542
	tau = 1000.0
	beta = 7.0

	gNa = 100.
	gK = 40.
	gahp = 0.01
	gkl = 0.05
	gnal = 0.0175
	gcil = 0.05
	phi = 3.
	Vcl = -81.93
	gCa = 0.1
	VCa = 120.
	beta = 7.
	rho = 1.25
	Gglia = 66.
	epsilon = 1.2 
	k0inf = 8.
	cli = 6.
	cl0 = 130.
	parameters = (gamma1, tau, beta, gNa, gK, gahp, gkl, gnal, gcil, phi, Vcl, gCa, VCa, beta, rho, Gglia, epsilon, k0inf, cli, cl0)

	for i in np.arange(10000):
		ds1, ds2, ds3, ds4,ds5, ds6 = equation(s1, s2, s3, s4, s5, s6, parameters)
		s1, s2, s3, s4, s5, s6 = euler(s1, s2, s3, s4, s5, s6, ds1, ds2, ds3, ds4, ds5, ds6, dt)
		if i%100==0:
			print i
			y1.append(s1)
			y2.append(s2)
			y3.append(s3)
			y4.append(s4)
			y5.append(s5)
			y6.append(s6)

	np.save('cressman_time_series.npy', np.array([y1, y2, y3, y4, y5, y6]))
	plt.figure()
	plt.subplot(611)
	plt.plot(y1)
	plt.subplot(612)
	plt.plot(y2)
	plt.subplot(613)
	plt.plot(y3)
	plt.subplot(614)
	plt.plot(y4)
	plt.subplot(615)
	plt.plot(y5)
	plt.subplot(616)
	plt.plot(y6)

	plt.show()

if __name__ == '__main__':
	main()
