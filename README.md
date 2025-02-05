<H1>Predictor de Abandono de Clientes</H1>
</BR>
<H3>¡Somos el Equipo C23-17-Data y les presentamos nuestro MVP!</H3>
</BR>
<H2>Análisis Descriptivo y Predictivo de Clientes para Detección de Abandonos</H2>

## **Descripción y objetivo del proyecto:**

### Situación inicial

La pérdida de clientes es un problema de millones de dólares para las empresas de hoy. El mercado de SaaS está cada vez más saturado y los clientes pueden elegir entre muchos proveedores. La retención y el mantenimiento de los clientes son un desafío. Los negocios online consideran que los clientes se dan de baja cuando dejan de comprar bienes y servicios. La pérdida de clientes puede depender de factores específicos de la industria, pero algunos impulsores comunes incluyen la falta de uso del producto, la duración del contrato y los precios más baratos en otros lugares.

Limitar la pérdida de clientes fortalece sus flujos de ingresos. Las empresas y los vendedores deben predecir y prevenir la pérdida de clientes para seguir siendo sostenibles. La mejor manera de hacerlo es conocer a sus clientes. Y detectar patrones de comportamiento en datos históricos puede ayudar enormemente con esto. Entonces, ¿cómo los descubrimos?

La aplicación del aprendizaje automático (ML) a los datos de los clientes ayuda a las empresas a desarrollar programas enfocados en la retención de clientes. Por ejemplo, un departamento de marketing podría usar un modelo de pérdida de ML para identificar clientes de alto riesgo y enviar contenido promocional para atraerlos.

Para que estos modelos puedan hacer predicciones con nuevos datos, es fundamental saber cómo empaquetar un modelo como una aplicación interactiva orientada al usuario. En este blog, trasladaremos un modelo de ML de un entorno de Jupyter Notebook a una aplicación en contenedores. Usaremos Streamlit como nuestro marco de aplicación para crear componentes de interfaz de usuario y empaquetar nuestro modelo. A continuación, usaremos Docker para publicar nuestro modelo como punto de conexión.

La contenedorización de Docker ayuda a que esta aplicación sea independiente del hardware y del sistema operativo. Los usuarios pueden acceder a la aplicación desde su navegador a través del punto de conexión, ingresar los detalles del cliente y recibir una probabilidad de abandono en una fracción de segundo. Si la puntuación de abandono de un cliente supera un umbral determinado, ese cliente puede recibir notificaciones push específicas y ofertas especiales. El diagrama a continuación pone esto en perspectiva:

</BR>
<div style="display: flex; justify-content: center; align-items: center; width: 100%;">
    <img style="width: 95%;" src="/images/diagramastreamlitdocker.jpg" />
</div>
</BR>

Nuestro cliente, una empresa de Telecomunicación, identificó un problema creciente: **abandono de clientes**. Para abordar este desafío, nos pidieron analizar los datos de sus clientes, con dos objetivos claros:

