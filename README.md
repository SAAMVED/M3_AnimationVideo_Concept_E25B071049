# Eigenvalues and Eigenvectors: animation source code

Built with Manim Community v0.22.1 (Python 3.13). Needs LaTeX and ffmpeg installed.

## Files
- scenes.py, scenes2.py, scenes3.py, scenes4.py: all scene classes
- pace.py: scales the pauses in each scene to fit the voice-over
- build.sh: joins each rendered clip with its narration into the final MP4

## Render
    python3 -m venv venv && source venv/bin/activate
    pip install -r requirements.txt
    for s in Scene1Hook Scene2Concept Scene3TestVector Scene3EigenLines Scene3Compress Scene5Interpret Scene6Summary; do manim -qh scenes2.py $s; done
    manim -qh scenes.py Scene3
    manim -qh scenes3.py Scene4Algebra2 Scene4Decomp2
    manim -qh scenes4.py Scene3Columns

## Build final video
    bash build.sh
(build.sh expects the narration WAV files in audio/final/, which are not included here.)
