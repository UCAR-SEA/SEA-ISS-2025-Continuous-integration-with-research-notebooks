# Developers' perspective

## Inversion of Control in atmospheric sciences <img src="img/cloud-solid.svg" width=50>

What makes atmospheric science unique?  It is not uncommon in atmospheric modeling for different studies to use different simulation flow control schemes or parameterizations.
We present Inversion of Control (IoC) solutions from PySDM that allow users to choose formulae and constants directly for their purposes and directly from the code without trade-offs in:
- performance,
- ability to switch between CPU and GPU backends, and
- dimensional analysis of physics-relevant routines for testing unit correctness.
    

```{admonition} Inversion of Control
A prerequisite for code reusability and effective testing in atmospheric science.
```

The simple notebook demonstrates this modularity by reproducing findings from {cite:t}bolin_1958. 
The author, Bert Bolin, was a Swedish meteorologist and the first chairman of the Intergovernmental Panel on Climate Change (IPCC), from 1988 to 1997 [Wikipedia](https://en.wikipedia.org/wiki/Bert_Bolin).

In the notebook one can find Bolin's table with relaxation timescales (Table 1.) reproduced with PySDM package.
The screenshot below shows a section of that notebook where physical system is defined: formulae are selected and constants are set.
<img src="img/Bolin_formula.png" width=500>

Thanks to the modular structure of the [`physics` folder](https://github.com/open-atmos/PySDM/tree/main/PySDM/physics), users can easily customize theirs settings and parameterizations.
New developers can easily familiarise themselves with the codebase and work on isolated components.
Additional utilities, constants and formulations of physical equations can be introduced or modified without requiring deep understanding of the entire project or its dependiecies.

```{admonition} Take-home message
Formulae and Constants chosen by User --- Modularity and Inversion of Control.

Help with on-boarding new developers 
```


## Dimensional analysis

Moreover, the modular architecture of the repository enables optional dimensional analysis, which can be activated for testing and switched off by default.
Returning to the Bolin's work, we demonstrate an example test for units correctness of a specific equation.
<img src="img/Bolin_test.png" width=500>

```{admonition} Take-home message
Modularity and Inversion of Control help with dimensional analysis!
```

## Notebooks are a source of test (edge) cases!
Creating tests for edge cases can be challenging. 
Our notebooks - designed to reproduce results from scientific literature - naturally provide tests cases!
This include:
- comparisons between current implementation and previous results;
- evaluation of different parameterizations or simulation settings from the literature.

For these purposes, we present a function from **`open-atmos-jupyter-utils`** used in Jupyter-notebooks testing. 
[![link to GitHub](https://img.shields.io/static/v1?label=open-atmos-jupyter-utils%20on&logo=github&color=87ce3e&message=GitHub)](https://github.com/open-atmos/jupyter-utils)

### **`notebook_vars()`**
- Executes an unmodified notebook code for automated testing
- Allows multiple assert statements o be evaluated via a single test run using pytest fixture.

```{admonition} Take-home message
Research notebooks are a source of test cases --- physical model, paper results, etc.
```

Additionally, by using `pytest fixture` and isolating a separate package for notebooks, i.e. [`PySDM-examples`](https://open-atmos.github.io/PySDM/PySDM_examples.html) we enable automated tests to be maintained outside the notebooks themselves.
This approach improve maintenance of both notebooks and tests.
```{admonition} Take-home message
Using pytest fixture unit tests are decoupled from the notebooks - improving test maintainability!
```

---
## DEMO - presented solutions
Preview the functionality described above in the following example notebook:
[![preview notebook](https://img.shields.io/static/v1?label=Bolin&logo=github&color=87ce3e&message=example)](https://github.com/open-atmos/PySDM/blob/main/examples/PySDM_examples/Bolin_1958/table_1.ipynb)).

<video width=320 height=240  controls>
  <source src="../_static/1_devs.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>

\
<img src="img/signs-post-solid.svg" width=50>  The next section highlights benefits from the user's perspective.

---
