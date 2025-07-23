# A subjective and objective video quality dataset for neural and traditional video codecs
This repository contains all the data related to the paper:
_"Evaluating Video Quality Metrics for Neural and Traditional Codecs using 4K/UHD-1 Videos"_

## Dataset

The subjective and metric results are organized in the following way:

- The `/metrics` directory contains all raw outputs from the evaluated quality metrics, stored as `.json` files.
- The file `subjective.csv` holds the subjective scores collected from the user study.
- An aggregated version of all results is available in `results.json` for easier access and analysis.

The corresponding video files can be downloaded using the link [AVT-VQDB-UHD-1-NVC](https://avtshare01.rz.tu-ilmenau.de/avt-vqdb-uhd-1-nvc/).
The videos are provided as HEVC lossless transcodes for the encoded and source video files.
To reproduce the results from the paper the videos need to be upscaled to 3840x2160 using `ffmpeg` with a lanczos filter and a lossless codec (eg. ffvhuff or lossless HEVC). 
Make sure ffmpeg is installed on your system.

```bash
ffmpeg -i INPUT.mkv -c:v ffvhuff -vf "scale=3840x2160:param0=5" -sws_flags lanczos+accurate_rnd+bitexact OUTPUT.mkv
ffmpeg -i INPUT.mkv -c:v libx265 -x265-params lossless=1 -vf "scale=3840x2160:param0=5" -sws_flags lanczos+accurate_rnd+bitexact OUTPUT.mkv
```

The included helper script `prepare_videos.py` can also be used to upscale all videos at once.

```bash
python prepare_videos.py --input_dir decoded  -output_dir pvs
```
To save space (at the cost of longer encoding times), use the --codec h265 option:

```bash
python prepare_videos.py --input_dir decoded  -output_dir pvs --codec h265
```


## Citation
Please cite the following paper if you use any part of the data or code provided in this repository.

```bibtex
@article{herb_evaluating_2025,
    title={Evaluating Video Quality Metrics for Neural and Traditional Codecs using 4K/UHD-1 Videos},
    author={Herb, Benjamin and Ramachandra Rao, Rakesh Rao and Göring, Steve and Raake, Alexander},
    publisher={to appear},
    year={2025},
    journal={to appear}
}
```
