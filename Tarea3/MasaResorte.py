#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Oscilador: #Definimos la clase
    def __init__(self,m,k,y0): 
        import numpy as np #Importamos numpy para definir omega
        self.m=m
        self.k=k
        self.y0=y0
        self.w=np.sqrt(self.k/self.m)
        self.condicioninicial=[self.y0,0]
class OsciladorAmortiguado: #Definimos la clase
    def __init__(self,m,k,y0,a): 
        import numpy as np #Importamos numpy para definir omega
        self.m=m
        self.k=k
        self.y0=y0
        self.a=a
        self.w=np.sqrt(self.k/self.m)
        self.condicioninicial=[self.y0,0]
        self.l=self.a/(2*self.m)

