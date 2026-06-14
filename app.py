import gradio as gr


def generate_clips(url: str):
    if not url:
        return 'Paste a YouTube or Twitch URL.'

    # Pipeline to be implemented:
    # 1. Download video (yt-dlp)
    # 2. Transcribe (faster-whisper)
    # 3. Score viral moments
    # 4. Cut clips (FFmpeg)
    # 5. Add captions and export
    return f'Processing started for: {url}'


with gr.Blocks() as demo:
    gr.Markdown('# AI Viral Clipper V1')
    url = gr.Textbox(label='Video URL')
    output = gr.Textbox(label='Status')
    btn = gr.Button('Generate Clips')
    btn.click(generate_clips, inputs=url, outputs=output)


if __name__ == '__main__':
    demo.launch()
