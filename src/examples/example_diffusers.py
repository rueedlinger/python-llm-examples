from diffusers import DiffusionPipeline
import torch

#generator = torch.Generator("cpu").manual_seed(0)

# Use CPU instead of CUDA
model_id = "stable-diffusion-v1-5/stable-diffusion-v1-5"
pipeline = DiffusionPipeline.from_pretrained(model_id, use_safetensors=True)
#pipeline = DiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, use_safetensors=True)

#pipeline.to("cuda")
pipeline.to("cpu")
#pipeline.to("mps")


image = pipeline("bear fishing in the mountains", guidance_scale=7.5, num_inference_steps=80, height=512, width=768).images[0]

# Save image to disk
image.save("test.png")