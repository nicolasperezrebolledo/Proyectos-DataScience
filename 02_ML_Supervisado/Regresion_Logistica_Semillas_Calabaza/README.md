# Clasificación Semillas de Calabazas mediante Regresión Logística

## Descripción  
Este proyecto tiene como objetivo desarrollar un **modelo de regresión logística** para clasificar calabazas en dos tipos: **Urgup_Sivrisi (0)** y **Cercevelik (1)**. Se emplean técnicas de **selección de variables y reducción de dimensionalidad** para mejorar el rendimiento del modelo.

## Tecnologías utilizadas  
- **Lenguaje / Framework:** R  
- **Librerías o paquetes clave:**  
  - tidyverse, dplyr, purrr: Manipulación y transformación de datos.  
  - rsample: División de datos en entrenamiento y prueba.  
  - FSelectorRcpp: Selección de características basada en información mutua.  
  - ggplot2, GGally, gridExtra, patchwork: Visualización de datos.  
  - corrplot, ggcorrplot: Análisis de correlaciones.  
  - caret: Modelado y evaluación de clasificación.  
  - pROC: Evaluación del rendimiento con curva ROC y AUC.  

## Resultados clave  

### **Comparación de Modelos de Regresión Logística**  
Se evaluaron cinco modelos con diferentes estrategias de selección de variables:

| Modelo | Variables Seleccionadas | F1-Score | Accuracy | AIC |
|--------|-------------------------|----------|----------|------|
| **Modelo 0 (Base)** | 12 variables originales | 0.88 | 0.874 | 1143.103 |
| **Modelo 1 (Correlación)** | Compactness, Aspect_Ration_sqrt, Eccentricity, Roundness | 0.873 | 0.866 | 1289.092 |
| **Modelo 2 (Información Ganada)** | Compactness, Aspect_Ration_sqrt, Eccentricity, Roundness, Major_Axis_Length_sqrt, Minor_Axis_Length_sqrt | 0.875 | 0.868 | 1286.294 |
| **Modelo 3 (PCA Alta Correlación)** | Aspect_Ration_sqrt, Area_log, Convex_Area_log, Compactness, Equiv_Diameter_sqrt | 0.889 | 0.884 | 1195.969 |
| **Modelo 4 (PCA Alta y Moderada Correlación)** | Eccentricity, Compactness, Aspect_Ration_sqrt, Area_log, Perimeter_log, Convex_Area_log, Equiv_Diameter_sqrt | **0.890** | **0.884** | **1140.927** |

### **Evaluación del Modelo 4 (Ganador)**  

#### **Conjunto de Entrenamiento:**  
- **Accuracy:** 88.75%  
- **Balanced Accuracy:** 88.65%  
- **Sensibilidad:** 0.8604  
- **Especificidad:** 0.9125  
- **AUC:** 0.95  
- **Kappa:** 0.7743  

#### **Conjunto de Prueba:**  
- **Accuracy:** 88.4%  
- **Balanced Accuracy:** 88.32%  
- **Sensibilidad:** 0.8625  
- **Especificidad:** 0.9038  
- **AUC:** 0.9439  

## Conclusión  
**El Modelo 4 es el mejor**, logrando el mejor equilibrio entre **precisión, recall y selección eficiente de variables mediante PCA**.  
**PCA demostró ser una técnica eficaz** para seleccionar y reducir dimensiones de las variables, permitiendo mantener un alto desempeño con un modelo más compacto.  
**El modelo generaliza bien**, manteniendo un rendimiento sólido tanto en entrenamiento como en prueba, lo que lo hace adecuado para su uso en clasificación de calabazas en nuevos datos.
