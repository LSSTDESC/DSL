# DSL: Differentiable Survey Library
Automatically Differentiable Probabilistic Survey Simulation Library.

## Broad Description and Initial Ideas for Scope

- Similar to the CCL in that is will generate cosmological observables, except at the field level instead of 2pt functions. 
- It won't implement complex things like n-body sims, but instead rely on swappable external modules like pmwd or jaxpm
- Will rely on `numpyro` for defining the probabilistic model.
- Will rely on `Equinox` to build a nice compartementalized API.
