:title: New Paper in Earth's Future
:author: James Doss-Gollin
:date: 2019-03-28
:category: updates
:tags: English, climate, papers
:slug: 2019-probabilistic-harvey
:summary: New paper with Viktor Rozer et. al Probabilistic models significantly reduce uncertainty in Hurricane Harvey pluvial flood loss estimates

A paper I co-authored with `Viktor Rozer <http://http://www.lse.ac.uk/GranthamInstitute/profile/viktor-rozer/>`_ (lead author), `Heidi Kreibich <https://www.gfz-potsdam.de/en/staff/heidi-kreibich/sec54/>`_, `Kai Schroter <https://www.gfz-potsdam.de/en/staff/kai-schroeter/sec44/>`_, `Meike Muller <https://system-risk.eu/node/82>`_, `Nivedita Sairam <https://www.gfz-potsdam.de/en/staff/nivedita-sairam/sec54/>`_, `Upmanu Lall <http://www.columbia.edu/~ula2>`_, and `Bruno Merz <https://www.gfz-potsdam.de/en/staff/bruno-merz/sec44/>`_  titled `Probabilistic Models Significantly Reduce Uncertainty in Hurricane Harvey Pluvial Flood Loss Estimates <https://doi.org/10.1029/2018EF001074>`_ has been published in the **open access** journal Earth's Future [@@Rozer:2019]!

In this paper we dive into the (unfortunately very relevant) challenge of estimating damages from the measurable characteristics of the floods.
Engineers traditionally use "stage-damage functions" to do this; these relate the depth of the flood to the expected damage.
Though they are straightforward to use, stage-damage functions often perform poorly in real-world situations.

Instead, we explore several statistical models for predicting flood damages using a dataset of flood damages in Houston, TX sustained during Hurricane Harvey.
The best-performing model is the "zero-inflated beta regression", which uses regression to first estimate whether damage occurred or not, and then to estimate the fraction of total damage that occurred, if any.
We found that using this model performed substantially better than commonly used models on the Hurricane Harvey dataset.

For more details, read the paper (did I mention it's open access?!)
Here's our abstract:

  Pluvial flood risk is mostly excluded in urban flood risk assessment.
  However, the risk of pluvial flooding is a growing challenge with a projected increase of extreme rainstorms compounding with an ongoing global urbanization.
  Considered as a flood type with minimal impacts when rainfall rates exceed the capacity of urban drainage systems, the aftermath of rainfall‐triggered flooding during Hurricane Harvey and other events show the urgent need to assess the risk of pluvial flooding.
  Due to the local extent and small scale variations, the quantification of pluvial flood risk requires risk assessments on high spatial resolutions.
  While flood hazard and exposure information is becoming increasingly accurate, the estimation of losses is still a poorly understood component of pluvial flood risk quantification.
  We use a new probabilistic multi‐variable modeling approach to estimate pluvial flood losses of individual buildings, explicitly accounting for the associated uncertainties.
  Except for the water depth as the common most important predictor, we identified the drivers for having loss or not and for the degree of loss to be different.
  Applying this approach to estimate and validate building structure losses during Hurricane Harvey using a property level data set, we find that the reliability and dispersion of predictive loss distributions vary widely depending on the model and aggregation level of property level loss estimates.
  Our results show that the use of multi‐variable zero‐inflated beta models reduce the 90% prediction intervals for Hurricane Harvey building structure loss estimates on average by 78% (totalling US$ 3.8 billion) compared to commonly used models.

If you have any questions please feel free to `contact me <mailto:james.doss-gollin@columbia.edu>`_ or you can `contact Viktor <mailto:https://www.gfz-potsdam.de/en/staff/bruno-merz/sec44/>`_, who is the paper's corresponding author.
Thanks for any thoughts!

.. image::  {static}/images/2019-03-28-probabilistic-harvey/abstract-key-points.png
  :height: 350px
  :align: center
  :alt: Abstract and key points of article