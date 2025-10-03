# Análisis de Sentimiento en Reviews de Apps con Naive Bayes

## Descripción  
Este proyecto tiene como objetivo construir un **modelo de Naive Bayes** para clasificar el **sentimiento de las reviews en Google Play Store** como **positivas o negativas**. Se exploraron varias técnicas para mejorar el rendimiento del modelo, incluyendo **Laplace Smoothing, TF-IDF, balanceo de clases y la inclusión de package_name como factor**.

## Tecnologías utilizadas  
- **Lenguaje / Framework:** R  
- **Librerías o paquetes clave:**  
  - tidyverse, dplyr, purrr: Manipulación y transformación de datos.  
  - caret: Modelado y evaluación de clasificación.  
  - pROC: Evaluación con curva ROC y métricas de desempeño.  
  - tm: Procesamiento de texto.  
  - text2vec: Implementación de TF-IDF.  
  - SnowballC: Lematización y procesamiento lingüístico.  

## Resultados clave  

### **Comparación de Modelos de Clasificación**  
Se evaluaron cuatro enfoques distintos para mejorar la precisión del modelo de Naive Bayes:

| Modelo | Técnica Aplicada | Accuracy | Sensibilidad | Especificidad |
|--------|-----------------|----------|--------------|--------------|
| **Naive Bayes con Laplace Smoothing** | Optimización de suavizado | 82.02% | 84.57% | 77.17% |
| **Naive Bayes con package_name** | Factor adicional en la matriz de términos | **83.52%** | **85.14%** | **80.43%** |
| **TF-IDF** | Transformación de términos ponderados | 32.4% | 0.00% | 100.00% |
| **Balanceo de Clases** | Sobremuestreo de clases minoritarias | 50.0% | 0.00% | 99.15% |

### **Evaluación del Mejor Modelo (Naive Bayes con package_name)**  
- **Accuracy:** 83.52%  
- **Sensibilidad:** 85.14% (capacidad para identificar correctamente las reseñas positivas)  
- **Especificidad:** 80.43% (capacidad para identificar correctamente las reseñas negativas)  
- **Balanced Accuracy:** 82.79%  
- **Kappa:** 0.6425 (buena concordancia con la clasificación real)  

### **Hallazgos Clave**  
- La inclusión de **package_name** mejoró el rendimiento del modelo, indicando que la **app de origen es una variable relevante** en la clasificación de sentimientos.  
- **Laplace Smoothing** fue útil para estabilizar el modelo, pero no mejoró significativamente la precisión en comparación con el modelo base.  
- **TF-IDF y balanceo de clases no mejoraron el desempeño**, lo que sugiere que la estructura de los datos originales ya era adecuada.  

## Conclusión  
**El modelo con Laplace Smoothing y package_name como factor es el mejor**, con una precisión del **83.52%** y un buen equilibrio entre **sensibilidad y especificidad**.  
**TF-IDF y balanceo de clases no fueron efectivos**, ya que no mejoraron la capacidad predictiva del modelo.  
**Vías abiertas para mejoras:**  
- Exploración de **Word Embeddings, SVM o redes neuronales** para mejorar la clasificación.  
- Incorporación de **nuevas variables** como la categoría de la app, número de descargas o calificaciones promedio.  
- Optimización de **preprocesamiento de texto** con técnicas avanzadas como **BERT o TF-IDF con ajustes específicos**.
