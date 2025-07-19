# **open-atmos** packages <img src=img/code-branch-solid.svg width=50>
Before going into specific descriptions of our proposed solutions, let us introduce open-source Pythonic packages that will serve as examples and show-cases. All of them are developed and maintained by `open-atmos` contributors [![link to GitHub](https://img.shields.io/static/v1?label=open-atmos%20on&logo=github&color=87ce3e&message=GitHub)](https://github.com/open-atmos).
Packages started over 5 years ago, hence, serve as good examples for discussion about maintainability.



---

## PySDM               <img src="img/pysdm_logo.svg" width=50>


**PySDM** is a package for simulating the dynamics of a population of particles undergoing diffusional and collisional growth (and breakage). The package features a **Pythonic high-performance (multithreaded CPU & CUDA GPU)** implementation of the **Super-Droplet Method (SDM) Monte-Carlo** algorithm for representing collisional growth {cite:t}`shima_2009`, hence the name. 

The animation from the landing page [PySDM Documentation](https://open-atmos.github.io/PySDM/)

<img width="600" height="300" src="https://github.com/open-atmos/PySDM/releases/download/tip/docs_intro_animation_ubuntu-24.04.gif">


[![link to GitHub](https://img.shields.io/static/v1?label=PySDM%20on&logo=github&color=87ce3e&message=GitHub)](https://github.com/open-atmos/PySDM)
[![PyPI version](https://badge.fury.io/py/PySDM.svg)](https://pypi.org/project/PySDM)

---

## PyMPDATA <img src="img/pympdata_logo.svg" width=50>
 

**PyMPDATA** is a **Numba-accelerated multithreaded Pythonic** implementation of the **MPDATA algorithm** of {cite:t}`smolarkiewicz_1984` used in geophysical fluid dynamics for solving convection-diffusion PDEs. PyMPDATA supports integration in 1D, 2D, and 3D structured meshes with optional coordinate transformations. 

More information and examples can be found in [PyMPDATA Documentation](https://open-atmos.github.io/PyMPDATA/)


[![link to github](https://img.shields.io/static/v1?label=PyMPDATA%20on&logo=github&color=87ce3e&message=GitHub)](https://github.com/open-atmos/PyMPDATA)
[![PyPI version](https://badge.fury.io/py/PyMPDATA.svg)](https://pypi.org/project/PyMPDATA)

---

## open-atmos-jupyter-utils <img src=img/Atmos-logo-vert.svg width=70>

`open-atmos-jupyter-utils` is a Python package providing Jupyter notebook utility routines for:
- presenting [Matplotlib](https://matplotlib.org) plots as either SVG vector graphics or animated GIFs, embedding them within the notebooks, and rendering correctly in [GitHub's Rich Jupyter Notebook diffs](https://github.blog/changelog/2023-03-01-feature-preview-rich-jupyter-notebook-diffs/)
- save-as buttons below each figure (triggering [Google-Drive downloads](https://colab.research.google.com/notebooks/io.ipynb#scrollTo=hauvGV4hV-Mh) on [Colab](https://colab.google/))
- execution of unmodified notebook code for automated testing (e.g., within [pytest fixtures](https://docs.pytest.org/en/stable/explanation/fixtures.html))
- pip-installation of external packages on Colab safeguarded against [alterations of Google-shipped packages](https://github.com/googlecolab/colabtools/issues/2837)
 
Can be installed via `pip`

```
pip install open-atmos-jupyter-utils
```

[![link to GitHub](https://img.shields.io/static/v1?label=open-atmos-jupyter-utils%20on&logo=github&color=87ce3e&message=GitHub)](https://github.com/open-atmos/jupyter-utils)
[![PyPI version](https://badge.fury.io/py/open-atmos-jupyter-utils.svg)](https://pypi.org/project/open-atmos-jupyter-utils)

---

## What's next?

The next part links challenges of the maintainability of research-results reproducibility with solutions developed during evolution of the packages mentioned above. We divided it into sections concerning developers' and users' gains. 

<img src="img/signs-post-solid.svg" width=50> Let's start with the developers' perspective!

