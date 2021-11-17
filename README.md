# ISIC Datasets Duplicate Removal Strategy

Instructions for the removal of duplicate image files from within individual ISIC datasets and across all ISIC datasets.

If you use any part of the duplicate removal strategy in a research project, please consider citing [our paper](https://www.sciencedirect.com/science/article/pii/S1361841521003509):

```BibTex
@article{cassidy2021isic,
 title   = {Analysis of the ISIC Image Datasets: Usage, Benchmarks and Recommendations},
 author  = {Bill Cassidy and Connah Kendrick and Andrzej Brodzicki and Joanna Jaworek-Korjakowska and Moi Hoon Yap},
 journal = {Medical Image Analysis},
 year    = {2021},
 issn    = {1361-8415},
 doi     = {https://doi.org/10.1016/j.media.2021.102305},
 url     = {https://www.sciencedirect.com/science/article/pii/S1361841521003509}
} 
```

Please read the DISCLAIMER before using any of the methods or code from this repository.

## 1. Prerequisites

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

## 2. Duplicate Removal Process

1. Make a copy of your ISIC dir (e.g. `ISIC (Master)`) and  rename the copy to `ISIC (A)`. If you make any mistakes, you can easily go back to your original Master dir to start again.

2. In `2019/train`, find all 2,074 files containing the `_downsampled` suffix and move them into a new folder called `downsampled` in the `ISIC (A)` dir.

3. Run the *remove_downsampled_suffix.py* script from within the `ISIC (A)` dir. This removes the `_downsampled` suffix from the downsampled files so that they can be compared by name to files in all the other ISIC train/test sets.

4. Run command `fslint-gui` in a Terminal to open FSlint.

5. Once FSlint has loaded, click on the *Search path* tab and remove any default dirs listed using the *Remove* button.

6. In FSlint, click the *Add* button and add the `ISIC (A)/downsampled` dir.

### 2.1 Delete Downsampled Duplicates

7. In FSlint, select the *Name clashes* option (left panel) and ensure that the `$PATH` checkbox is unticked. Select *Same name (ignore case)* in the dropdown. Click the *Add* button and add the `ISIC (A)/2016/test` dir to the *Search path*. You should now have two paths in the *Search path* window: `ISIC (A)/downsampled` and `ISIC (A)/2016/test`. Click the *Find* button. When the results are returned, click *Select > within groups > Select all but first* to select only the downsampled files in the duplicate results. When all the files you want to delete are highlighted, click the *Delete* button. Note that no test image files should be selected in the search results. If any test image files are selected, unselect them individually by holding *CTRL* and click left mouse button on the image files you want to unselect. Repeat this step for each of the remaining individual ISIC test dirs: 2017 - 2020. Ensure that you highlight the current year dir in the *Search path* window and click the *Remove* button before moving on to the next year dir.

8. In FSlint, highlight all paths shown in the *Search path* window and click the *Remove* button.

9. In FSlint, select the 'Duplicates' option (left panel). Add the following dirs to the *Search path*: `ISIC (A)/downsampled` and `ISIC (A)/2016/test`. Click the *Find* button. When the results are returned, click *Select > within groups > Select all but first* to select only the downsampled files in the duplicate results. When all the files you want to delete are highlighted, click the *Delete* button. Repeat this step for each of the remaining individual ISIC test dirs: 2017 - 2020. Ensure that you highlight the current year dir in the *Search path* window and click the *Remove* button before moving on to the next year dir. Note that at this stage, binary duplicates may exist within each test set. Ensure that only downsampled image files are selected when deleting image files. If any test image files are selected, hold *Ctrl* and click left mouse button to unselect individual image files.

10. In FSlint, highlight all paths shown in the *Search path* window and click the *Remove* button.

11. In FSlint, select the *Name clashes* option (left panel) and ensure that the `$PATH` checkbox is unticked. Select *Same name (ignore case)* in the dropdown. Click the *Add* button and add the `ISIC (A)/2016/train` dir to the *Search path*. You should now have two paths in the *Search path* window: `ISIC (A)/downsampled` and `ISIC (A)/2016/train`. Click the *Find* button. When the results are returned, click *Select > within groups > Select all but first* to select only the downsampled files in the duplicate results. When all the files you want to delete are highlighted, click the *Delete* button. Note that no train image files should be selected in the search results. If any train image files are selected, unselect them individually by holding *CTRL* and click left mouse button on the image files you want to unselect. Repeat this step for each of the remaining individual ISIC train dirs: 2017 - 2020. Ensure that you highlight the current year dir in the *Search path* window and click the *Remove* button before moving on to the next year dir.

12. In FSlint, highlight all paths shown in the *Search path* window and click the *Remove* button.

13. In FSlint, select the 'Duplicates' option (left panel). Add the following dirs to the *Search path*: `ISIC (A)/downsampled` and `ISIC (A)/2016/train`. Click the *Find* button. When the results are returned, click *Select > within groups > Select all but first* to select only the downsampled files in the duplicate results. When all the files you want to delete are highlighted, click the *Delete* button. Repeat this step for each of the remaining individual ISIC train dirs: 2017 - 2020. Ensure that you highlight the current year dir in the *Search path* window and click the *Remove* button before moving on to the next year dir. Note that at this stage, binary duplicates may exist within each train set. Ensure that only downsampled image files are selected when deleting image files. If any train image files are selected, hold *Ctrl* and click left mouse button to unselect individual image files.

14. In FSlint, highlight all paths shown in the *Search path* window and click the *Remove* button.

15. Run the 'add_downsampled_suffix.py' script from within the `ISIC (A)` dir. This adds the *_downsampled* suffix back to the remaining downsampled filenames.

16. Move all remaining downsampled files in the `ISIC (A)/downsampled` dir back into the `ISIC (A)/2019/train` dir.

### 2.2 Delete Binary Identical 'Within-Train-Sets' and 'Across-Train-Sets' Training Images

17. In FSlint, ensure that the 'Duplicates' option (left panel) is selected. Highlight all paths shown in the *Search path* window and click the *Remove* button. Add the following dirs to the *Search path*: `ISIC (A)/2016/train`, `ISIC (A)/2017/train`, `ISIC (A)/2018/train`, `ISIC (A)/2019/train`, and `ISIC (A)/2020/train`. Click the *Find* button. When results are returned, if you want to delete the oldest duplicate image files, click *Select > within groups > select all but newest*. If you want to delete the newest duplicate image files, click *Select > within groups > select all but oldest*. Click the *Delete* button to delete the selected image files.

18. In FSlint, highlight all paths shown in the *Search path* window and click the *Remove* button.

### 2.3 Delete Binary Identical Training Images That Exist 'Across-Train-and-Test-Sets'

19. In FSlint, ensure that the 'Duplicates' option (left panel) is selected. Add the `ISIC (A)/2016/train` dir and the `ISIC (A)/2016/test` dir to the Search path. Click the *Find* button. When results are returned, if you want to delete the oldest duplicate image files, click *Select > within groups > select all but newest*. If you want to delete the newest duplicate image files, click *Select > within groups > select all but oldest*. Click the *Delete* button to delete the selected image files. Ensure that you only have train image files selected in the search results. To unselect individual test images, hold *Ctrl* and click left mouse button on the image file(s) in the results window you want to exclude from deletion.

20. In FSlint, highlight all paths shown in the *Search path* window and click the *Remove* button.

21. Repeat steps 19 to 20 for each of the remaining year dirs (2017 - 2020).

### 2.4 Delete Binary Identical 'Within-Test-Sets' Test Images

22. In FSlint, ensure that the 'Duplicates' option (left panel) is selected. Highlight all paths shown in the *Search path* window and click the *Remove* button. Add the following dirs to the *Search path*: `ISIC (A)/2016/test`, `ISIC (A)/2017/test`, `ISIC (A)/2018/test`, `ISIC (A)/2019/test`, and `ISIC (A)/2020/test`. Click the *Find* button. When results are returned, if you want to delete the oldest duplicate image files, click *Select > within groups > select all but newest*. If you want to delete the newest duplicate image files, click *Select > within groups > select all but oldest*. Click the *Delete* button to delete the selected image files.

## 3. Image File Deletion Logs

The table below shows a summary of all the file lists you can download from this repository containing image file names of the images that were deleted using the above duplicate removal strategy. Note that for items 6 to 11 (Order column) the *Select > within groups > Select all but newest* option was used in FSlint to mark files for deletion.

Order | Filename                                                 | Delete Count
----- | ---------------------------------------------------------| ------------
1     | downsampled_vs_2016_test_duplicate_filename_deleted.txt  | 95
2     | downsampled_vs_2017_test_duplicate_filename_deleted.txt  | 594
3     | downsampled_vs_2016_test_binary_duplicate_deleted.txt    | 1
4     | downsampled_vs_2016_train_duplicate_filename_deleted.txt | 291
5     | downsampled_vs_2017_train_duplicate_filename_deleted.txt | 946
6     | all_train_duplicates_deleted_(all but newest).txt        | 12,038
7     | 2016_train_vs_2016_test_duplicates_deleted.txt           | 2
8     | 2017_train_vs_2016_test_duplicates_deleted.txt           | 82
9     | 2017_train_vs_2017_test_duplicates_deleted.txt           | 2
10    | 2019_train_vs_2016_test_duplicates_deleted.txt           | 258
11    | 2019_train_vs_2017_test_duplicates_deleted.txt           | 1
12    | all_test_duplicates_deleted_(all but newest).txt         | 1,592

<!--- * about the 'train vs test' searches - note that within-set duplicates will be included in the search results if you have not previously performed steps to delete within-set duplicates. --->

<!--- todo: add details of static search results that don't include any cumulative deletes --->
