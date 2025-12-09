import asyncio

class DeployAgent:
    async def deploy(self, image):
        print("[DeployAgent] Deploying image (simulated)...")
        await asyncio.sleep(1)
        print(f"[DeployAgent] Deployed {image['image']} to staging cluster")
        return {"status": "success"}

