# -*- coding: utf-8 -*-

import subprocess
import os


os.environ["nnUNet_raw"] = "/content/drive/MyDrive/HECKTOR_2026/nnUNet_raw"
os.environ["nnUNet_preprocessed"] = "/content/drive/MyDrive/HECKTOR_2026/nnUNet_preprocessed"
os.environ["nnUNet_results"] = "/content/drive/MyDrive/HECKTOR_2026/nnUNet_results"

subprocess.run([
    "nnUNetv2_train",
    "501",
    "3d_fullres",
    "0",
    "-device",
    "cuda"
], check=True)