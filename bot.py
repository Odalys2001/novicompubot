import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)

# 🔐 TOKEN SEGURO PARA RENDER
TOKEN = os.getenv("TOKEN")


# ======================
# START
# ======================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    teclado = [
        ["🛒 Productos", "🔧 Servicios"],
        ["💰 Promociones", "📞 Contacto"],
        ["📍 Ubicación", "ℹ️ Nosotros"],
        ["📄 Carátula"]
    ]

    markup = ReplyKeyboardMarkup(teclado, resize_keyboard=True)

    await update.message.reply_text(
        "🖥️ BIENVENIDO A NOVICOMPU\nSeleccione una opción:",
        reply_markup=markup
    )


# ======================
# RESPUESTAS
# ======================
async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):

    texto = update.message.text.lower()
    print("Mensaje recibido:", texto)

    # 🛒 PRODUCTOS
    if "productos" in texto:

        await update.message.reply_text(
            """
🛒 CATÁLOGO NOVICOMPU

💻 1. Laptop Lenovo IdeaPad 3 - $650
💻 2. Laptop HP 15 - $720
💻 3. Laptop ASUS VivoBook - $680
🖥️ 4. PC Gamer Ryzen 5 - $850
🖥️ 5. PC Office Intel Core i3 - $550
🖨️ 6. Impresora Epson L3250 - $220
🖨️ 7. Impresora HP Smart Tank - $250
⌨️ 8. Teclado Gamer RGB - $35
🖱️ 9. Mouse Logitech - $25
"""
        )

        # 📸 IMAGEN PRODUCTO
        try:
            with open("productos/laptop_lenovo.png", "rb") as foto:
                await update.message.reply_photo(
                    photo=foto,
                    caption="💻 Laptop Lenovo IdeaPad 3 - $650"
                )
        except Exception as e:
            await update.message.reply_text("❌ No se encontró la imagen")
            print("ERROR imagen:", e)

    # 🔧 SERVICIOS
    elif "servicios" in texto:
        await update.message.reply_text(
            "🛠️ Reparación, Formateo, Redes, Instalación de software"
        )

    # 💰 PROMOCIONES
    elif "promociones" in texto:
        await update.message.reply_text(
            "🔥 Laptop Lenovo $599\n🖥️ PC Gamer $850"
        )

    # 📞 CONTACTO
    elif "contacto" in texto:
        await update.message.reply_text(
            "📱 0987654321\n📧 ventas@novicompu.com"
        )

    # 📍 UBICACIÓN
    elif "ubicación" in texto:
        await update.message.reply_text(
            "📍Babahoyo - Los Ríos - Ecuador"
        )

    # ℹ️ NOSOTROS
    elif "nosotros" in texto:
        await update.message.reply_text(
            "NOVICOMPU: venta de equipos y soporte técnico"
        )

    # 📄 CARÁTULA
    elif "carátula" in texto:

        try:
            with open("caratula.jpg", "rb") as foto:
                await update.message.reply_photo(
                    photo=foto,
                    caption="Carátula del proyecto NOVICOMPU"
                )
        except Exception as e:
            await update.message.reply_text("❌ No se encontró caratula.jpg")
            print("ERROR caratula:", e)

    else:
        await update.message.reply_text(f"Recibí: {texto}")


# ======================
# MAIN
# ======================
def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

    print("✅ Bot iniciado correctamente...")
    app.run_polling()


if __name__ == "__main__":
    main()
