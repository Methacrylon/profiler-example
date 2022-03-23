# Profiler example

This repo is just example code to be used with cProfile.

## Install

You need `poetry` to install this repo, you can find more info [here](https://python-poetry.org/docs/).

If you don't want to use `poetry`, you can still install dependencies manually, they are described in `pyproject.toml`.

## Run cProfile

```bash
python -m cProfile profiler_example/example.py
```

## Generate graph

You can use `flameprof` to generate flamegraph of the execution.
```bash
python -m cProfile -o profile.prof profiler_example/example.py
flameprof profile.prof > profile.svg
```