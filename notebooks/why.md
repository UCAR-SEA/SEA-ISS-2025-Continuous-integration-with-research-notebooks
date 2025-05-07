----- 

# Why reproducibility? 



## [Geoscientific Model Development (GMD) Guidelines](https://gmd.copernicus.org/articles/12/2215/2019/) 
![GMD Cover](img/gmd_cover.png)

GMD executive editors: Editorial: The publication of geoscientific model developments v1.2, {cite:t}`gmd_2019`.


**The GMD journal** in 2019 posted editorial guidelines regarding code and data policies. In the paper we can find that 
 
> _(...) it is not sufficient that the source code is provided. It is also necessary to have **access** to all of the **input data** (...) and all **model configuration files** are provided._

Next point in the same section mentions that manual processing is considered harmful

> _(...) challenge (...) occurs where model inputs or outputs have been manually processed by an author. (...) nobody, not even the author, can definitively know (...) how the results came about._

To avoid:
> _All figures and tables must be **scientifically reproducible from the scripts**._


```{attention} GMD Guidelines: 
Journals enforce reproducibility against archived releases (which is great!)
```
---
# Why notebooks?



##  _Why Jupyter is data scientists’ computational notebook of choice_
Nature 563 (toolbox): {cite:t}`perkel_2018`

<img src="img/nature.svg.webp" width=500 class="center">

If you're still asking yourself, "Why notebooks?" here is a quote from Nature's paper:
> We went from Jupyter notebooks not existing some six years ago to in essence everybody using them today.


Here, we want to address challenges with Jupyter-notebooks that are
> (...) difficult to organize code logically, break it into reusable modules and develop tests to ensure~the code is working properly

---

##  _Reactive, reproducible, collaborative: computational notebooks evolve_
Nature 593: {cite:t}`perkel_2021`
<img src=img/Nature2021.webp width=500>

Three years after the previous paper, we can find another one (with the above title). 

> A 2019 study found that just 24\% of 863,878 publicly available Jupyter notebooks on GitHub could be successfully re-executed, and only 4\% produced the same results.[^1]

[^1]: {cite:t}`pimentel_2019`

---
# Can we do even better?

```{admonition} Even better!
The reproducibility maintained with ongoing developments
```

<img src="img/signs-post-solid.svg" width=50>   In next sections you can find solutions developed in our packages.

---
