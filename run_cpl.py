import os

if "darwin" == os.uname():
    os.environ["JAX_PLATFORM_NAME"] = "cpu"
    from jax import config

    config.update("jax_enable_x64", False)
import jax
from desidr2 import logl_desidr2
from pantheonplus import logl_pantheonplus
import cpl
from nested_sampling import sample_cpl

rng_key = jax.random.PRNGKey(1729)
os.makedirs("chains", exist_ok=True)


def logl(x):
    return logl_desidr2(x, cpl) + logl_pantheonplus(x, cpl)


samples = sample_cpl(logl, 500, "dp_cpl", rng_key)

print(f"anesthetic logZ = {samples.logZ():.2f} = {samples.logL_P():.2f} - {samples.D_KL():.2f}")
