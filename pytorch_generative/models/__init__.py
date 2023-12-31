"""Models available in pytorch-generative."""

from ants.libs.pg.pytorch_generative.models.autoregressive.fvbn import FullyVisibleBeliefNetwork
from ants.libs.pg.pytorch_generative.models.autoregressive.gated_pixel_cnn import GatedPixelCNN
from ants.libs.pg.pytorch_generative.models.autoregressive.image_gpt import ImageGPT
from ants.libs.pg.pytorch_generative.models.autoregressive.made import MADE
from ants.libs.pg.pytorch_generative.models.autoregressive.nade import NADE
from ants.libs.pg.pytorch_generative.models.autoregressive.pixel_cnn import PixelCNN
from ants.libs.pg.pytorch_generative.models.autoregressive.pixel_snail import PixelSNAIL
from ants.libs.pg.pytorch_generative.models.flow.nice import NICE
from ants.libs.pg.pytorch_generative.models.kde import (
    GaussianKernel,
    KernelDensityEstimator,
    ParzenWindowKernel,
)
from ants.libs.pg.pytorch_generative.models.mixture_models import (
    BernoulliMixtureModel,
    GaussianMixtureModel,
)
from ants.libs.pg.pytorch_generative.models.vae.beta_vae import BetaVAE
from ants.libs.pg.pytorch_generative.models.vae.vae import VAE
from ants.libs.pg.pytorch_generative.models.vae.vd_vae import VeryDeepVAE
from ants.libs.pg.pytorch_generative.models.vae.vq_vae import VectorQuantizedVAE
from ants.libs.pg.pytorch_generative.models.vae.vq_vae_2 import VectorQuantizedVAE2
