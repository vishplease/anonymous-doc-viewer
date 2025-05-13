import asyncio
import random
import time
from playwright.async_api import async_playwright

doc_url = "https://docs.google.com/document/d/17D6CApuNyckqip6Y_ORv-IC1Eg1pmppMUlOGq6-wRGg/edit"

async def simulate_viewer(viewer_id, stay_time):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        print(f"[Viewer {viewer_id}] Opened.")

        await page.goto(doc_url)
        await asyncio.sleep(10)  # load doc

        start = time.time()
        while time.time() - start < stay_time:
            await page.mouse.wheel(0, 100)
            await asyncio.sleep(random.randint(5, 15))

        await browser.close()
        print(f"[Viewer {viewer_id}] Closed after {stay_time}s.")

async def orchestrate_viewers():
    viewer_id = 0
    while True:
        num_new_viewers = random.randint(1, 2)  
        viewer_tasks = []

        for _ in range(num_new_viewers):
            viewer_id += 1
            stay_time = random.randint(60, 120)  
            delay = random.randint(0, 20)
            viewer_tasks.append(run_with_delay(viewer_id, stay_time, delay))

        for task in viewer_tasks:
            asyncio.create_task(task)

        await asyncio.sleep(random.randint(45, 60))  

async def run_with_delay(viewer_id, stay_time, delay):
    await asyncio.sleep(delay)
    await simulate_viewer(viewer_id, stay_time)

if __name__ == "__main__":
    asyncio.run(orchestrate_viewers())
