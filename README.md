# Eigenvalues and Eigenvectors: Animation Video

**Module 3 submission: Animation Video (Concept)**

| | |
|---|---|
| **Student Name** | `<YOUR FULL NAME>` |
| **Student ID** | E25B071049 |
| **Concept** | Eigenvalues and Eigenvectors |
| **Tool** | [Manim Community](https://www.manim.community/) v0.22.1 (Python 3.13) |

## Watch the video

[Watch / download E25B071049_Video.mp4](https://github.com/SAAMVED/M3_AnimationVideo_Concept_E25B071049/raw/main/E25B071049_Video.mp4)

or

https://drive.google.com/file/d/1rmbZbQFVnbZdClbEX9z0s_fOnzpNRjnr/view?usp=sharing

GitHub can't preview files this large in the browser (the video is 28.1 MB), so use the link above or the download button on the file page. Format: 1080p, 16:9, MP4, with an opening frame (title, concept, name and ID) and a closing frame (summary and credits).

## About the video

This video explains what eigenvalues and eigenvectors are and why they matter. It walks through the idea visually: how a matrix transforms space, which special directions stay on their own line, how the scaling along those directions gives the eigenvalues, and how this lets us break a transformation down into simple stretches.

## Repository structure

```
.
├── README.md                    <- this file
├── E25B071049_Video.mp4         <- final video
└── E25B071049_Code/             <- complete animation source code
    ├── README.md                <- detailed render instructions
    ├── requirements.txt         <- Python dependencies (manim==0.22.1)
    ├── scenes.py                <- scene classes
    ├── scenes2.py               <- scene classes
    ├── scenes3.py               <- scene classes
    ├── scenes4.py               <- scene classes
    ├── pace.py                  <- scales pauses in each scene to fit the voice-over
    └── build.sh                 <- joins each rendered clip with its narration
```

## Scenes

| Scene | File |
|---|---|
| Scene1Hook | scenes2.py |
| Scene2Concept | scenes2.py |
| Scene3 | scenes.py |
| Scene3TestVector | scenes2.py |
| Scene3EigenLines | scenes2.py |
| Scene3Compress | scenes2.py |
| Scene3Columns | scenes4.py |
| Scene4Algebra2 | scenes3.py |
| Scene4Decomp2 | scenes3.py |
| Scene5Interpret | scenes2.py |
| Scene6Summary | scenes2.py |

## Reproduce the animation

**Requirements:** Python 3.13, [LaTeX](https://www.latex-project.org/get/), and [ffmpeg](https://ffmpeg.org/) installed on your system.

```bash
cd E25B071049_Code
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Render every scene at 1080p
for s in Scene1Hook Scene2Concept Scene3TestVector Scene3EigenLines Scene3Compress Scene5Interpret Scene6Summary; do manim -qh scenes2.py $s; done
manim -qh scenes.py Scene3
manim -qh scenes3.py Scene4Algebra2 Scene4Decomp2
manim -qh scenes4.py Scene3Columns
```

To assemble the final video:

```bash
bash build.sh
```

`build.sh` expects the narration WAV files in `audio/final/`. These are not included in the repository, so the final build can't be reproduced without them. The individual scene renders above work on their own.

## Credits

- Animation: [Manim Community Edition](https://www.manim.community/)
- Created by `<YOUR FULL NAME>` (E25B071049)
