from manim import Scene

# Pause multipliers, set from the recorded audio lengths
SCALES = {
    "Scene1Hook": 2.0,
    "Scene2Concept": 1.8,
    "Scene3": 2.2,
    "Scene3Columns": 1.0,
    "Scene3TestVector": 2.0,
    "Scene3EigenLines": 3.0,
    "Scene3Compress": 1.5,
    "Scene4Algebra2": 1.0,
    "Scene4Decomp2": 1.8,
    "Scene5Interpret": 1.2,
    "Scene6Summary": 1.55,
}

_orig_wait = Scene.wait


def _scaled_wait(self, duration=1.0, *args, **kwargs):
    return _orig_wait(self, duration * SCALES.get(type(self).__name__, 1.0),
                      *args, **kwargs)


Scene.wait = _scaled_wait
