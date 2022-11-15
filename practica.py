#consume los datos del archivo suelo.csv
#almacena en un dataFrame el NOM_ENS, la superficie y el TIPUSSOL
#gráfico de dispersión de los totales de superficie por TIPUSSOL
#gráfico de barras de la supeficie media de los 10 primeros NOM_ENS
#gráfico circular de las superficie de 10 TIPUSSOL

import pandas as pd
import matplotlib.pyplot as plt

def consumirInversiones():
    datos=pd.read_csv('suelo.csv')
    #print(datos)
    df=datos[['NON_ENS','SUPERFICIE','TIPUSSOL']]
    #print(df)
    df.plot.scatter(x='SUPERFICIE', y='TIPUSSOL', alpha=0.3)
    plt.show()

consumirInversiones()