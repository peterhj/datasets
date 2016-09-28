#!/usr/bin/env python3

import numpy as np
import scipy.io

def preproc_mat_to_bin(mat_path, bin_path):
  mat = scipy.io.loadmat(mat_path)
  with open(bin_path, "wb") as bin_file:
    n = mat["X"].shape[3]
    assert n == mat["y"].shape[0]
    for idx in range(n):
      image_bytes = mat["X"][:,:,:,idx].tobytes()
      image_label = mat["y"][idx,0]
      if image_label == 10:
        image_label = np.uint8(0)
      image_label = np.array([image_label]).tobytes()
      assert 1 == len(image_label)
      assert 3072 == len(image_bytes)
      bin_file.write(image_label)
      bin_file.write(image_bytes)

def main():
  preproc_mat_to_bin("svhn/train_32x32.mat", "svhn/train.bin")
  preproc_mat_to_bin("svhn/test_32x32.mat", "svhn/test.bin")

if __name__ == "__main__":
  main()
