# Developers' perspective

## Inversion of Control in atmospheric sciences <img src="img/cloud-solid.svg" width=50>

What is special about atmospheric science?  It is not uncommon in atmospheric modeling for papers to use different simulation flow control or different parameterization.
We present the inversion of control solutions from PySDM that enable the choice of formulae and constants from user code without trade-offs in:
- performance,
- ability to switch between CPU and GPU backends, and
- dimensional analysis of physics-relevant routines for testing unit correctness.
    

```{admonition} Inversion of Control
Prerequisite for reusability in atmospheric science and for testing
```

The simple notebook depicting usage of the code modularity is reproducing findings from {cite:t}bolin_1958. 
Bert Bolin was a Swedish meteorologist and the first chairman of the Intergovernmental Panel on Climate Change (IPCC), from 1988 to 1997 [Wikipedia](https://en.wikipedia.org/wiki/Bert_Bolin).

In the notebook one can find Bolin's table with relaxation timescales (Table 1.) reproduced with package.
On the screenshot is a part of this notebook where physical system is set: formulae are chosen and constants are defined.
<img src="img/Bolin_formula.png" width=500>

Thanks to the modular structure of the [`physics` folder](https://github.com/open-atmos/PySDM/tree/main/PySDM/physics), it is user's choice of settings and parameterisation.
New developers can easily familiarise themselves with the code structure and work only on a small part of the code base.
Additional utilities, constants or formulations of the mathematical equations governing physical processes can be introduced or modified without extended knowledge of the project structure and dependiecies.

```{admonition} Take-home message
Formulae and Constants chosen by User --- Modularity and Inversion of Control.

Help with on-boarding new developers 
```


## Dimensional analysis

Moreover, due to modularity inside the repository, there is a feasibility to engineer dimensional analysis of the code that can be switched on for testing and switched off by default
Going back to the Bolin's paper, we present exemplary test of the units correctness specific equation.
<img src="img/Bolin_test.png" width=500>

```{admonition} Take-home message
Modularity and Inversion of Control help with dimensional analysis!
```

## Notebooks are a source of test (edge) cases!
Creating tests for edge cases can be challenging. 
Our notebooks are based on scientific papers - reproducing their results - which provide tests cases!
For example, comparison between implementation and previous findings, or comparison between paremetrisation or settings in different papers.

From **`open-atmos-jupyter-utils`** we present a function used in Jupyter-notebooks testing. 
[![link to GitHub](https://img.shields.io/static/v1?label=open-atmos-jupyter-utils%20on&logo=github&color=87ce3e&message=GitHub)](https://github.com/open-atmos/jupyter-utils)

### **`notebook_vars()`**
- executes unmodified notebook code for automated testing
- run-once with multiple asserts (using pytest fixture)

```{admonition} Take-home message
Research notebooks are a source of test cases --- physical model, paper results, etc.
```

Additionally, using `pytest fixture` and separating another package just for notebooks, i.e. [`PySDM-examples`](https://open-atmos.github.io/PySDM/PySDM_examples.html) tests can be outside the notebooks. This approach improve maintenance of notebooks and tests.
```{admonition} Take-home message
Using pytest fixture unit tests are outside the notebooks!
```

---
## DEMO featuring solutions mentioned in this section (with [![preview notebook](https://img.shields.io/static/v1?label=Bolin&logo=github&color=87ce3e&message=example)](https://github.com/open-atmos/PySDM/blob/main/examples/PySDM_examples/Bolin_1958/table_1.ipynb)).

<video width=320 height=240  controls>
  <source src="../_static/1_devs.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>

\
<img src="img/signs-post-solid.svg" width=50>   Next section covers users' gains.

---
