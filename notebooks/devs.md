# Developers' perspective

## Inversion of Control as a solution to the patchwork of parameterization in atmospheric modeling <img src="img/cloud-solid.svg" width=50>

It is not uncommon in atmospheric modeling for different studies to use different parameterization or simulation flow control.
We present Inversion of Control (IoC) solutions from PySDM that allow users to select formulae and constants from the topmost level of the codebase, without trade-offs in:
- performance,
- compatibility with both CPU and GPU backends, and
- ability to perform dimensional analysis of physics-relevant routines for testing unit correctness.
    

```{admonition} Inversion of Control
A prerequisite for code reusability and effective testing.
```

The simple notebook demonstrates this modularity by reproducing findings from {cite:t}`bolin_1958`. 
The author, Bert Bolin, was a Swedish meteorologist and the first chairman of the Intergovernmental Panel on Climate Change (IPCC), from 1988 to 1997 [Wikipedia](https://en.wikipedia.org/wiki/Bert_Bolin).

In the notebook, one can find Bolin's table with the timescales of water isotopic exchange between a falling raindrop and the ambient air (Table 1.) reproduced with PySDM.
The screenshot below shows a section of that notebook where physical system is defined: formulae are selected and constants are set.

<img src="img/Bolin_formula.png" width=500>

Thanks to the modular structure of the [`physics` subpackage](https://github.com/open-atmos/PySDM/tree/main/PySDM/physics), users can easily customize parameterization and values of constants.
Such code design helps compartmentalize a new developer’s exposure, allowing them to focus on one component at a time.

```{admonition} Take-home message
Formulae and Constants chosen by User --- Modularity and Inversion of Control.

Help with on-boarding new developers 
```


## Dimensional analysis

This IoC approach not only exposes all physical constants for user configuration, but also allows us to substitute them with unit-carrying objects making dimensional consistency checks across the entire codebase automatable.
Returning to the Bolin's work, we demonstrate an example test for units correctness of a specific equation.

<img src="img/Bolin_test.png" width=500>

```{admonition} Take-home message
Modularity and Inversion of Control help with dimensional analysis!
```

## Notebooks are a source of test (edge) cases!
Creating tests for edge cases can be challenging. 
Our notebooks - designed to reproduce results from scientific literature - naturally provide tests cases!
This includes:
- regression tests ensuring new components do not alter previous results;
- evaluation of different parameterization or simulation settings against reference values from literature.

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
[![preview notebook](https://img.shields.io/static/v1?label=Bolin&logo=github&color=87ce3e&message=example)](https://github.com/open-atmos/PySDM/blob/main/examples/PySDM_examples/Bolin_1958/table_1.ipynb).

<video width=90% controls>
  <source src="../_static/1_devs.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>

\
<img src="img/signs-post-solid.svg" width=50>  The next section highlights benefits from the user's perspective.
