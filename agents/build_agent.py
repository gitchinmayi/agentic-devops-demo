import asyncio

class BuildAgent:
    async def build_image(self, code):
        print("[BuildAgent] Building Docker image (simulated)...")
        await asyncio.sleep(2)
        image = f"{code['repo']}:{code['commit']}"
        print(f"[BuildAgent] Built image {image}")
        return {"image": image}

