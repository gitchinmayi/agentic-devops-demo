import asyncio
from agents.git_agent import GitAgent
from agents.test_agent import TestAgent
from agents.build_agent import BuildAgent
from agents.deploy_agent import DeployAgent

async def main():
        git = GitAgent()
        tester = TestAgent()
        builder = BuildAgent()
        deployer = DeployAgent()

        print("\nCoordinator: Starting pipeline...\n")

        # Step 1: Fetch code from Git
        code = await git.fetch_code()
        # Step 2: Run tests
        test_result = await tester.run_tests(code)
        if not test_result["passed"]:
            print("\nCoordinator: Tests failed ❌ — stopping pipeline.")
            return
        # Step 3: Build Docker image or artifact
        image = await builder.build_image(code)
        # Step 4: Deploy the image
        await deployer.deploy(image)

        print("\nCoordinator: Pipeline completed successfully! 🎉")

if __name__ == "__main__":
        asyncio.run(main())

