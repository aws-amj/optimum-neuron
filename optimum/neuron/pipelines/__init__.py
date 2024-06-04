# coding=utf-8
# Copyright 2023 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import TYPE_CHECKING

from transformers.utils import _LazyModule


_import_structure = {
    "transformers": ["pipeline"],
    "diffusers": [
        "NeuronStableDiffusionPipelineMixin",
        "NeuronStableDiffusionImg2ImgPipelineMixin",
        "NeuronStableDiffusionInpaintPipelineMixin",
        "NeuronLatentConsistencyPipelineMixin",
        "NeuronStableDiffusionControlNetPipelineMixin",
        "NeuronStableDiffusionXLPipelineMixin",
        "NeuronStableDiffusionXLImg2ImgPipelineMixin",
        "NeuronStableDiffusionXLInpaintPipelineMixin",
        "NeuronStableDiffusionXLControlNetPipelineMixin",
    ],
}

if TYPE_CHECKING:
    from .diffusers import (
        NeuronLatentConsistencyPipelineMixin,
        NeuronStableDiffusionControlNetPipelineMixin,
        NeuronStableDiffusionImg2ImgPipelineMixin,
        NeuronStableDiffusionInpaintPipelineMixin,
        NeuronStableDiffusionPipelineMixin,
        NeuronStableDiffusionXLControlNetPipelineMixin,
        NeuronStableDiffusionXLImg2ImgPipelineMixin,
        NeuronStableDiffusionXLInpaintPipelineMixin,
        NeuronStableDiffusionXLPipelineMixin,
    )
    from .transformers import (
        pipeline,
    )
else:
    import sys

    sys.modules[__name__] = _LazyModule(
        __name__,
        globals()["__file__"],
        _import_structure,
        module_spec=__spec__,
    )
