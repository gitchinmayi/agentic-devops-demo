import asyncio

class GitAgent:
    async def fetch_code(self):
        print("[GitAgent] Fetching code (simulated)...")
        await asyncio.sleep(1)
        code = {
            "repo": "demo-repo",
            "commit": "abc123",
            "files": ["app.py", "Dockerfile"]
        }   
        print(f"[GitAgent] Fetched commit {code['commit']}")
        return code

