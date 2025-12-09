import asyncio
import sys
import os

class TestAgent:
    async def run_tests(self, code):
        print("[TestAgent] Running real tests...")

        # Find path to demo_app/test_calculator.py
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        test_file = os.path.join(base_dir, "demo_app", "test_calculator.py")

        # Run tests asynchronously
        process = await asyncio.create_subprocess_exec(
            sys.executable,
            test_file,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        stdout, stderr = await process.communicate()

        if process.returncode == 0:
            print("[TestAgent] Tests passed ✅")
            return {"passed": True}
        else:
            print("[TestAgent] Tests failed ❌")
            print("STDOUT:\n", stdout.decode())
            print("STDERR:\n", stderr.decode())
            return {"passed": False}
