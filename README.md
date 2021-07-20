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
    ├─ 2016
    |   └─ test
    |   └─ train
    ├─ 2017
    |   └─ test
    |   └─ train
    ├─ 2018
    |   └─ test
    |   └─ train
    ├─ 2019
    |   └─ test
    |   └─ train
    └─ 2020
        └─ test
        └─ train

## Duplicate Removal Process

1. Make a copy of your ISIC dir (e.g. `ISIC (Master)`) and  rename the copy to `ISIC (A)`. If you make any mistakes, you can easilty go back to your backup dir to start again.

2. In `2019/train`, find all 2,074 files containing the `_downsampled` suffix and move them into a new folder called `downsampled` in the `ISIC (A)` dir.

3. Run the *remove_downsampled_suffix.py* script from within the `ISIC (A)` dir. This removes the `_downsampled` suffix from the downsampled files so that they can be compared by name to files in all the other ISIC train/test sets.

4. Run command *fslint-gui* in a Terminal to open FSlint.

5. Once FSlint is open, click on the *Search path* tab and remove any default dirs listed using the Remove button.

6. In FSlint, click the *Add* button and add the `ISIC (A)/downsampled` dir.

### Delete Downsampled Duplicates

7. In FSlint, select the *Name clashes* option (left panel) and ensure that the `$PATH` checkbox is unticked. Select *Same name (ignore case)* in the dropdown. For each ISIC test dir, find duplicate filenames between each test dir and the downsampled dir. Use *Select > within groups > Select all but first* to select only the downsampled files in the duplicate results.

8. In FSlint, select the 'Duplicates' option (left panel). Check for binary identical images (downsampled vs each individual test set (2016 - 2020)). Note that at this stage, binary duplicates will exist within each test set, those should be ignored at this point as we are only concerned with duplicates that exist between downsampled and each test set.

9. In FSlint, select the 'Name clashes' option (left panel) and ensure that the $PATH checkbox is unticked. Select *Same name (ignore case)' in the dropdown*. For each ISIC train dir, find duplicate filenames between each train dir and the downsampled dir. Use *Select > within groups > Select all but first* to select only the downsampled files in the duplicate results.

10. In FSlint, select 'Duplicates' option (left panel). Check for binary identical images (downsampled vs each individual train set (2016 - 2020)). Note that at this stage, duplicates will exist within each train set, those should be ignored at this point as we are only concerned with duplicates that exist between downsampled and each train set.

11. Run the 'add_downsampled_suffix.py' script from within the 'ISIC (A)' dir. This adds the '_downsampled' suffix back to the remaining downsampled filenames.

12. Move all remaining downsampled files in the `ISIC (A)/downsampled` dir back into the `ISIC (A)/2019/train` dir.

### Delete Binary Indentical 'Within-Sets' Training Images 

13. In FSlint, ensure that the 'Duplicates' option (left panel) is seleced. Add the `ISIC (A)/2016/train` dir to the Search path. Click Find. When results are returned, if you want to delete the oldest duplicate image files, click *Select > within groups > select all but newest*. If you want to delete the newest duplicate image files, click *Select > within groups > select all but oldest*. Click the Delete button to delete the selected image files.

14. In FSlint, ensure that the 'Duplicates' option (left panel) is seleced. Add the `ISIC (A)/2016/train` dir and the `ISIC (A)/2016/test` dir to the Search path. Click Find. When results are returned, if you want to delete the oldest duplicate image files, click *Select > within groups > select all but newest*. If you want to delete the newest duplicate image files, click *Select > within groups > select all but oldest*. Click the Delete button to delete the selected image files.

15. Repeat steps 13 and 14 for each of the remaining years (2017 - 2020). Complete the steps one year at a time. E.g. 2017 train, 2017 train vs test, then move on to 2018, etc.

### Delete Binary Indentical Training Images Where Duplicates Exist Within Test Sets

16. Delete all files from each train set where duplicates exist in any test sets. Use select 'all but newest' to ensure that only train images are selected.

TODO... expand descriptions for this bit, as per steps 13, 14 and 15.

* about the 'train vs test' searches - note that within-set duplicates will be included in the search results if you have not previously performed steps to delete within-set duplicates.
