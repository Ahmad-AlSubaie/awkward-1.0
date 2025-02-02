# BSD 3-Clause License; see https://github.com/scikit-hep/awkward-1.0/blob/main/LICENSE

import pytest  # noqa: F401
import numpy as np  # noqa: F401
import cupy as cp  # noqa: F401
import awkward as ak  # noqa: F401


def test_from_cupy():
    cupy_array_1d = cp.arange(10)
    cupy_array_2d = cp.array([[1.1, 2.2], [3.3, 4.4], [5.5, 6.6], [7.7, 8.8]])

    ak_cupy_array_1d = ak._v2.from_cupy(cupy_array_1d)
    ak_cupy_array_2d = ak._v2.from_cupy(cupy_array_2d)

    for i in range(10):
        assert ak_cupy_array_1d[i] == cupy_array_1d[i]

    for i in range(4):
        for j in range(2):
            assert ak_cupy_array_2d[i][j] == cupy_array_2d[i][j]


def test_from_cupy_tolist():
    cupy_array_1d = cp.array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

    ak_cupy_array_1d = ak._v2.from_cupy(cupy_array_1d)

    assert ak._v2.to_list(ak_cupy_array_1d.layout) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


def test_NumpyArray_constructor():
    assert ak._v2.backend(ak._v2.contents.NumpyArray(np.array([1, 2, 3]))) == "cpu"
    assert ak._v2.backend(ak._v2.contents.NumpyArray(cp.array([1, 2, 3]))) == "cuda"


@pytest.mark.skip(
    reason="Can't test this right now because of unimplemented CUDA Kernels (awkward_ListOffsetArray_compact_offsets"
)
def test_add():
    one = ak._v2.Array([[1.1, 2.2, 3.3], [], [4.4, 5.5]], backend="cuda")
    two = ak._v2.Array([100, 200, 300], backend="cuda")
    assert ak._v2.backend(one) == "cuda"
    assert ak._v2.backend(two) == "cuda"
    three = one + two
    assert ak._v2.to_list(three) == [[101.1, 102.2, 103.3], [], [304.4, 305.5]]
    assert ak._v2.backend(three) == "cuda"


def test_add_2():
    one = ak._v2.Array([[1.1, 2.2, 3.3], [], [4.4, 5.5]], backend="cuda")
    two = 100
    assert ak._v2.backend(one) == "cuda"
    three = one + two
    assert ak._v2.to_list(three) == [[101.1, 102.2, 103.3], [], [104.4, 105.5]]
    assert ak._v2.backend(three) == "cuda"
