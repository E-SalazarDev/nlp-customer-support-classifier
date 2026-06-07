# AG News Text Classifier

Proyecto de maestría en Procesamiento de Lenguaje Natural para la clasificación automática de noticias mediante técnicas de preprocesamiento textual, vectorización TF-IDF y Regresión Logística utilizando el dataset AG News.

## Objetivo

Construir un modelo de clasificación de texto capaz de identificar automáticamente la categoría de una noticia a partir de su título y descripción.

Categorías utilizadas:

* World
* Sports
* Business
* Sci/Tech

## Dataset

Se utiliza el dataset AG News Classification Dataset, compuesto por noticias clasificadas en cuatro categorías.
Los archivos utilizados son:

```text
data/raw/ag_news_train.csv
data/raw/ag_news_test.csv
```

El dataset contiene 127,600 registros en total y presenta una distribución balanceada de clases.

## Metodología

El proyecto sigue el flujo completo de una solución NLP:

1. Carga y exploración del corpus.
2. Análisis de valores nulos, duplicados y distribución de clases.
3. Construcción de la variable textual mediante Title + Description.
4. Normalización del texto.
5. Tokenización, eliminación de stopwords y lematización con spaCy.
6. Vectorización mediante TF-IDF.
7. Entrenamiento con Regresión Logística.
8. Evaluación con accuracy, precision, recall, F1-score y matriz de confusión.

## Resultados principales

El modelo obtuvo los siguientes resultados sobre el conjunto de prueba:

```text
Accuracy: 0.9088
Precision weighted: 0.9086
Recall weighted: 0.9088
F1-score weighted: 0.9086
```

La categoría Sports presentó el mejor desempeño, mientras que Business y Sci/Tech mostraron mayor posibilidad de confusión debido al solapamiento de vocabulario relacionado con empresas, tecnología y mercado.

## Estructura del proyecto

```text
data/
  raw/
    ag_news_train.csv
    ag_news_test.csv
  processed/

notebooks/
  01_analisis_exploratorio.ipynb
  02_modelado_y_evaluacion.ipynb

outputs/
  figures/
  reports/

models/

src/
  nlp/

tests/

.github/
  workflows/
```

## Instalación

Crear entorno virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

Instalar dependencias:

```powershell
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## Ejecución

Ejecutar los notebooks en este orden:

```text
notebooks/01_analisis_exploratorio.ipynb
notebooks/02_modelado_y_evaluacion.ipynb
```

El primer notebook genera el dataset procesado y las gráficas de análisis.
El segundo notebook entrena el modelo, calcula métricas, genera la matriz de confusión y guarda los artefactos del modelo.

## Artefactos generados

```text
outputs/figures/distribucion_clases_ag_news.png
outputs/figures/reduccion_texto_ag_news.png
outputs/figures/confusion_matrix_ag_news.png
outputs/reports/metrics_ag_news.json
outputs/reports/classification_report_ag_news.csv
models/ag_news_tfidf_logistic_regression_model.pkl
```

## Pruebas

Ejecutar:

```powershell
pytest
```

## Consideraciones

El archivo procesado no se versiona en GitHub porque puede superar los límites de tamaño permitidos. Se genera automáticamente al ejecutar el notebook de análisis exploratorio.
