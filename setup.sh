#!/bin/bash
# Setup script for LLM Paper Curation Project

# Create directory structure
mkdir -p .github/workflows
mkdir -p .github/scripts
mkdir -p papers

# Create the main workflow file (already provided above)
# Create the main curation script (already provided above)

# Create requirements.txt for local development
cat > requirements.txt << 'EOF'
requests>=2.31.0
beautifulsoup4>=4.12.0
feedparser>=6.0.10
nltk>=3.8.1
scikit-learn>=1.3.0
pandas>=2.0.0
numpy>=1.24.0
python-dateutil>=2.8.2
markdown>=3.5.0
EOF

# Create .gitignore
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual environments
venv/
ENV/
env/
.venv/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Temporary files
*.tmp
*.temp
.cache/

# NLTK data (downloaded at runtime)
nltk_data/
EOF

# Create main README
cat > README.md << 'EOF'
# 🤖 LLM Paper Curation System

An automated system that discovers, analyzes, and organizes the most promising Large Language Model (LLM) research papers daily.

## 🌟 Features

- **Automated Discovery**: Scans arXiv and other sources for new LLM papers
- **Intelligent Scoring**: Uses multi-criteria analysis to evaluate paper significance
- **Smart Organization**: Categorizes papers into subject-specific folders
- **No External APIs**: Uses local sentiment analysis and NLP techniques
- **Daily Updates**: Runs automatically or on-demand via GitHub Actions
- **PR Integration**: Creates pull requests with detailed annotations

## 📊 Evaluation Criteria

Papers are scored on multiple dimensions:

### Innovation Score (30% weight)
- Novel methods and approaches
- Breakthrough techniques
- State-of-the-art improvements

### Impact Score (25% weight)  
- Real-world applications
- Industry relevance
- Practical significance

### Technical Quality (25% weight)
- Mathematical rigor
- Comprehensive analysis
- Methodological soundness

### Sentiment Analysis (20% weight)
- Positive language indicators
- Confidence markers
- Reception signals

## 📁 Paper Categories

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

## 🚀 Setup

1. **Enable GitHub Actions** in your repository
2. **Set up the workflow** by copying the files to:
   - `.github/workflows/llm-curation.yml`
   - `.github/scripts/curate_papers.py`
3. **Configure permissions** for the workflow to create PRs
4. **Customize settings** in the workflow file if needed

## 🔧 Configuration

### Workflow Inputs
- `days_back`: Number of days to look back for papers (default: 1)
- `min_score`: Minimum significance score threshold (default: 70)

### Environment Variables
Set these in your GitHub repository settings:
- `GITHUB_TOKEN`: Automatically provided by GitHub Actions

## 📅 Usage

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

## 🤖 How It Works

1. **Paper Discovery**: Fetches from arXiv API and RSS feeds
2. **Deduplication**: Removes duplicates based on URL and content hash
3. **Analysis**: Applies multi-criteria scoring algorithm
4. **Classification**: Categorizes into subject areas using keyword matching
5. **Filtering**: Only includes papers above significance threshold
6. **Organization**: Creates structured file system with metadata
7. **PR Creation**: Generates pull request with detailed summary

## 📈 Scoring Algorithm

```python
significance_score = (
    innovation_score * 0.30 +  # Novel approaches
    impact_score * 0.25 +      # Real-world relevance  
    technical_score * 0.25 +   # Technical quality
    sentiment_score * 0.20     # Positive indicators
) + bonus_terms_score
```

## 🎯 Customization

### Adding New Categories
Edit the `subject_categories` dictionary in `curate_papers.py`:

```python
self.subject_categories = {
    "your_category": ["keyword1", "keyword2", "keyword3"],
    # ... existing categories
}
```

### Adjusting Scoring Weights
Modify the scoring algorithm in `analyze_paper_significance()` method.

### Adding New Data Sources
Extend the `fetch_papers_with_rss()` method with additional RSS feeds or APIs.

## 🔍 Quality Assurance

The system includes multiple quality checks:
- Duplicate detection across sources
- Minimum score thresholds
- Content validation
- Error handling and logging
- Manual review via pull requests

## 📊 Analytics

Each run generates:
- Summary statistics in PR description  
- Category distribution analysis
- Score distribution metrics
- Trend analysis over time

## 🛠️ Troubleshooting

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

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally
5. Submit a pull request

## 📄 License

This project is open source. Feel free to adapt and modify for your needs.

## 🙏 Acknowledgments

- arXiv for providing open access to research papers
- NLTK for natural language processing tools
- scikit-learn for machine learning utilities
- The research community for advancing LLM science

---

*Last updated: $(date +'%Y-%m-%d')*
EOF

echo "Project structure created successfully!"
echo ""
echo "Next steps:"
echo "1. Copy the workflow file to .github/workflows/llm-curation.yml"
echo "2. Copy the Python script to .github/scripts/curate_papers.py"  
echo "3. Commit and push to enable the automated workflow"
echo "4. Check the Actions tab to monitor the first run"
