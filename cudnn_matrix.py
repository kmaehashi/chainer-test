#!/usr/bin/env python

import sys

supported_matrix = {
    'cuda70': (['cudnn4'], ''),
    'cuda75': (['cudnn5', 'cudnn51', 'cudnn6'], ''),
    'cuda80': (['cudnn5', 'cudnn51', 'cudnn6', 'cudnn7'], '-cuda8'),
    'cuda90': (['cudnn7'], '-cuda9'),
}

def translate_cudnn(cuda, cudnn):
    if cuda not in supported_matrix:
        raise RuntimeError('unsupported CUDA version')
    (supported_cudnn, suffix) = supported_matrix[cuda]
    if cudnn not in supported_cudnn:
        raise RuntimeError('unsupported CUDNN version')
    return '{}{}'.format(cudnn, suffix)

def generate_matrix():
    conds = []
    for cuda in sorted(supported_matrix.keys()):
        supported_cudnn, _ = supported_matrix[cuda]
        conds += [
            '(CUDA == "{}" && CUDNN in {})'.format(cuda, supported_cudnn)
        ]
    return ' || '.join(conds)


if sys.argv[1] == '--translate':
    print(translate_cudnn(sys.argv[2], sys.argv[3]))
elif sys.argv[1] == '--generate-matrix':
    print(generate_matrix())
else:
    raise RuntimeError()
