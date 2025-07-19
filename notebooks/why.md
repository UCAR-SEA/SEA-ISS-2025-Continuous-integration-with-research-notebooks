# Why reproducibility? 

By _reproducibility_, we refer to the main principle of the scientific method: research findings must be replicable 
through independent experimentation or data analysis. The results should be consistent with those of the original study, within acceptable error margin.

In modern scientific research, software plays a central role in data processing, analysis, and experimentation,
introducing additional challenges to reproducibility.
It is no longer sufficient to merely describe the methods used in an experiment. 
Access to the source code is essential - but not sufficient on its own.

### [Geoscientific Model Development (GMD) Guidelines](https://gmd.copernicus.org/articles/12/2215/2019/) 
![GMD Cover](img/gmd_cover.png)

The  _GMD_ journal explicitly states the importance of reproducibility in its editorial guidelines.
In {cite:t}`gmd_2019`, it introduced editorial guidelines regarding code and data policies. For example:
 
> _(...) it is not sufficient that the source code is provided. It is also necessary to have **access** to all the **input data** (...) and all **model configuration files** are provided._

Additionally:

> _(...) challenge (...) occurs where model inputs or outputs have been manually processed by an author. (...) nobody, not even the author, can definitively know (...) how the results came about._

> _All figures and tables must be **scientifically reproducible from the scripts**._

Why is reproducibility essential? Because it is a core principle of the scientific method and a requirement enforced by scientific journals.

```{attention} GMD Guidelines: 
Journals enforce reproducibility against archived releases (which is great!)
```
---
# Why notebooks?
In this paper, we will present utility package and practical recommendations to support reproducible scientific research within the context of research software engineering (RSE). 
These tools are intended for use with scientific notebooks contained in code repositories. 
In this section, we explore the growing use of notebooks in research, based on statements from articles published in Nature.


###  _Why Jupyter is data scientists’ computational notebook of choice_
Nature 563 (toolbox): {cite:t}`perkel_2018`
<img src="img/nature.svg.webp" width=500 class="center">

We read:
> We went from Jupyter notebooks not existing some six years ago to in essence everybody using them today.


However, the same paper also highlights challenges:
> (...) difficult to organize code logically, break it into reusable modules and develop tests to ensure the code is working properly

---

###  _Reactive, reproducible, collaborative: computational notebooks evolve_
Nature 593: {cite:t}`perkel_2021`
<img src=img/Nature2021.webp width=500>

Three years later, they published:

> A 2019 study found that just 24\% of 863,878 publicly available Jupyter notebooks on GitHub could be successfully re-executed, and only 4\% produced the same results.[^cite1]

Due to notebooks wide presence in scientific research, it is important to address the challenges they present.

[^cite1]: {cite:t}`pimentel_2019`

---
# Can we do even better?
Journals require that results are reproducible using the code and data working at the time of publication. 
This necessitates using specific package versions to ensure consistent behavior.
Hence, we propose going further. 

```{admonition} Even better!
The reproducibility maintained with ongoing developments
```


<img src="img/signs-post-solid.svg" width=50 alt="next">   In next sections you can find solutions developed in our packages.
