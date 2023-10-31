import tkinter as tk
from textblob import TextBlob
from newspaper import Article

def summarize():
    # Summarization
    url = utext.get('1.0', "end").strip()

    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    date.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)
    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)
    date.delete('1.0', 'end')
    date.insert('1.0', article.publish_date)
    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    # Sentiment Analysis
    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

    title.config(state='disabled')
    author.config(state='disabled')
    date.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

def clear_url():
    utext.delete('1.0', 'end')

# GUI
root = tk.Tk()
root.title("News Filter")
root.geometry('1200x600')

# Row 1: URL Label, URL Text Box, Summarize Button, Clear Button
url_label = tk.Label(root, text='URL')
url_label.grid(row=0, column=0, padx=10, pady=5)

utext = tk.Text(root, height=1, width=60)
utext.grid(row=0, column=1, padx=10, pady=5)

btn_summarize = tk.Button(root, text="Summarize", command=summarize)
btn_summarize.grid(row=0, column=2, padx=10, pady=5)

btn_clear = tk.Button(root, text="Clear", command=clear_url)
btn_clear.grid(row=0, column=3, padx=10, pady=5)

# Row 2: Title Label, Title Text Box
title_label = tk.Label(root, text='Title')
title_label.grid(row=1, column=0, padx=10, pady=5)

title = tk.Text(root, height=1, width=60)
title.config(state='disabled', bg='#dddddd')
title.grid(row=1, column=1, padx=10, pady=5)

# Row 3: Author Label, Author Text Box
author_label = tk.Label(root, text='Author')
author_label.grid(row=2, column=0, padx=10, pady=5)

author = tk.Text(root, height=1, width=60)
author.config(state='disabled', bg='#dddddd')
author.grid(row=2, column=1, padx=10, pady=5)

# Row 4: Publishing Date Label, Publishing Date Text Box
date_label = tk.Label(root, text='Publishing Date')
date_label.grid(row=3, column=0, padx=10, pady=5)

date = tk.Text(root, height=1, width=60)
date.config(state='disabled', bg='#dddddd')
date.grid(row=3, column=1, padx=10, pady=5)

# Row 5: Summary Label, Summary Text Box
summary_label = tk.Label(root, text='Summary')
summary_label.grid(row=4, column=0, padx=10, pady=5)

summary = tk.Text(root, height=10, width=60)
summary.config(state='disabled', bg='#dddddd')
summary.grid(row=4, column=1, padx=10, pady=5)

# Row 6: Sentiment Analysis Label, Sentiment Analysis Text Box
sentiment_label = tk.Label(root, text='Sentiment Analysis')
sentiment_label.grid(row=5, column=0, padx=10, pady=5)

sentiment = tk.Text(root, height=1, width=60)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.grid(row=5, column=1, padx=10, pady=5)

root.mainloop()
