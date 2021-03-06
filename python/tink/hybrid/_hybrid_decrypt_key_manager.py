# Copyright 2019 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Python wrapper of the CLIF-wrapped C++ Hybrid En- and Decryption key manager."""

from __future__ import absolute_import
from __future__ import division
# Placeholder for import for type annotations
from __future__ import print_function

from typing import Text

from tink import core
from tink.cc.pybind import cc_key_manager
from tink.cc.pybind import hybrid_decrypt as cc_hybrid_decrypt
from tink.hybrid import _hybrid_decrypt


class _HybridDecryptCcToPyWrapper(_hybrid_decrypt.HybridDecrypt):
  """Transforms cliffed C++ HybridDecrypt primitive into a Python primitive."""

  def __init__(self, cc_primitive: cc_hybrid_decrypt.HybridDecrypt):
    self._hybrid_decrypt = cc_primitive

  @core.use_tink_errors
  def decrypt(self, ciphertext: bytes, context_info: bytes) -> bytes:
    return self._hybrid_decrypt.decrypt(ciphertext, context_info)


def from_cc_registry(
    type_url: Text
) -> core.PrivateKeyManager[_hybrid_decrypt.HybridDecrypt]:
  return core.PrivateKeyManagerCcToPyWrapper(
      cc_key_manager.HybridDecryptKeyManager.from_cc_registry(type_url),
      _hybrid_decrypt.HybridDecrypt, _HybridDecryptCcToPyWrapper)
