---
layout: post
title: GEV Marginal Distributions and Log-Normal Conditional Distributions
date: 2018-09-10
category: analysis
author: James
comments: true
mathjax: true
thumbnail: /img/posts/2018-09-10-gev-lognormal-dist/index.jpg
---

In statistical analysis of hydroclimate data we're often interested in fitting distributions to observed variables such as rainfall and streamflow.
The General Extreme Value (GEV) distribution is commonly used because of its "fat" tails, but maybe that's not always necessary.

<!--more-->

In the following [jupyter notebook](https://jupyter.org/){:target="_blank"}, I do a simple experiment.
First, I create several time series with random period and phases, which represent the indices of large-scale climate variables (such as ENSO, the PDO, etc).
Second, I draw fake streamflow data using a conditional log-normal model:

$$
\begin{align*}
    \mu &= \mu_0 + X^T \beta \\
    \sigma &= 0.1 \mu \\
    \log Q &\sim \mathcal{N}(\mu, \sigma)
\end{align*}
$$

where $$\beta$$ are the (also randomly chosen) dependences on the large-scale climate predictors and $$X$$ is the notation for these predictors.

This is an incredibly over-simplified model and isn't meant to represent all the physics of streamflow -- just the fact that theres is variability present on many timescales (and here there's no trend!)
Interestingly, if you look at the resulting histogram of a long simulation from this model, you would think that a GEV fit was necessary to capture the "fat" tail of this model.
However, the real model doesn't have any GEV dependence -- the "fat tail" comes purely from the dependence on the climate predictors.
It's therefore worth asking ourselves whether we always need to use a GEV distribution (which comes with many problems including difficulty estimating the parameters) or whether we can instead use a simpler statistical distribution (such as the log-normal) plus the use of conditional estimation.
I won't get into the theory in this post, but it's certainly an interesting question!

Here's the analysis:

{::nomarkdown}
{% jupyter_notebook "/notebooks/gev-lognormal.ipynb" %}
{:/nomarkdown}