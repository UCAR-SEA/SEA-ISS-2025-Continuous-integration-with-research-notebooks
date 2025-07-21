# Users' perspective  <img src="img/users-solid.svg" width=50>
In PySDM and PyMPDATA packages, we enforce a consistent structure across Jupyter-notebooks. This includes three standard badges enabling execution of the notebook on different platforms: Google Colab, Binder, and GitHub.

```{admonition} Take-home message
Notebooks are self-contained and ready to run! User can open them directly in Colab, Binder, etc.
```

## Visualisations
In all example-notebooks, visuals are embedded within the file without storing separate output files in the repository (self-contained). This approach supports:
- maintainability for developers, and
- usability for researchers who want to run and modify the code themselves.


```{admonition} Take-home message
Inline visuals make research notebooks easier to maintain and adapt!

```
---

We provide utilities for visualisations via `open-atmos-jupyter-utils` package: 
### **`show_plot()`**

```{admonition} show_plot()
- renders inline SVG graphics
- adds buttons to save figures as SVG or PDF
- provides Google Drive integration on Colab
- displays correctly on GitHub
```

```{admonition} Take-home message
Vector graphics =  journal-ready plots.
```

#### Minimal example 
See this minimal usage demo in the `open-atmos-jupyter-utils` repository:

[![link to github](https://img.shields.io/static/v1?label=open%20on&logo=github&color=87ce3e&message=GitHub)](https://github.com/open-atmos/jupyter-utils/blob/main/examples/show_plot.ipynb)

This notebook reproduces the Mandelbrot set, first published by Brooks and Matelski (see [Wikipedia: Mandelbrot set](https://en.wikipedia.org/wiki/Mandelbrot_set#History))


```python
import numpy as np
from matplotlib import pyplot 
from open_atmos_jupyter_utils import show_plot

np.seterr(all='ignore')

def is_stable(c, n_iters):
    z = 0
    for _ in range(n_iters):
        z = z ** 2 + c 
    return abs(z) <= 2

data = np.array([
    re + im * 1j  
    for re in np.arange(-2,   1,   3/64)
    for im in np.arange(-1.5, 1.5, 3/64)
])
data = data[is_stable(data, n_iters=20)]

pyplot.scatter(data.real, data.imag, marker='.')
show_plot()

```

With CI automation, testing routines and version-controlled environments, we ensure notebooks stay up-to-date, satisfying reproducibility requirements.

```{admonition} Take-home message
Notebooks are powerful for tutorials, but only if kept up-to-date with ongoing development (with CI automation!)
```

#### PySDM examples with `show_plot()` usage

- [![preview notebook](https://img.shields.io/static/v1?label=render%20on&logo=github&color=87ce3e&message=GitHub)](https://github.com/open-atmos/PySDM/blob/main/examples/PySDM_examples/Lowe_et_al_2019/fig_2.ipynb) [![launch on mybinder.org](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/open-atmos/PySDM.git/main?urlpath=lab/tree/examples/PySDM_examples/Lowe_et_al_2019/fig_2.ipynb) [![launch on Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/open-atmos/PySDM/blob/main/examples/PySDM_examples/Lowe_et_al_2019/fig_2.ipynb) based on Fig. 2 from
  {cite:t}`lowe_2019`
- [![preview notebook](https://img.shields.io/static/v1?label=render%20on&logo=github&color=87ce3e&message=GitHub)](https://github.com/open-atmos/PySDM/blob/main/examples/PySDM_examples/deJong_Mackay_et_al_2023/figs_10_11_12_13.ipynb) [![launch on mybinder.org](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/open-atmos/PySDM.git/main?urlpath=lab/tree/examples/PySDM_examples/deJong_Mackay_et_al_2023/figs_10_11_12_13.ipynb) [![launch on Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/open-atmos/PySDM/blob/main/examples/PySDM_examples/deJong_Mackay_et_al_2023/figs_10_11_12_13.ipynb) based on Fig. 1 from {cite:t}`shipway_2012` --- Including BREAKUP process to demonstrate physical changes to cloud.
- [![preview notebook](https://img.shields.io/static/v1?label=render%20on&logo=github&color=87ce3e&message=GitHub)](https://github.com/open-atmos/PySDM/blob/main/examples/PySDM_examples/Miyake_et_al_1968/fig_19.ipynb) [![launch on mybinder.org](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/open-atmos/PySDM.git/main?urlpath=lab/tree/examples/PySDM_examples/Miyake_et_al_1968/fig_19.ipynb) [![launch on Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/open-atmos/PySDM/blob/main/examples/PySDM_examples/Miyake_et_al_1968/fig_19.ipynb) {cite:t}`miyake_1968`

- and more...

---
### **`show_anim()`**

```{admonition} show_anim()
- uses `matplotlib` and `imageio`
- embeds animations as base64 GIFs in `.ipynb`
- adds "Save as GIF" button and Colab support
- renders correctly on GitHub
```

#### Minimal example
 Example usage available in the `open-atmos-jupyter-utils` repository:
[![link to github](https://img.shields.io/static/v1?label=open%20on&logo=github&color=87ce3e&message=GitHub)](https://github.com/open-atmos/jupyter-utils/blob/main/examples/show_anim.ipynb)


```python
from matplotlib import pyplot
from open_atmos_jupyter_utils import show_anim 

def anim_func(frame):
    pyplot.plot([(1j**((i+frame)/100)).real for i in range(500)])    
    return pyplot.gcf()

show_anim(anim_func, frame_range=range(50))
```



---

# DEMO - Users' perspective

Here we show how a user can open a notebook in Colab and generate an animation directly within the file:

<video width=90% controls src="../_static/2_users.mp4" type="video/mp4">animation</video>

<img src="img/signs-post-solid.svg" width=50> On to the summary!
