import torch
from diffusers import StableDiffusionPipeline


def generate_image(
    prompt: str,
    model_id: str = "stabilityai/stable-diffusion-2",
    seed: int | None = None,
):

    device = (
        "mps"
        if torch.backends.mps.is_available()
        else "cuda" if torch.cuda.is_available() else "cpu"
    )

    # Load the pipeline
    if model_id is None:
        model_id = "stabilityai/stable-diffusion-2"

    pipe = StableDiffusionPipeline.from_pretrained(model_id).to(device)

    # Set up a generator for reproducibility
    if seed is not None:
        generator = torch.Generator(device=device).manual_seed(seed)
    else:
        generator = torch.Generator(device=device)

    # Run the pipeline
    pipe_output = pipe(
        prompt=prompt,  # What to generate
        # negative_prompt="Oversaturated, blurry, low quality",  # What NOT to generate
        # height=480,
        # width=640,  # Specify the image size
        guidance_scale=8,  # How strongly to follow the prompt
        num_inference_steps=35,  # How many steps to take
        generator=generator,  # Fixed random seed
    )

    # Return the generated image
    return pipe_output.images[0]


if __name__ == "__main__":
    for model in [
        "stabilityai/stable-diffusion-2",
    ]:
        image = generate_image(
            "Palette knife painting of an autumn cityscape", seed=None
        )
        image.save(model.split("/")[-1] + ".png")
