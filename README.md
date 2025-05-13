# Google Doc Viewer Simulator

This project simulates multiple viewers for an online document (e.g. Google Docs). It opens headless browser sessions, navigates to a specified document URL, simulates scrolling and user presence, then closes the session after a random interval.

---

## Quick Start

1. **Clone the Repository**

   ```bash
   git clone https://github.com/vishplease/anonymous-doc-viewer.git
   ```

2. **Set the Document URL**

   Open `main.py` (or this script), and change the value of `doc_url` at the top to the document you want to simulate views on:

   ```python
   doc_url = "https://docs.google.com/document/your-doc-id/edit"
   ```

3. **Build and Run the Container**

   Ensure you have [Docker](https://docs.docker.com/get-docker/) installed.

   ```bash
   docker build -t doc-viewer .
   docker run --rm doc-viewer
   ```

   **OR**, if running without Docker, just:

   ```bash
   pip install playwright
   playwright install
   python main.py
   ```

---

## Features

- Simulates multiple "viewers" with random scrolling behavior.
- Each viewer:
    - Opens a headless browser.
    - Navigates to your target document.
    - Stays on the document for a random interval (1–2 minutes).
    - Scrolls occasionally to mimic real user activity.

- Viewers are launched in random small batches over time.

---

## Configuration

- **doc_url**  
  Change this at the top of the script to your desired document!

- **Numbers of viewers, session length, and delays**  
  These can be easily tuned via:
  - `num_new_viewers` in `orchestrate_viewers()`
  - Viewer `stay_time`
  - "Wave" timing between new viewer batches

---

## Requirements

- Python 3.8+
- [Playwright](https://playwright.dev/python/)

  ```
  pip install playwright
  playwright install
  ```

- (If using Docker, these are installed automatically.)

---

## Example Console Output

```
[Viewer 1] Opened.
[Viewer 1] Closed after 110s.
[Viewer 2] Opened.
[Viewer 2] Closed after 66s.
```

---

## License

MIT