1️⃣ **Entender el comportamiento de los clientes y encontrar patrones**. </BR> (ver notebook [Churn_EDA_model_development.ipynb](https://github.com/No-Country-simulation/equipo-c23-17-data/blob/main/Churn_EDA_model_development.ipynb))

2️⃣ **Desarrollar un modelo predictivo** que permitiera calcular la probabilidad de que un cliente abandone la compañía.
</BR>
(ver https://equipo-c23-17-data-main.streamlit.app/ )

> [!NOTE]
> Fuente del proyecto: [Kaggle dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)



</BR>

## **Diccionario de datos**


| Nombre de la columna         | Tipo de dato          | Descripción |
|-----------------------------|----------------------|-------------|
| `gender`                        | `object`                | El género de una persona. |
| `seniorcitizen`     | `int64`           | Si un cliente puede clasificarse como un ciudadano de la tercera edad. |
| `partner`                    | `object`             | Si un cliente está casado/ vive con su pareja. |
| `dependents`                  | `object`       | Si un cliente tiene dependientes (hijos/ padres jubilados. |
| `phoneservice`                  | `object`        | Si un cliente tiene un servicio de teléfono fijo junto con el servicio de Internet. |
| `multiplelines`              | `object`      | Si un cliente tiene varias líneas de conectividad a Internet. |
| `internetservice`                | `object`        | El tipo de servicios de Internet elegidos por el cliente. |
| `onlinesecurity`                 | `object`        | Especifica si un cliente tiene seguridad en línea. |
| `onlinebackup`                    | `object`            | Especifica si un cliente tiene copia de seguridad en línea. |
| `deviceprotection`                    | `object`       | Especifica si un cliente ha optado por la protección del dispositivo. |
| `techsupport`                      | `object`       | Si un cliente ha optado por el soporte técnico o no. |
| `streamingtv`                | `object`            | Si un cliente tiene la opción de transmisión de TV. |
| `streamingmovies`                       | `object`        | Si un cliente tiene la opción de transmisión de películas. |
| `contract`                  | `object`       | El tipo de contrato que ha elegido un cliente. |
| `paperlessbilling`                 | `object`       | Si un cliente ha optado por la facturación sin papel. |
| `paymentmethod`           | `object`                | Especifica el método por el cual se pagan las facturas. |
| `tenure`                       | `int64`       | El tiempo durante el cual un cliente ha estado utilizando el servicio. |
| `monthlycharges`                       | `float64`               | El dinero total que el cliente pagó a la empresa. |
| `totalcharges`                 | `object`        | Identificador único de la transacción. |


<H2> Construyendo un modelo simple de aprendizaje automático </H2>

El aprendizaje automático utiliza algoritmos y modelos estadísticos. Estos analizan datos históricos y hacen inferencias a partir de patrones sin ninguna programación explícita. En última instancia, el objetivo es predecir resultados basados en los datos entrantes.

En nuestro caso, estamos creando un modelo a partir de datos históricos de clientes para predecir qué clientes tienen más probabilidades de abandonar. Dado que necesitamos clasificar a los clientes como baja o no baja, entrenaremos un modelo de clasificación simple pero potente. Nuestro modelo utiliza regresión logística en un conjunto de datos históricos de clientes de una empresa de telecomunicaciones. Este conjunto rastrea la demografía del cliente, la antigüedad, los cargos mensuales y más. Sin embargo, también se responde una pregunta clave: ¿el cliente abandonó?

La regresión logística estima la probabilidad de un evento basándose en un conjunto de datos dado de variables independientes. Dado que el resultado es una probabilidad, la variable dependiente está acotada entre 0 y 1. El modelo se someterá a múltiples iteraciones y calculará los coeficientes de mejor ajuste para cada variable. Esto cuantifica cuánto impacta cada uno en la deserción. Con estos coeficientes, el modelo puede asignar puntajes de probabilidad de deserción entre 0 y 1 a los nuevos clientes. Alguien que obtenga un puntaje de 1 tiene una probabilidad extremadamente alta de abandonar. Alguien con un 0 tiene una probabilidad increíblemente baja de abandonar.

Python tiene excelentes bibliotecas como Pandas, NumPy y Matplotlib que admiten el análisis de datos. Los marcos de código abierto como Scikit Learn tienen wrappers preconstruidos para varios modelos de ML. Usaremos su API para entrenar un modelo de regresión logística. Para comprender cómo nació este modelo básico de predicción de deserción, consulte [Churn_EDA_model_development.ipynb](https://github.com/No-Country-simulation/equipo-c23-17-data/blob/main/Churn_EDA_model_development.ipynb).

En resumen, realizamos los siguientes pasos para crear nuestro modelo de predicción de deserción:

### 1. Preparación inicial de datos
  - Realizar comprobaciones de cordura en los tipos de datos y los nombres de las columnas
  - Realizar correcciones de tipo de datos si es necesario
    
### 2. Comprensión de datos y características
  - Verificar la distribución de las características numéricas
  - Verificar los valores distintos de las características categóricas
  - Verificar la distribución de la característica objetivo
    
### 3. Análisis exploratorio de datos
  - Manejar los valores faltantes
  - Manejar los valores atípicos
  - Comprender las correlaciones e identificar las espurias
    
### 4. Ingeniería de características e importancia
  - Analizar la tasa de deserción y los puntajes de riesgo en diferentes cohortes y grupos de características
  - Calcular la información mutua
  - Verificar las correlaciones de características
  
### 5. Codificación de características categóricas y escalado de características numéricas
  - Convertir las características categóricas en valores numéricos utilizando la función auxiliar de Scikit-Learn: Dictionary Vectoriser
  - Escalar las características numéricas para estandarizarlas en un rango fijo
  
### 6. Entrenamiento del modelo
  - Seleccionar un algoritmo de ML apropiado
  - Entrenar el modelo con parámetros personalizados

### 7. Evaluación del modelo
  - Consulte [Churn_EDA_model_development.ipynb](https://github.com/No-Country-simulation/equipo-c23-17-data/blob/main/Churn_EDA_model_development.ipynb).
  - Utilizar diferentes métricas para evaluar el modelo, como la precisión, la tabla de confusión, la precisión, la exhaustividad, las curvas ROC, AUROC y la validación cruzada.
    
### 8. Repetimos los pasos 6 y 7 para diferentes algoritmos e hiperparámetros del modelo, luego seleccione el modelo de mejor ajuste.
Es una buena práctica automatizar el proceso de entrenamiento usando un script de Python. Cada vez que elegimos volver a entrenar el modelo con un nuevo parámetro o un nuevo conjunto de datos, podemos ejecutar este script y guardar el modelo resultante.

Consulte [train.py](https://github.com/No-Country-simulation/equipo-c23-17-data/blob/main/train.py)  para explorar cómo empaquetar un modelo en un script que automatiza el entrenamiento del modelo

Una vez que descubrimos el modelo de mejor ajuste, debemos guardarlo para reutilizarlo más adelante sin ejecutar ninguno de los scripts del código de entrenamiento anteriores.  

<H2> Disponibilizando el servicio de predicción a través de una aplicación web con Streamlit </H2>

La barra lateral de Streamlit presenta una menu desplegable donde los usuarios pueden seleccionar el tipo de predicción del modelo que desean realizar: por lotes (BATCH - predicciones para múltiples clientes, cargando un archivo csv) o predicción en línea (ONLINE - para clientes individuales).

<H2> Conclusión </H2>

Este análisis desarrollado en [Churn_EDA_model_development.ipynb](https://github.com/No-Country-simulation/equipo-c23-17-data/blob/main/Churn_EDA_model_development.ipynb) no solo ayudó al cliente a comprender mejor los patrones de comportamiento en de sus clientes, sino que también le proporcionó una herramienta poderosa para **anticiparse y mitigar riesgos**, por ejemplo realizando una campaña de marketing con aquellos clientes para los cuales se predice un abandono. Con esta solución empresa está ahora mejor equipada para fidelizar sus clientes y asignar eficientemente sus recursos en campañas de marketing.

## Integrantes

- José Fernández Madero: [GitHub](https://github.com/josefmadero)
- Melissa Londoño: [GitHub](https://github.com/melissa9608)

## Tecnologías

<img align="left" alt="Python" width="50px" style="padding-right:10px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg"/>
<img align="left" alt="Pandas" width="50px" style="padding-right:10px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pandas/pandas-original-wordmark.svg"/>
<img align="left" alt="Numpy" width="50px" style="padding-right:10px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/numpy/numpy-plain.svg"/>
<img align="left" alt="Scikit-learn" width="50px" style="padding-right:10px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/scikitlearn/scikitlearn-original.svg"/>
<img align="left" alt="Jupyter" width="50px" style="padding-right:10px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jupyter/jupyter-original.svg"/>
<img align="left" alt="Streamlit" width="50px" style="padding-right:10px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/streamlit/streamlit-plain-wordmark.svg"/>
