from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "faireval"
AUTHOR_USER_NAME = "mukulnamagiri"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = [
    "streamlit",
    "numpy",
    "gunicorn",
    "dash",
    "dash-bootstrap-components",
    "dash-core-components",
    "dash-html-components",
    "dash-renderer",
    "dash-table",
    "flask",
    "flask-compress",
    "geopandas",
    "folium",
    "plotly",
    "datasets",
]

setup(
    name=REPO_NAME,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="ai fairness exploration research",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="mukulnamagiri12@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.12",
    install_requires=LIST_OF_REQUIREMENTS
)
