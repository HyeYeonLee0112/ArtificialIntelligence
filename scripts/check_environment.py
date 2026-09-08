"""CPU/GPU, seed repeatability and a small matmul; no dataset download."""
import argparse
import json
import platform
import random
import sys
from pathlib import Path


def inspect_environment(require_cuda=False):
    result = {"python": platform.python_version(), "platform": platform.system()}
    random.seed(42)
    first = random.random()
    random.seed(42)
    result["python_seed_repeatable"] = first == random.random()
    try:
        import numpy as np
        import torch
        import torchvision
    except ImportError as error:
        result["error"] = str(error)
        result["hint"] = "Install requirements.txt and PyTorch; see docs/SETUP.md."
        return result, False
    result.update(numpy=np.__version__, torch=torch.__version__,
                  torchvision=torchvision.__version__, cuda_build=torch.version.cuda,
                  cuda_available=torch.cuda.is_available())
    if require_cuda and not result["cuda_available"]:
        result["error"] = "CUDA was required but is unavailable."
        return result, False
    device = "cuda" if result["cuda_available"] else "cpu"
    result["device"] = device
    if device == "cuda":
        result["gpu"] = torch.cuda.get_device_name(0)
        result["capability"] = list(torch.cuda.get_device_capability(0))
    torch.manual_seed(42)
    a = torch.rand(2, 3, device=device)
    torch.manual_seed(42)
    result["torch_seed_repeatable"] = torch.equal(a, torch.rand(2, 3, device=device))
    x = torch.tensor([[1., 2.], [3., 4.]], device=device)
    expected = torch.tensor([[7., 10.], [15., 22.]], device=device)
    result["matmul_ok"] = torch.allclose(x @ x, expected)
    result["numpy_broadcast_shape"] = list((np.zeros((2, 3)) + np.ones(3)).shape)
    if device == "cuda":
        torch.cuda.synchronize()
    return result, all(result[k] for k in
                       ("python_seed_repeatable", "torch_seed_repeatable", "matmul_ok"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--require-cuda", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result, ok = inspect_environment(args.require_cuda)
    except Exception as error:
        result, ok = {"error": str(error), "type": type(error).__name__}, False
    content = json.dumps(result, ensure_ascii=False, indent=2)
    print(content)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content + "\n", encoding="utf-8")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
