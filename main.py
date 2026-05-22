# Copyright 2026 bananakitssu
# Licensed under the Apache License, Version 2.0

from pathlib import Path
import sys

current_dir = Path(__file__).resolve().parent
target_dir = current_dir / "libraries" / "Python"
sys.path.append(str(target_dir))
import Object

def run():
    print("BananaPhysics BETA") # basically do nothing until some required BananaPhysics modules are finished.
