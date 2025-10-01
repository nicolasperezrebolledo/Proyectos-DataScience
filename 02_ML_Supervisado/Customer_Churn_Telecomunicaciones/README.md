# Análisis de Customer Churn en Empresa de Telecomunicaciones

## Descripción  
Este proyecto tiene como objetivo **identificar factores clave que contribuyen al churn de clientes** en una empresa de telecomunicaciones en **India**. Se utilizan técnicas de **análisis exploratorio, selección de variables y modelos de regresión logística** para predecir y prevenir la pérdida de clientes.

## Tecnologías utilizadas  
- **Lenguaje / Framework:** R  
- **Librerías o paquetes clave:**  
  - tidyverse, dplyr, ggplot2, purrr: Manipulación y visualización de datos.  
  - GGally, gridExtra, patchwork: Herramientas avanzadas de visualización.  
  - corrplot, ggcorrplot: Análisis y visualización de correlaciones.  
  - FSelectorRcpp: Selección de variables mediante información mutua.  
  - car, infotheo: Pruebas estadísticas y validaciones.  
  - rsample, caret, pROC: Modelado de machine learning y evaluación.  

## Resultados clave  

### **1. Análisis Exploratorio**  
- **Distribución de la variable objetivo (`is_churned`)**: Se identificó un **desbalance en la proporción de clientes** que hicieron churn.  
- **Relaciones clave**: Se analizaron correlaciones entre atributos y churn mediante visualizaciones y pruebas estadísticas.  

### **2. Selección de Variables**  
Se aplicaron múltiples técnicas para identificar las variables más relevantes:

- **Correlación**: Se seleccionaron **6 variables clave** con alta correlación con `is_churned`.  
- **PCA**: No proporcionó mejoras significativas en la selección de variables.  
- **ANOVA**: Confirmó que todas las variables seleccionadas presentaban **diferencias significativas** entre clientes que hicieron churn y los que no.  
- **Información Mutua**: No aportó nueva información relevante para la selección de variables.  

Las **variables finales** seleccionadas para el modelo fueron:

- `payments_completed_amount_first_7days`
- `payments_initiated`
- `given_permission_1`
- `given_permission_2`
- `number_of_cards`
- `is_referral`

### **3. Modelado de Regresión Logística**  
Se probaron varios modelos, incluyendo versiones con **datos originales, submuestreo y sobremuestreo**.

- **Mejor modelo:** `modelo_submuestreo_0`  
- **Métricas de desempeño:**  
  - **Accuracy:** 63,04%  
  - **Precision:** 62,18%  
  - **Recall:** 66,79%  
  - **F1-Score:** 64,40%  
  - **AUC:** 0.66  

El modelo logró un **buen balance entre precisión y recall**, permitiendo **identificar clientes en riesgo de churn** con un desempeño aceptable.  

## Conclusión  
 **El churn está influenciado principalmente por la actividad de pagos, el número de tarjetas y los permisos otorgados.**  

 **Recomendaciones para reducir el churn:**  
- **Incentivar la participación de nuevos clientes** con recompensas en los primeros pagos.  
- **Mejorar la experiencia de pago** mediante opciones más accesibles y automatizadas.  
- **Optimizar el programa de referidos** para fomentar la retención de clientes recomendados.  
- **Aprovechar los permisos otorgados** para ofrecer una experiencia más personalizada.  
- **Implementar estrategias proactivas dirigidas a clientes de alto riesgo.**  

Estos hallazgos pueden **servir como base para estrategias de retención y optimización de la experiencia del cliente** en la empresa. 
