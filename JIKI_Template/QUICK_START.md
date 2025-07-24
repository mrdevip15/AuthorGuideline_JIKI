# Quick Start Guide

## Get Started in 5 Minutes

1. **Copy the template**: 
   ```bash
   cp mainTemplate_JIKI.tex my_article.tex
   ```

2. **Edit the basic information**:
   - Change the title in line 447
   - Update author names and affiliations (lines 448-456)
   - Replace the abstract with your own (lines 465-475)
   - Update keywords (line 476)

3. **Write your content**:
   - Replace the Introduction section (starting around line 485)
   - Add your Methodology section
   - Write your Results and Analysis
   - Conclude your paper

4. **Compile your document**:
   ```bash
   pdflatex my_article.tex
   bibtex my_article
   pdflatex my_article.tex
   pdflatex my_article.tex
   ```

## Key Sections to Edit

### Title and Authors (lines 447-456)
```latex
\title{Your Article Title Here}
\author{\IEEEauthorblockN{Your Name\textsuperscript{1}}
\IEEEauthorblockA{\textsuperscript{1}Your Institution}
```

### Abstract (lines 465-475)
```latex
\begin{abstract}
Your abstract here (max 200 words)...
\textbf{Keywords}: keyword1, keyword2, keyword3, keyword4, keyword5
\end{abstract}
```

### Content Sections
- **Introduction**: Start around line 485
- **Methodology**: Add after Introduction
- **Results and Analysis**: Add your findings
- **Conclusion**: Summarize your work

## Important Reminders

- **Page limit**: 6-15 pages
- **Abstract**: Maximum 200 words
- **Keywords**: Up to 5 keywords
- **Title**: Maximum 20 words
- **No bullets or numbering** in lists
- **No subheadings** (discouraged)

## Need Help?

- Check `README.md` for detailed instructions
- Look at `example_article.tex` for a complete example
- Contact: jiki@cs.ui.ac.id 