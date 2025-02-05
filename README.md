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
| `id`                        | `INT`                | Identificador único de la transacción. |
| `trans_date_trans_time`     | `DATETIME`           | Fecha y hora en la que ocurrió la transacción. |
| `cc_num`                    | `BIGINT`             | Número de la tarjeta de crédito utilizada en la transacción. |
| `merchant`                  | `VARCHAR(255)`       | Nombre del comerciante donde se realizó la transacción. |
| `category`                  | `VARCHAR(50)`        | Categoría del comercio donde se realizó la transacción. |
| `trans_amount`              | `DECIMAL(10,2)`      | Monto de la transacción en dólares. |
| `first_name`                | `VARCHAR(50)`        | Nombre del titular de la tarjeta. |
| `last_name`                 | `VARCHAR(50)`        | Apellido del titular de la tarjeta. |
| `gender`                    | `CHAR(1)`            | Género del titular de la tarjeta (`M` = Masculino, `F` = Femenino). |
| `street`                    | `VARCHAR(255)`       | Dirección del titular de la tarjeta. |
| `city`                      | `VARCHAR(100)`       | Ciudad de residencia del titular de la tarjeta. |
| `state_code`                | `CHAR(2)`            | Código del estado en el que reside el titular de la tarjeta. |
| `zip`                       | `VARCHAR(10)`        | Código postal del titular de la tarjeta. |
| `latitude`                  | `DECIMAL(9,6)`       | Latitud de la ubicación de residencia del titular. |
| `longitude`                 | `DECIMAL(9,6)`       | Longitud de la ubicación de residencia del titular. |
| `city_population`           | `INT`                | Población de la ciudad donde reside el titular de la tarjeta. |
| `job`                       | `VARCHAR(100)`       | Profesión del titular de la tarjeta. |
| `dob`                       | `DATE`               | Fecha de nacimiento del titular de la tarjeta. |
| `trans_num`                 | `VARCHAR(50)`        | Identificador único de la transacción. |
| `unix_time`                 | `BIGINT`             | Timestamp de la transacción en formato UNIX. |
| `merch_lat`                 | `DECIMAL(9,6)`       | Latitud de la ubicación del comerciante. |
| `merch_long`                | `DECIMAL(9,6)`       | Longitud de la ubicación del comerciante. |
| `is_fraud`                  | `BOOLEAN`            | Indica si la transacción es fraudulenta (`true` = fraude, `false` = no fraude). |
