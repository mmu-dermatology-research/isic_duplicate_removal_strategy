# ISIC Duplicate Removal Strategy

Instructions for the removal of duplicate image files from within individual ISIC datasets and across all ISIC datasets.

If you use any part of the duplicate removal strategy in a research project, please consider citing [our paper](https://www.abcde.com):

```BibTex
@article{cassidy2021isic,
 author    = {Cassidy, Bill and Kendrick, Connah and Brodzickib, Andrzej and Jaworek-Korjakowskab, Joanna and Yap, Moi Hoon},
 title     = {Analysis of the ISIC Image Datasets: Usage, Benchmarks and Recommendations},
 journal   = {Medical Image Analysis},
 volume    = {?},
 pages     = {?--?},
 year      = {2021},
 publisher = {Elsevier}
} 
```

Please read the DISCLAIMER before using any of this code.

## Prequisites

Download FSlint from here: http://www.pixelbeat.org/fslint/

Note that when using the Save function within FSlint to save file lists, it will save the files you have highlighted.

The following steps assume that you have downloaded and organised your ISIC datasets into the following directory structure:

ISIC
 > 2016
  > test
  > train
 > 2017
  > test
  > train
 > 2018
  > test
  > train
 > 2019
  > test
  > train
 > 2020
  > test
  > train

## Duplicate Removal Steps

1. Make a copy of your ISIC dir (e.g. 'ISIC (Master)') and  rename the copy to 'ISIC (A)'. If you make any mistakes, you can easilty go back to your backup dir to start again.

2. In 2019 > train, find all 2,074 files containing the "_downsampled" suffix and move them into a new folder called "downsampled" in the 'ISIC (A)' dir.

3. Run the 'remove_downsampled_suffix.py' script from within the 'ISIC (A)' dir. This removes the "_downsampled" suffix from the downsampled files so that they can be compared by name to files in all the other ISIC train/test sets.
