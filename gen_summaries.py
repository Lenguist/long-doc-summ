import argparse
import backoff
import json
import openai
import os

from datetime import date

from oa_secrets import OA_KEY, OA_ORGANIZATION


openai.organization = OA_ORGANIZATION
openai.api_key = OA_KEY


@backoff.on_exception(backoff.expo, openai.error.RateLimitError)
def chatgpt(messages, model, temperature, max_tokens=650):
    response = openai.ChatCompletion.create(
        model=model, messages=messages, temperature=temperature, max_tokens=max_tokens
    )
    return response['choices'][0]['message']['content']


def get_summary(content, model, temperature, max_tokens):
    messages = [
        {'role': 'system', 'content': 'You are an expert summary-writer. Summarize the provided passage in several paragraphs using only information from the passage provided.'},
        {'role': 'user', 'content': f'Passage: {content}\n\nWrite a detailed summary of this passage in several paragraphs.\nSummary:'},
    ]

    summary = chatgpt(messages=messages, model=model, temperature=temperature, max_tokens=max_tokens)

    return summary

def get_subdirs(dir):
    return [x for x in os.listdir(dir) if not x.endswith('.json')]


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Script to generate summaries from book chapters.')
    parser.add_argument('--dir', default='booksumm-sample2')
    parser.add_argument('--outdir', default='gpt4_summaries')
    # setting comes from this https://arxiv.org/pdf/2109.10862.pdf and this https://arxiv.org/pdf/2301.13848.pdf
    parser.add_argument('--temperature', default=0.3)
    parser.add_argument('--model', default='gpt-3.5-turbo', choices=[
        'gpt-3.5-turbo',
        'gpt-4'
    ])
    parser.add_argument('--max_tokens', default=1000, type=int)

    args = parser.parse_args()

    books = get_subdirs(args.dir)

    if not os.path.exists(args.outdir):
        os.makedirs('gpt4_summaries')

    with open(os.path.join(args.outdir, "settings.txt"), 'w') as f:
        argsdict = args.__dict__
        argsdict['last-modified-date'] = str(date.today())
        json.dump(argsdict, f, indent=2)
    
    print(f'Generating summaries for {len(books)} books...')
    for book in books:
        print(f'Generating summaries for {book}:')
        chapters = get_subdirs(os.path.join(args.dir, book))
        for chapter in chapters:
            chapter_file = os.path.join(args.dir, book, chapter)
            out_chapter = os.path.join(args.outdir, book, chapter)
            if os.path.exists(out_chapter):
                print('Skipping')
                continue
            os.makedirs(out_chapter)
            with open(os.path.join(chapter_file, 'metadata.json'), 'r')  as f:
                length = json.load(f)['chapter-len']
            print(f'Chapter {chapter} - length {length}')
            with open(os.path.join(chapter_file, 'content.txt'), 'r') as f:
                content = f.read()
            summary = get_summary(content, args.model, args.temperature, args.max_tokens)
            with open(os.path.join(out_chapter, 'summary.txt'), 'w') as f:
                f.write(summary)

