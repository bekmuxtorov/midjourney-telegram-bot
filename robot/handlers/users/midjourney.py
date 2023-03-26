import os
import replicate
from .translate import indentify_lang, to_english
from environs import Env

env = Env()
env.read_env()

# Set the REPLICATE_API_TOKEN environment variable
REPLICATE_API_TOKEN = env.str("REPLICATE_API_TOKEN")
model = replicate.models.get("tstramer/midjourney-diffusion")
version = model.versions.get("436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b")


def draw_picture(admin_permission_midjourney: bool, admin_permission_lang: bool, input: str, version: str = version) -> str:
    if admin_permission_lang:
        lang = indentify_lang(input)
        if lang != 'en':
            input = to_english(input, lang)
            print(input)

    if admin_permission_midjourney:
        return version.predict(prompt=input)
    return
