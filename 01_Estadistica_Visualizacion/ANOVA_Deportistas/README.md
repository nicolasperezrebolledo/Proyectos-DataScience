# Análisis de Variables Fisiológicas en Deportistas

## Descripción  
Este proyecto analiza **variables fisiológicas en deportistas** para evaluar el impacto del **deporte practicado** y el **género** en diferentes métricas. Se emplea el **Análisis de Varianza (ANOVA)** para determinar la significancia estadística de estas relaciones.

## Tecnologías utilizadas  
- **Lenguaje / Framework:** R  
- **Librerías o paquetes clave:**  
  - tidyverse  
  - ggplot2  
  - GGally  
  - gridExtra  
  - vioplot  
- **Algoritmos o modelos utilizados:**  
  - ANOVA One-Way  
  - ANOVA Two-Way  

## Resultados clave  

### **Análisis de la variable WCC (Células Blancas en Sangre)**  
- **Explicación breve del análisis:** Se realizó un **ANOVA Two-Way** para evaluar el efecto del deporte y el género en la cantidad de células blancas en sangre.  
- **Métricas relevantes o hallazgos:**  
  - No se encontraron diferencias significativas entre deportes (**p = 0.283**).  
  - No se encontraron diferencias significativas entre géneros (**p = 0.348**).  
  - La interacción entre deporte y género tampoco resultó significativa (**p = 0.109**).  
- **Conclusión:** La variable **WCC** es homogénea y no está influenciada por el deporte, el género ni su combinación.  

### **Análisis de la variable HC (Hematocrito)**  
- **Explicación breve del análisis:** Se realizó un **ANOVA Two-Way** para evaluar el efecto del deporte y el género en los niveles de hematocrito.  
- **Métricas relevantes o hallazgos:**  
  - Se encontraron diferencias significativas entre deportes (**p = 0.0343**).  
  - Se encontraron diferencias altamente significativas entre géneros (**p < 2e-16**).  
  - No se detectó interacción significativa entre deporte y género (**p = 0.5502**).  
- **Conclusión:** Tanto el **deporte** como el **género** influyen en los niveles de hematocrito, pero sus efectos son independientes entre sí.  



**Este análisis evidencia que variables fisiológicas como HC y BMI están significativamente influenciadas por el deporte practicado**, reflejando las demandas físicas específicas de cada disciplina. Además, el **género tiene un impacto relevante** en variables como HC, lo que es consistente con diferencias fisiológicas inherentes.  
**Por otro lado, variables como WCC y HG son más consistentes entre grupos**, mostrando una menor dependencia de los factores analizados. Esto destaca la importancia de considerar **tanto el deporte como el género** en el análisis de métricas fisiológicas en deportistas, lo que puede ser útil para diseñar **programas específicos de entrenamiento** o evaluar el impacto de disciplinas deportivas en la salud y el rendimiento físico.
