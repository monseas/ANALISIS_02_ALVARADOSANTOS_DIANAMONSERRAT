#!/usr/bin/env python
# coding: utf-8

# In[89]:


#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# %%

#Lectura del archivo 
base_logistics = pd.read_csv("synergy_logistics_database.csv", index_col=0)


# Las 10 rutas más demandadas

# In[90]:


#Tipo de direccion de importaciones
base_importaciones=base_logistics.loc[base_logistics['direction']=='Imports']
#Tipo de direccion de exportaciones
base_exportaciones=base_logistics.loc[base_logistics['direction']=='Exports']


# In[91]:


#Utilizar count, para las importaciones
base_importaciones_c=base_importaciones[['origin','destination']].value_counts()
print("Las rutas mas demandadas para importar son:\n",base_importaciones_c[0:10])


# In[92]:


#Utilizar count, para las exportaciones
base_exportaciones_c=base_exportaciones[['origin','destination']].value_counts()
print("Las rutas mas demandas para exportar son:\n",base_exportaciones_c[0:10])


# Los tres medios de transporte más utilizados según el valor de importaciones y exportaciones 

# In[93]:


#Crear un diccionario para obtener las impt según el tipo de transporte 
transp_impt=base_importaciones['transport_mode'].unique()
transp_total={}
for transport in transp_impt:
    base_importaciones_c=base_importaciones.loc[base_importaciones['transport_mode']==transport]
    transp_total[transport]=base_importaciones_c['total_value'].sum()

#print(transp_total)

import operator
transp_total_sort = sorted(transp_total.items(), key=operator.itemgetter(1), reverse=True)
#print(transp_total_sort)


# In[94]:


for n in enumerate(transp_total_sort):
    print('El transporte por: ',n[1][0], 'tiene ', n[1][1],'de importaciones')


# In[95]:


#Crear un diccionario para obtener las expt según el tipo de transporte 
transp_expt=base_exportaciones['transport_mode'].unique()
transp_total_2={}
for transport in transp_expt:
    base_exportaciones_c=base_exportaciones.loc[base_exportaciones['transport_mode']==transport]
    transp_total_2[transport]=base_exportaciones_c['total_value'].sum()

#print(transp_total)

import operator
transp_total_2_sort = sorted(transp_total_2.items(), key=operator.itemgetter(1), reverse=True)
#print(transp_total_sort)


# In[96]:


for n in enumerate(transp_total_2_sort):
    print('El transporte por: ',n[1][0], 'tiene ', n[1][1],'de exportaciones')


# Valor total de las importaciones si se enfocara en países que generan el 80%

# In[97]:


#Total de importaciones en terminos de dinero 
import_mon=base_importaciones['total_value'].sum()
print('El total de importaciones es: $',import_mon)


# In[98]:


#Origenes para las importaciones
origin_impt=base_importaciones['origin'].unique()

#Segun el origen asignarle su total 
prov_tot=[]
for origin in origin_impt: 
    prov=base_importaciones.loc[base_importaciones['origin']==origin]
    prov_tot.append([origin,prov['total_value'].sum()])
print(prov_tot)


# In[105]:


#Dataframe para relacionar el total con el país 

prov_frame=pd.DataFrame(prov_tot, columns=['Origin','total_value'])
prov_frame=prov_frame.sort_values(by=['total_value'],ascending=False)
prov_frame['percent']=(prov_frame['total_value']/import_mon)
prov_frame['cum_percent']=prov_frame['percent'].cumsum()
print(prov_frame[:8])


# Valor total de las importaciones si se enfocara en países que generan el 80%

# In[100]:


#Total de exportaciones en terminos de dinero 
export_mon=base_exportaciones['total_value'].sum()
print('El total de exportaciones es: $',export_mon)


# In[101]:


#Origenes para las exportaciones
dest_expt=base_exportaciones['destination'].unique()

#Segun el origen asignarle su total 

dest_tot=[]
for dest in dest_expt: 
    destino=base_exportaciones.loc[base_exportaciones['destination']==dest]
    dest_tot.append([dest,destino['total_value'].sum()])
print(dest_tot)


# In[102]:


#Dataframe para relacionar el total con el país 

dest_frame=pd.DataFrame(dest_tot, columns=['destination','total_value'])
dest_frame=dest_frame.sort_values(by=['total_value'],ascending=False)
dest_frame['percent']=(dest_frame['total_value']/export_mon)
dest_frame['cum_percent']=dest_frame['percent'].cumsum()
print(dest_frame[:14])


# In[ ]:




