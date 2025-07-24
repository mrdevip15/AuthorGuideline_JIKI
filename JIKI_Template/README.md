# JIKI LaTeX Template

This folder contains all necessary files to create articles for **Jurnal Ilmu Komputer dan Informasi (Journal of Computer Science and Information)** using LaTeX.

## Files Included

### Core Template Files
- `mainTemplate_JIKI.tex` - Main template file (start here!)
- `IEEEtran.cls` - IEEE LaTeX class file
- `README.md` - This file

### Bibliography Files
- `IEEEabrv.bib` - IEEE abbreviations
- `IEEEexample.bib` - Example references

### Style Files
- `balance.sty` - Column balancing
- `caption.sty` - Caption formatting
- `cite.sty` - Citation formatting
- `import.sty` - Import functionality
- `algorithm2e.sty` - Algorithm formatting

### Graphics
- `pics/` - Folder containing example images

## How to Use

1. **Start with the template**: Copy `mainTemplate_JIKI.tex` to your working directory
2. **Rename it**: Give it a meaningful name like `my_article.tex`
3. **Edit the content**: Replace the example content with your own
4. **Compile**: Use LaTeX to generate PDF

## Template Features

### Document Format
- **Paper Size**: A4 (210mm × 297mm)
- **Margins**: 3cm on all sides
- **Font**: Times New Roman, 10pt
- **Spacing**: Single-spaced
- **Layout**: Two-column format

### Required Sections
1. Introduction
2. Methodology
3. Results and Analysis
4. Conclusion
5. References

### Special Formatting
- **Tables**: 8pt font, title above, no vertical lines
- **Figures**: Caption below, 8pt font
- **Equations**: Centered with numbered brackets
- **Code**: Consolas 10pt font, referenced as figures
- **Citations**: Arabic numbers in square brackets [1]

### Length Requirements
- **Pages**: 6-15 pages including graphics and tables
- **Abstract**: Maximum 200 words
- **Keywords**: Up to 5 keywords in English
- **Title**: Maximum 20 words

## Compilation

To compile your document:

```bash
pdflatex your_article.tex
bibtex your_article
pdflatex your_article.tex
pdflatex your_article.tex
```

## Important Notes

- **No bullets or numbering** in lists
- **No subheadings** (discouraged)
- **Abbreviations** must be written in full first time
- **Foreign terms** in italics
- **Balance columns** at the end
- **Widow/orphan control** activated

## Submission

Submit your article to: http://jiki.cs.ui.ac.id
Contact: jiki@cs.ui.ac.id

## Example Usage

1. Copy `mainTemplate_JIKI.tex` to your working directory
2. Rename it to your article name
3. Edit the title, authors, and affiliations
4. Replace the abstract with your own
5. Write your content in the appropriate sections
6. Add your references to the bibliography
7. Compile and check the output

## Troubleshooting

- Make sure all `.sty` files are in the same directory as your `.tex` file
- Ensure the `pics/` folder is accessible for images
- Check that bibliography files are properly referenced
- Verify that all required packages are installed on your LaTeX system 