from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import Response
import qrcode
from io import BytesIO

# Initialize the App
app = FastAPI(
    title="QR Code Microservice",
    description="A high-performance API to generate QR codes on the fly.",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "QR Generator is Online! Go to /docs to test it."}

@app.get("/generate")
def generate_qr(
    url: str = Query(..., description="The URL or text to encode"),
    size: int = Query(10, ge=1, le=50, description="Box size (1-50)"),
    fill_color: str = Query("black", description="Color of the QR code"),
    back_color: str = Query("white", description="Background color")
):
    """
    Generates a QR code image from a URL.
    Returns the image directly (image/png).
    """
    try:
        # 1. Create the QR Code Object
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=size,
            border=4,
        )
        
        # 2. Add Data
        qr.add_data(url)
        qr.make(fit=True)

        # 3. Generate Image (in memory)
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        
        # 4. Save Image to a Byte Stream (RAM, not Hard Drive)
        img_byte_arr = BytesIO()
        img.save(img_byte_arr, format='PNG')
        
        # Reset pointer to the start of the stream
        img_byte_arr.seek(0)

        # 5. Return the raw bytes as an image response
        return Response(content=img_byte_arr.getvalue(), media_type="image/png")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

