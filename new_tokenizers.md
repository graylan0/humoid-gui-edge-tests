

Different tokenizer ideas.

# Idea 1 

To enhance your stable diffusion prompts for a video system and incorporate a unique highlighting format with tokenization, you can use a structured approach like this:

1. **Define Tokenization Format**: 
   - `[bold]`: For key elements that should be strongly emphasized.
   - `[weak]`: For elements that should be present but not dominant.
   - `[light]`: For subtle or background elements.

2. **Apply Tokenization to Your Prompt**:
   - Original Prompt: "A beautiful picture of a treehouse and a union of elves."
   - Tokenized Prompt: `[bold](A beautiful picture of a treehouse) [weak](and a union of elves).`

3. **Integrate with Your Existing Prompts**:
   - For each of your existing prompts, identify the key elements (bold), secondary elements (weak), and background or subtle details (light). 

Here's how you can apply this to one of your existing prompts:

- **Original**: "A mystical portal in a serene forest, symbolizing the gateway to multiversal peace, overseen by the TAODAO. --neg nsfw, nude"
- **Tokenized**: `[bold](A mystical portal) [weak](in a serene forest), [light](symbolizing the gateway to multiversal peace), [weak](overseen by the TAODAO). --neg nsfw, nude`

And for the new prompt about the treehouse and elves:

- **Tokenized New Prompt**: `[bold](A majestic treehouse nestled in an ancient, enchanted forest) [weak](surrounded by a diverse gathering of elves), [light](symbolizing unity and peace), [weak](under the guiding principles of the TAODAO). --neg nsfw, nude`

This approach helps to guide the model's focus, ensuring that the most important elements are captured vividly, while still maintaining the overall balance and theme of the scene. Remember, the effectiveness of this tokenization depends on how well the model has been trained to interpret these markers.
