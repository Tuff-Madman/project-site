"""
Product Description Generator using Transformer Models

This script generates creative product descriptions using the Hugging Face transformers library.
"""

import argparse
from transformers import pipeline, set_seed
import random

def setup_generator(model_name="gpt2"):
    """Initialize the text generation pipeline with the specified model."""
    try:
        generator = pipeline('text-generation', model=model_name)
        return generator
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

def generate_description(generator, product_name, keywords=None, max_length=150, num_variations=1):
    """Generate product descriptions based on product name and optional keywords."""
    if not generator:
        return ["Failed to initialize text generator."]
    
    # Set a random seed for variety
    set_seed(random.randint(1, 10000))
    
    # Create prompt based on inputs
    prompt = f"Product: {product_name}\nDescription:"
    if keywords:
        prompt = f"Product: {product_name}\nKeywords: {', '.join(keywords)}\nDescription:"
    
    # Generate descriptions
    descriptions = []
    for _ in range(num_variations):
        try:
            result = generator(prompt, max_length=max_length, num_return_sequences=1)
            # Clean up the generated text
            description = result[0]['generated_text'].replace(prompt, "").strip()
            descriptions.append(description)
        except Exception as e:
            descriptions.append(f"Error generating description: {e}")
    
    return descriptions

def main():
    parser = argparse.ArgumentParser(description='Generate product descriptions using transformer models')
    parser.add_argument('--product', required=True, help='Name of the product')
    parser.add_argument('--keywords', nargs='+', help='Keywords related to the product')
    parser.add_argument('--model', default='gpt2', help='Model to use for generation (default: gpt2)')
    parser.add_argument('--max_length', type=int, default=150, help='Maximum length of generated description')
    parser.add_argument('--variations', type=int, default=3, help='Number of descriptions to generate')
    
    args = parser.parse_args()
    
    print(f"Initializing generator with model: {args.model}")
    generator = setup_generator(args.model)
    
    print(f"Generating {args.variations} descriptions for: {args.product}")
    descriptions = generate_description(
        generator, 
        args.product, 
        args.keywords, 
        args.max_length, 
        args.variations
    )
    
    print("\n=== Generated Product Descriptions ===\n")
    for i, desc in enumerate(descriptions, 1):
        print(f"Description #{i}:\n{desc}\n")

if __name__ == "__main__":
    main()