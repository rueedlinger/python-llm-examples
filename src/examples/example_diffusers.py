import torch
from diffusers import StableDiffusion3Pipeline


# Set device
device = "mps" if torch.backends.mps.is_available() else "cuda" if torch.cuda.is_available() else "cpu"

# Load the pipeline
model_id = "stabilityai/stable-diffusion-3-medium-diffusers"
#model_id = "stabilityai/stable-diffusion-3.5-large"

pipe = StableDiffusion3Pipeline.from_pretrained(model_id).to(device)


# Set up a generator for reproducibility
generator = torch.Generator(device=device).manual_seed(42)

# Run the pipeline, showing some of the available arguments
pipe_output = pipe(
    #prompt="Palette knife painting of an autumn cityscape",  # What to generate
    #negative_prompt="Oversaturated, blurry, low quality",  # What NOT to generate
    prompt="Reealstic portrait of swiss mountain farmer",
    #height=480,
    #width=640,  # Specify the image size
    guidance_scale=8,  # How strongly to follow the prompt
    num_inference_steps=35,  # How many steps to take
    generator=generator,  # Fixed random seed
)

# View the resulting image
image = pipe_output.images[0]

# Save image to disk
image.save("test.png")
