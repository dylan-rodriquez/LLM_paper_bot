# LLM Paper Curation System

An automated system that discovers, analyzes, and organizes the most promising Large Language Model (LLM) research papers daily.

## Features

- **Automated Discovery**: Scans arXiv and other sources for new LLM papers
- **Intelligent Scoring**: Uses Google Gemma to evaluate paper significance
- **Smart Organization**: Categorizes papers into subject-specific folders
- **Daily Updates**: Runs automatically or on-demand via GitHub Actions
- **PR Integration**: Creates pull requests with detailed annotations

## Paper Categories

Papers are automatically organized into:

- **Architectures**: Model designs, attention mechanisms, transformers
- **Training**: Learning methods, optimization, fine-tuning
- **Multimodal**: Vision, audio, cross-modal capabilities
- **Reasoning**: Logic, inference, problem-solving
- **Alignment**: Safety, ethics, human feedback
- **Efficiency**: Compression, quantization, acceleration
- **Evaluation**: Benchmarks, metrics, testing
- **Applications**: Real-world deployment, tools
- **Theoretical**: Mathematical analysis, complexity
- **Agents**: Autonomous systems, planning
- **Generation**: Text synthesis, creativity
- **Knowledge**: Retrieval, memory, factual reasoning

## Configuration

### Workflow Inputs
- `days_back`: Number of days to look back for papers (default: 1)
- `min_score`: Minimum significance score threshold (default: 70)

### Environment Variables
Set these in your GitHub repository settings:
- `GITHUB_TOKEN`: Automatically provided by GitHub Actions

## Usage

### Automatic Daily Run
The workflow runs automatically at 9 AM UTC daily.

### Manual Trigger
1. Go to Actions tab in your GitHub repository
2. Select "LLM Paper Curation" workflow
3. Click "Run workflow"
4. Optionally adjust parameters

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export DAYS_BACK=3
export MIN_SCORE=75

# Run the curation script
python .github/scripts/curate_papers.py
```

## 📋 Output Structure

```
papers/
├── architectures/
│   ├── README.md
│   ├── metadata.json
│   └── [paper-id].md
├── training/
│   ├── README.md
│   ├── metadata.json
│   └── [paper-id].md
└── [other-categories]/
```

Each paper gets:
- Individual markdown file with full analysis
- Entry in category metadata.json
- Link in category README.md

## How It Works

1. **Paper Discovery**: Fetches from arXiv API and RSS feeds
2. **Deduplication**: Removes duplicates based on URL and content hash
3. **Analysis**: Queries Gemma to evaluate and summarize findings
4. **Classification**: Categorizes into subject areas using Gemma
5. **Filtering**: Only includes papers above significance threshold
6. **Organization**: Creates structured file system with metadata
7. **PR Creation**: Generates pull request with detailed summary

## 🎯 Customization

### Adding New Categories
Edit the `subject_categories` dictionary in `curate_papers.py`:

```python
self.subject_categories = {
    "your_category": ["keyword1", "keyword2", "keyword3"],
    # ... existing categories
}
```

### Adding New Data Sources
Extend the `fetch_papers_with_rss()` method with additional RSS feeds or APIs.

## 🔍 Quality Assurance

The system includes multiple quality checks:
- Duplicate detection across sources
- Minimum score thresholds
- Content validation
- Error handling and logging
- Manual review via pull requests

## Troubleshooting

### Common Issues

**No papers found**: 
- Check if arXiv is accessible
- Verify date range settings
- Lower the minimum score threshold

**Workflow fails**:
- Check GitHub Actions logs
- Verify repository permissions
- Ensure all required files are present

**Categories not working**:
- Review keyword lists in subject_categories
- Check paper classification logic
- Verify directory creation permissions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally
5. Submit a pull request
