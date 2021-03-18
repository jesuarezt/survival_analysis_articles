#https://medium.com/loftbr/o-poder-da-an%C3%A1lise-de-sobreviv%C3%AAncia-no-mercado-imobili%C3%A1rio-f0b0f16a57b3

# tiempo de vida de muestra imuebles en una ventana de 10 meses

import pandas as pd
from lifelines import KaplanMeierFitter
from matplotlib import pyplot as plt

time_day_life = [150, 130, 300, 100, 80, 60, 270, 150, 82, 50]
tag_sale = [1,0,0,1,0,1,0,1,0,1]

df = pd.DataFrame( {'time_day_life' : time_day_life,
                 'tag_sale' : tag_sale})
df.sort_values('time_day_life', ascending=True)

print('Descriptive')
print( df.time_day_life.mean())
print('')
print(df.groupby('tag_sale').agg('mean'))
## Observamos que el tiempo de vida medio no es comparable entre los leads vendidos y no vendidso con respecto al promedio general

#Calculo del estadistico Kaplan-Meier
# Curva Kaplan-Meier
kmf = KaplanMeierFitter()
kmf.fit(durations= df.time_day_life, event_observed=df.tag_sale)
kmf.survival_function_

# Plot survival analysis
kmf.plot(label='Kaplan-Meier',
        figsize=(12,12),
        show_censors=True,
        at_risk_counts=True
        )
plt.xlabel('tiempo de vida inmueble  en dias', size=15)
plt.ylabel('Sobrevida - $P(T>t)$', size=15)
