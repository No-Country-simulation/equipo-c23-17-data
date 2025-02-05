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

Nuestro cliente, una empresa de Telecomunicación, identificó un problema creciente: **abandono de clientes**. Para abordar este desafío, nos pidieron analizar los datos de sus clientes, con dos objetivos claros:

1️⃣ **Entender el comportamiento de los clientes y encontrar patrones**. VER EL NOTEBOOK "Churn_EDA_model_development.ipynb"

2️⃣ **Desarrollar un modelo predictivo** que permitiera calcular la probabilidad de que un cliente abandone la compañía. VER https://equipo-c23-17-data-main.streamlit.app/

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
| `deviceprotection`                    | `object`       | especifica si un cliente ha optado por la protección del dispositivo. |
| `techsupport`                      | `object`       | Si un cliente ha optado por el soporte técnico o no. |
| `streamingtv`                | `object`            | Si un cliente tiene la opción de transmisión de TV. |
| `streamingmovies`                       | `object`        | Si un cliente tiene la opción de transmisión de películas. |
| `contract`                  | `object`       | El tipo de contrato que ha elegido un cliente. |
| `paperlessbilling`                 | `object`       | Si un cliente ha optado por la facturación sin papel. |
| `paymentmethod`           | `object`                | Especifica el método por el cual se pagan las facturas. |
| `tenure`                       | `int64`       | El tiempo durante el cual un cliente ha estado utilizando el servicio. |
| `monthlycharges`                       | `float64`               | el dinero total que el cliente pagó a la empresa. |
| `totalcharges`                 | `object`        | Identificador único de la transacción. |
