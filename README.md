# ⚡ FastAPI QR Microservice

A high-performance, asynchronous REST API that generates customizable QR codes on the fly. Built with **FastAPI** to be lightweight and blazing fast.

**Part of the "15 Days, 15 Projects" Challenge.**

## 🚀 Features

* **Instant Generation:** Generates QR codes in memory (RAM) without saving files to disk, ensuring maximum speed.
* **Customizable:** detailed control over size, fill color, and background color via query parameters.
* **Auto-Documentation:** Comes with built-in interactive API docs (Swagger UI).
* **Validation:** Automatic data validation using Python type hints.

## 🛠️ Tech Stack

* **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (Modern, high-performance web framework)
* **Server:** [Uvicorn](https://www.uvicorn.org/) (Lightning-fast ASGI server)
* **Image Processing:** `qrcode` & `Pillow`
* **Language:** Python 3.10+

## ⚙️ Installation & Run

### 1. Clone & Setup
```bash
git clone <your-repo-url>
cd qr-microservice
