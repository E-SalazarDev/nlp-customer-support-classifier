from pathlib import Path


def test_raw_data_files_exist():
    assert Path("data/raw/ag_news_train.csv").exists()
    assert Path("data/raw/ag_news_test.csv").exists()


def test_notebooks_exist():
    assert Path("notebooks/01_analisis_exploratorio.ipynb").exists()
    assert Path("notebooks/02_modelado_y_evaluacion.ipynb").exists()


def test_output_figures_exist():
    assert Path("outputs/figures/distribucion_clases_ag_news.png").exists()
    assert Path("outputs/figures/reduccion_texto_ag_news.png").exists()
    assert Path("outputs/figures/confusion_matrix_ag_news.png").exists()