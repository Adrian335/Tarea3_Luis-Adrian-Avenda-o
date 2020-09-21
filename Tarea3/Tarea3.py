#!/usr/bin/env python
# coding: utf-8

# In[1]:


import MasaResorte as mr
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.pyplot import *
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import axes3d


# In[2]:


def f(y0,t): # La gravedad no se tiene en cuenta gracias a que se puede hacer una transformación de calibración
    f1 = y0[1]  #La ecuación es: y''=-yw^2
    f2 = -y0[0]*w**2
    return np.array([f1,f2])


# In[25]:


t = np.linspace(0,50,1000) #Tiempo de integración
#Condiciones iniciales
y0 = mr.Oscilador(2,0.8,1).condicioninicial
w = mr.Oscilador(2,0.8,1).w
sol0=odeint(f,y0, t)

y1 = mr.Oscilador(3,0.9,5).condicioninicial
w= mr.Oscilador(3,0.9,5).w
sol1=odeint(f,y1, t)

y2= mr.Oscilador(10,0.5,8).condicioninicial
w= mr.Oscilador(10,0.5,8).w
sol2=odeint(f,y2, t)

y3= mr.Oscilador(5,0.2,3).condicioninicial
w = mr.Oscilador(5,0.2,3).w
sol3=odeint(f,y3, t)

y4= mr.Oscilador(5,0.1,0.3).condicioninicial
w = mr.Oscilador(5,0.1,0.3).w
sol4=odeint(f,y4, t)


#Ploteamos la solución de posición vs tiempo

font = {'weight' : 'bold', 'size'  :13}
plt.figure(figsize=(13,10))
plt.plot(t,sol0[:,0],label= 'm=2 k=0.8 y0=1')
plt.plot(t,sol1[:,0], label= 'm=3 k=0.9 y0=5')
plt.plot(t,sol2[:,0],label= 'm=10 k=0.5 y0=8')
plt.plot(t,sol3[:,0],label= 'm=5 k=0.2 y0=3')
plt.plot(t,sol4[:,0],label= 'm=5 k=0.1 y0=0.3')
plt.title('Posición VS Tiempo')
plt.xlabel('t[s]')
plt.ylabel('y(t)[m]')
plt.grid()
plt.rc('font',**font)
plt.legend()
plt.savefig('posición.jpg')
plt.show()


# # 3. Para el mismo conjunto de parámetros haga graficas de el espacio de fase
# 
# Dado a la poca claridad del punto he decido plotear todo junto y no como subplot, igualmente no hay perdida alguna de lo que se pide.

# In[26]:


font = {'weight' : 'bold', 'size'  :13}
plt.figure(figsize=(13,10))
plt.plot(sol0[:,0],sol0[:,1],label= 'm=2 k=0.8 y0=1')
plt.plot(sol1[:,0],sol1[:,1], label= 'm=3 k=0.9 y0=5')
plt.plot(sol2[:,0],sol2[:,1],label= 'm=10 k=0.5 y0=8')
plt.plot(sol3[:,0],sol3[:,1],label= 'm=5 k=0.2 y0=3')
plt.plot(sol4[:,0],sol4[:,1],label= 'm=5 k=0.1 y0=0.3')
plt.title('Velocidad VS Posición')
plt.xlabel('y[m]')
plt.ylabel('v[m/s]')
plt.grid()
plt.rc('font',**font)
plt.legend()
plt.savefig('fases1.jpg')
plt.show()


# # Subamortiguado
# 
# La ecuación a resolver es la siguiente
# 
# $\ddot{y} + 2\lambda\dot{y} + \omega^2 y=0$
# 
# donde $\lambda = \frac{\eta}{2m}$

# In[14]:


def T(y0,t): #Definimos la función
    T1 = y0[1]
    T2 = -2*l*y0[1]-y0[0]*w**2
    return np.array([T1,T2])


# In[27]:


t = np.linspace(0,50,1000) #Tiempo de integración
#Condiciones iniciales
yA0 = mr.OsciladorAmortiguado(2,0.8,1,3).condicioninicial
w = mr.OsciladorAmortiguado(2,0.8,1,3).w
l = mr.OsciladorAmortiguado(2,0.8,1,3).l
solA0=odeint(T,yA0, t)

yA1 = mr.OsciladorAmortiguado(3,0.9,5,0.1).condicioninicial
w= mr.OsciladorAmortiguado(3,0.9,5,0.1).w
l = mr.OsciladorAmortiguado(2,0.8,1,0.1).l
solA1=odeint(T,yA1, t)

yA2= mr.OsciladorAmortiguado(10,0.5,8,1).condicioninicial
w= mr.OsciladorAmortiguado(10,0.5,8,1).w
l = mr.OsciladorAmortiguado(2,0.8,1,1).l
solA2=odeint(T,yA2, t)

yA3= mr.OsciladorAmortiguado(5,0.2,3,0.5).condicioninicial
w = mr.OsciladorAmortiguado(5,0.2,3,0.5).w
l = mr.OsciladorAmortiguado(2,0.8,1,0.5).l
solA3=odeint(T,yA3, t)

yA4= mr.OsciladorAmortiguado(5,0.1,0.3,0.8).condicioninicial
w = mr.OsciladorAmortiguado(5,0.1,0.3,0.8).w
l = mr.OsciladorAmortiguado(2,0.8,1,0.8).l
solA4=odeint(T,yA4, t)


#Ploteamos la solución de posición vs tiempo

font = {'weight' : 'bold', 'size'  :13}
plt.figure(figsize=(13,10))
plt.plot(t,solA0[:,0],label= 'm=2 k=0.8 y0=1 $\eta=3$')
plt.plot(t,solA1[:,0], label= 'm=3 k=0.9 y0=5 $\eta=0.1$')
plt.plot(t,solA2[:,0],label= 'm=10 k=0.5 y0=8 $\eta=1$')
plt.plot(t,solA3[:,0],label= 'm=5 k=0.2 y0=3 $\eta=0.5$')
plt.plot(t,solA4[:,0],label= 'm=5 k=0.1 y0=0.3 $\eta=0.8$')
plt.title('Posición VS Tiempo')
plt.xlabel('t[s]')
plt.ylabel('y(t)[m]')
plt.grid()
plt.rc('font',**font)
plt.legend()
plt.savefig('posición2.jpg')
plt.show()


# In[28]:


font = {'weight' : 'bold', 'size'  :13} #Ploteamos el espacio de fase
plt.figure(figsize=(13,10))
plt.plot(solA0[:,0],solA0[:,1],label= 'm=2 k=0.8 y0=1 $\eta=3$')
plt.plot(solA1[:,0],solA1[:,1], label= 'm=3 k=0.9 y0=5 $\eta=0.1$')
plt.plot(solA2[:,0],solA2[:,1],label= 'm=10 k=0.5 y0=8 $\eta=1$')
plt.plot(solA3[:,0],solA3[:,1],label= 'm=5 k=0.2 y0=3 $\eta=0.5$')
plt.plot(solA4[:,0],solA4[:,1],label= 'm=5 k=0.1 y0=0.3 $\eta=0.8$')
plt.title('Velocidad VS Posición')
plt.xlabel('y[m]')
plt.ylabel('v[m/s]')
plt.grid()
plt.rc('font',**font)
plt.legend()
plt.savefig('fases2.jpg')
plt.show()


# $\beta$

# In[ ]:




