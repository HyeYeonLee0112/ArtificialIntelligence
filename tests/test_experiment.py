import json
import tempfile
import unittest
from pathlib import Path
from src.experiment import save_metrics


class ExperimentRecordTests(unittest.TestCase):
    def test_round_trip(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "nested" / "metrics.json"
            result = save_metrics(path, question="Does h change search cost?", seed=42,
                                  device="cpu", baseline={"h": 1, "grid": "A"},
                                  changed={"h": 1.5, "grid": "A"}, metrics={"nodes": 8})
            self.assertEqual(json.loads(path.read_text(encoding="utf-8")), result)
            self.assertEqual(result["changed_variable"], "h")

    def test_rejects_uncontrolled_or_missing_measurements(self):
        cases = [
            ({"h": 1, "grid": "A"}, {"nodes": 8}),
            ({"h": 2, "grid": "B"}, {"nodes": 8}),
            ({"h": 2, "grid": "A"}, {}),
            ({"h": 2, "grid": "A"}, {"nodes": float("nan")}),
        ]
        with tempfile.TemporaryDirectory() as folder:
            for changed, metrics in cases:
                with self.subTest(changed=changed, metrics=metrics):
                    path = Path(folder) / "rejected.json"
                    with self.assertRaises(ValueError):
                        save_metrics(path, question="test", seed=42, device="cpu",
                                     baseline={"h": 1, "grid": "A"},
                                     changed=changed, metrics=metrics)
                    self.assertFalse(path.exists())


if __name__ == "__main__":
    unittest.main()
