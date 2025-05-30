#!/usr/bin/env python3
"""
LLM Paper Curation Script
Automatically finds, evaluates, and organizes promising LLM papers.
"""

import os
import re
import json
import time
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, asdict
from urllib.parse import urljoin, urlparse
import hashlib

import requests
import feedparser
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from dateutil import parser as date_parser
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class Paper:
    """Represents a research paper with metadata and analysis."""
    title: str
    authors: List[str]
    abstract: str
    url: str
    published_date: datetime
    source: str
    categories: List[str]
    significance_score: float
    innovation_score: float
    impact_score: float
    sentiment_score: float
    keywords: List[str]
    subject_classification: str
    justification: str
    paper_id: str

class PaperCurator:
    """Main class for curating and organizing LLM papers."""
    
    def __init__(self, days_back: int = 1, min_score: float = 70.0):
        self.days_back = days_back
        self.min_score = min_score
        self.sentiment_analyzer = SentimentIntensityAnalyzer()
        self.papers_dir = Path("papers")
        self.papers_dir.mkdir(exist_ok=True)
        
        # Initialize subject categories
        self.subject_categories = {
            "architectures": ["transformer", "architecture", "attention", "convolution", "rnn", "lstm", "gru"],
            "training": ["training", "learning", "optimization", "gradient", "backprop", "fine-tuning", "rlhf"],
            "multimodal": ["multimodal", "vision", "image", "video", "audio", "speech", "cross-modal"],
            "reasoning": ["reasoning", "logic", "inference", "problem solving", "chain-of-thought", "planning"],
            "alignment": ["alignment", "safety", "ethics", "bias", "fairness", "human feedback", "constitutional"],
            "efficiency": ["efficiency", "compression", "quantization", "pruning", "distillation", "acceleration"],
            "evaluation": ["evaluation", "benchmark", "metric", "assessment", "testing", "measurement"],
            "applications": ["application", "deployment", "real-world", "industry", "production", "tool"],
            "theoretical": ["theory", "theoretical", "mathematical", "analysis", "proof", "complexity"],
            "agents": ["agent", "autonomous", "planning", "tool use", "environment", "embodied"],
            "generation": ["generation", "creativity", "synthesis", "sampling", "decoding", "hallucination"],
            "knowledge": ["knowledge", "retrieval", "memory", "factual", "commonsense", "world model"]
        }
        
        # Load existing papers to avoid duplicates
        self.existing_papers = self._load_existing_papers()
        
    def _load_existing_papers(self) -> set:
        """Load IDs of existing papers to avoid duplicates."""
        existing = set()
        for category_dir in self.papers_dir.iterdir():
            if category_dir.is_dir():
                metadata_file = category_dir / "metadata.json"
                if metadata_file.exists():
                    try:
                        with open(metadata_file, 'r') as f:
                            data = json.load(f)
                            for paper in data.get('papers', []):
                                existing.add(paper.get('paper_id', ''))
                    except Exception as e:
                        logger.warning(f"Error loading metadata from {metadata_file}: {e}")
        return existing
    
    def fetch_arxiv_papers(self, query: str = None) -> List[Dict]:
        """Fetch recent papers from arXiv API."""
        if query is None:
            # Comprehensive LLM-related query
            query = ('cat:cs.CL OR cat:cs.AI OR cat:cs.LG OR cat:stat.ML) AND '
                    '(ti:"language model" OR ti:"transformer" OR ti:"GPT" OR ti:"BERT" OR '
                    'ti:"neural network" OR ti:"deep learning" OR ti:"machine learning" OR '
                    'ti:"artificial intelligence" OR ti:"natural language" OR ti:"LLM" OR '
                    'ti:"large language" OR abs:"language model" OR abs:"LLM")')
        
        base_url = "http://export.arxiv.org/api/query"
        start_date = datetime.now() - timedelta(days=self.days_back)
        
        params = {
            'search_query': query,
            'start': 0,
            'max_results': 100,
            'sortBy': 'submittedDate',
            'sortOrder': 'descending'
        }
        
        try:
            response = requests.get(base_url, params=params, timeout=30)
            response.raise_for_status()
            
            feed = feedparser.parse(response.content)
            papers = []
            
            for entry in feed.entries:
                published = date_parser.parse(entry.published)
                if published >= start_date:
                    papers.append({
                        'title': entry.title,
                        'authors': [author.name for author in entry.authors],
                        'abstract': entry.summary,
                        'url': entry.link,
                        'published_date': published,
                        'source': 'arXiv',
                        'categories': [tag.term for tag in entry.tags]
                    })
            
            logger.info(f"Fetched {len(papers)} papers from arXiv")
            return papers
            
        except Exception as e:
            logger.error(f"Error fetching arXiv papers: {e}")
            return []
    
    def fetch_papers_with_rss(self) -> List[Dict]:
        """Fetch papers from various RSS feeds."""
        feeds = [
            "http://export.arxiv.org/rss/cs.CL",  # Computation and Language
            "http://export.arxiv.org/rss/cs.AI",  # Artificial Intelligence
            "http://export.arxiv.org/rss/cs.LG",  # Machine Learning
        ]
        
        all_papers = []
        start_date = datetime.now() - timedelta(days=self.days_back)
        
        for feed_url in feeds:
            try:
                feed = feedparser.parse(feed_url)
                for entry in feed.entries:
                    published = date_parser.parse(entry.published)
                    if published.tzinfo is not None:
                        published = published.replace(tzinfo=None)
                    if published >= start_date:
                        all_papers.append({
                            'title': entry.title,
                            'authors': [entry.get('author', 'Unknown')],
                            'abstract': entry.get('summary', ''),
                            'url': entry.link,
                            'published_date': published,
                            'source': 'arXiv RSS',
                            'categories': [entry.get('category', 'cs.CL')]
                        })
                        
                time.sleep(1)  # Rate limiting
                
            except Exception as e:
                logger.warning(f"Error fetching from {feed_url}: {e}")
        
        logger.info(f"Fetched {len(all_papers)} papers from RSS feeds")
        return all_papers
    
    def analyze_paper_significance(self, paper_data: Dict) -> Tuple[float, float, float, float, str]:
        """Analyze paper significance using multiple criteria."""
        title = paper_data['title'].lower()
        abstract = paper_data['abstract'].lower()
        text = f"{title} {abstract}"
        
        # Innovation score based on keywords
        innovation_keywords = [
            'novel', 'new', 'first', 'breakthrough', 'revolutionary', 'unprecedented',
            'innovative', 'original', 'pioneering', 'cutting-edge', 'state-of-the-art',
            'advances', 'improves', 'outperforms', 'surpasses', 'exceeds'
        ]
        innovation_score = sum(1 for kw in innovation_keywords if kw in text) * 10
        innovation_score = min(innovation_score, 100)
        
        # Impact score based on scope and applications
        impact_keywords = [
            'significant', 'substantial', 'major', 'important', 'critical', 'fundamental',
            'comprehensive', 'extensive', 'large-scale', 'real-world', 'practical',
            'industry', 'deployment', 'production', 'applications'
        ]
        impact_score = sum(1 for kw in impact_keywords if kw in text) * 8
        impact_score = min(impact_score, 100)
        
        # Technical sophistication
        technical_keywords = [
            'algorithm', 'method', 'approach', 'technique', 'framework', 'architecture',
            'model', 'system', 'analysis', 'theoretical', 'mathematical', 'optimization'
        ]
        technical_score = sum(1 for kw in technical_keywords if kw in text) * 5
        technical_score = min(technical_score, 100)
        
        # Sentiment analysis
        sentiment = self.sentiment_analyzer.polarity_scores(abstract)
        sentiment_score = (sentiment['pos'] - sentiment['neg']) * 50 + 50
        
        # Combine scores with weights
        significance_score = (
            innovation_score * 0.3 +
            impact_score * 0.25 +
            technical_score * 0.25 +
            sentiment_score * 0.2
        )
        
        # Bonus for certain high-impact terms
        bonus_terms = ['gpt', 'bert', 'transformer', 'attention', 'llm', 'large language']
        bonus = sum(5 for term in bonus_terms if term in text)
        significance_score += bonus
        
        significance_score = min(significance_score, 100)
        
        # Generate justification
        justification_parts = []
        if innovation_score > 20:
            justification_parts.append(f"High innovation indicators (score: {innovation_score})")
        if impact_score > 20:
            justification_parts.append(f"Strong impact potential (score: {impact_score})")
        if technical_score > 30:
            justification_parts.append(f"Technical sophistication (score: {technical_score})")
        if sentiment_score > 60:
            justification_parts.append(f"Positive sentiment analysis (score: {sentiment_score:.1f})")
        if bonus > 0:
            justification_parts.append(f"Contains key LLM terms (bonus: {bonus})")
        
        justification = "; ".join(justification_parts) if justification_parts else "Standard evaluation criteria"
        
        return significance_score, innovation_score, impact_score, sentiment_score, justification
    
    def classify_subject(self, paper_data: Dict) -> str:
        """Classify paper into subject category."""
        text = f"{paper_data['title']} {paper_data['abstract']}".lower()
        
        category_scores = {}
        for category, keywords in self.subject_categories.items():
            score = sum(1 for kw in keywords if kw in text)
            if score > 0:
                category_scores[category] = score
        
        if category_scores:
            return max(category_scores, key=category_scores.get)
        else:
            return "general"
    
    def extract_keywords(self, text: str, max_keywords: int = 10) -> List[str]:
        """Extract key terms from paper text."""
        # Simple keyword extraction using TF-IDF
        vectorizer = TfidfVectorizer(
            max_features=100,
            stop_words='english',
            ngram_range=(1, 2),
            min_df=1
        )
        
        try:
            tfidf_matrix = vectorizer.fit_transform([text])
            feature_names = vectorizer.get_feature_names_out()
            scores = tfidf_matrix.toarray()[0]
            
            # Get top keywords
            keyword_scores = list(zip(feature_names, scores))
            keyword_scores.sort(key=lambda x: x[1], reverse=True)
            
            return [kw for kw, score in keyword_scores[:max_keywords] if score > 0]
        except:
            # Fallback to simple word frequency
            words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
            word_freq = {}
            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1
            
            return sorted(word_freq, key=word_freq.get, reverse=True)[:max_keywords]
    
    def process_papers(self, paper_data_list: List[Dict]) -> List[Paper]:
        """Process raw paper data into Paper objects."""
        papers = []
        
        for paper_data in paper_data_list:
            try:
                # Generate unique paper ID
                paper_id = hashlib.md5(
                    f"{paper_data['title']}{paper_data['url']}".encode()
                ).hexdigest()
                
                # Skip if already exists
                if paper_id in self.existing_papers:
                    continue
                
                # Analyze significance
                significance_score, innovation_score, impact_score, sentiment_score, justification = \
                    self.analyze_paper_significance(paper_data)
                
                # Skip papers below threshold
                if significance_score < self.min_score:
                    continue
                
                # Classify subject
                subject = self.classify_subject(paper_data)
                
                # Extract keywords
                text = f"{paper_data['title']} {paper_data['abstract']}"
                keywords = self.extract_keywords(text)
                
                paper = Paper(
                    title=paper_data['title'],
                    authors=paper_data['authors'],
                    abstract=paper_data['abstract'],
                    url=paper_data['url'],
                    published_date=paper_data['published_date'],
                    source=paper_data['source'],
                    categories=paper_data.get('categories', []),
                    significance_score=significance_score,
                    innovation_score=innovation_score,
                    impact_score=impact_score,
                    sentiment_score=sentiment_score,
                    keywords=keywords,
                    subject_classification=subject,
                    justification=justification,
                    paper_id=paper_id
                )
                
                papers.append(paper)
                
            except Exception as e:
                logger.error(f"Error processing paper {paper_data.get('title', 'Unknown')}: {e}")
        
        return papers
    
    def organize_papers(self, papers: List[Paper]) -> Dict[str, List[Paper]]:
        """Organize papers by subject category."""
        organized = {}
        for paper in papers:
            category = paper.subject_classification
            if category not in organized:
                organized[category] = []
            organized[category].append(paper)
        
        # Sort papers within each category by significance score
        for category in organized:
            organized[category].sort(key=lambda p: p.significance_score, reverse=True)
        
        return organized
    
    def save_papers(self, organized_papers: Dict[str, List[Paper]]) -> List[str]:
        """Save organized papers to filesystem."""
        added_files = []
        pr_content = []
        
        for category, papers in organized_papers.items():
            if not papers:
                continue
                
            category_dir = self.papers_dir / category
            category_dir.mkdir(exist_ok=True)
            
            # Load existing metadata
            metadata_file = category_dir / "metadata.json"
            existing_metadata = {"papers": [], "last_updated": ""}
            
            if metadata_file.exists():
                try:
                    with open(metadata_file, 'r') as f:
                        existing_metadata = json.load(f)
                except Exception as e:
                    logger.warning(f"Error loading existing metadata: {e}")
            
            # Add new papers
            new_papers_added = []
            for paper in papers:
                paper_dict = asdict(paper)
                paper_dict['published_date'] = paper.published_date.isoformat()
                existing_metadata["papers"].append(paper_dict)
                new_papers_added.append(paper)
                
                # Create individual paper file
                paper_file = category_dir / f"{paper.paper_id}.md"
                self._create_paper_markdown(paper, paper_file)
                added_files.append(str(paper_file))
            
            # Update metadata
            existing_metadata["last_updated"] = datetime.now().isoformat()
            
            with open(metadata_file, 'w') as f:
                json.dump(existing_metadata, f, indent=2)
            added_files.append(str(metadata_file))
            
            # Update category README
            readme_file = category_dir / "README.md"
            self._create_category_readme(category, existing_metadata["papers"], readme_file)
            added_files.append(str(readme_file))
            
            # Add to PR content
            if new_papers_added:
                pr_content.append(f"\n## {category.title()} ({len(new_papers_added)} new papers)")
                for paper in new_papers_added:
                    pr_content.append(f"- **{paper.title}** (Score: {paper.significance_score:.1f})")
                    pr_content.append(f"  - {paper.justification}")
        
        # Create PR body
        self._create_pr_body(organized_papers, pr_content)
        
        return added_files
    
    def _create_paper_markdown(self, paper: Paper, filepath: Path):
        """Create markdown file for individual paper."""
        content = f"""# {paper.title}

**Authors:** {', '.join(paper.authors)}

**Published:** {paper.published_date.strftime('%Y-%m-%d')} | **Source:** {paper.source}

**Categories:** {', '.join(paper.categories)}

**Significance Score:** {paper.significance_score:.1f}/100

## Abstract

{paper.abstract}

## Analysis

**Innovation Score:** {paper.innovation_score:.1f}/100
**Impact Score:** {paper.impact_score:.1f}/100  
**Sentiment Score:** {paper.sentiment_score:.1f}/100

**Justification:** {paper.justification}

## Keywords

{', '.join(paper.keywords)}

## Links

- [Paper URL]({paper.url})

---
*Auto-generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC*
"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def _create_category_readme(self, category: str, all_papers: List[Dict], filepath: Path):
        """Create README for paper category."""
        content = f"""# {category.title()} Papers

This directory contains papers related to {category} in large language models and AI.

## Papers ({len(all_papers)} total)

"""
        
        # Sort by significance score
        sorted_papers = sorted(all_papers, key=lambda p: p['significance_score'], reverse=True)
        
        for paper in sorted_papers:
            pub_date = paper['published_date'][:10] if isinstance(paper['published_date'], str) else paper['published_date'].strftime('%Y-%m-%d')
            content += f"### {paper['title']}\n\n"
            content += f"**Score:** {paper['significance_score']:.1f} | **Published:** {pub_date} | **Authors:** {', '.join(paper['authors'])}\n\n"
            content += f"{paper['abstract'][:200]}...\n\n"
            content += f"[📄 Full Paper]({paper['url']}) | [📝 Analysis]({paper['paper_id']}.md)\n\n"
            content += "---\n\n"
        
        content += f"\n*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC*\n"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def _create_pr_body(self, organized_papers: Dict[str, List[Paper]], content_lines: List[str]):
        """Create pull request body with summary."""
        total_papers = sum(len(papers) for papers in organized_papers.values())
        avg_score = np.mean([p.significance_score for papers in organized_papers.values() for p in papers])
        
        pr_body = f"""# 📚 Daily LLM Paper Curation Summary

## Overview
- **Total Papers Added:** {total_papers}
- **Average Significance Score:** {avg_score:.1f}/100
- **Categories Updated:** {len(organized_papers)}
- **Date Range:** Last {self.days_back} day(s)

## Selection Criteria
Papers are automatically selected based on:
- **Innovation Score:** Novel methods, breakthrough approaches
- **Impact Score:** Practical applications, real-world significance  
- **Technical Quality:** Mathematical rigor, comprehensive analysis
- **Sentiment Analysis:** Positive reception indicators
- **Minimum Threshold:** {self.min_score}/100 significance score

## Papers Added
"""
        
        pr_body += '\n'.join(content_lines)
        
        pr_body += f"""

## Categories
{', '.join(f'**{cat.title()}** ({len(papers)})' for cat, papers in organized_papers.items())}

---
*This PR was automatically generated by the LLM Paper Curation workflow*
*Review the papers and merge if the selection looks appropriate*
"""
        
        with open('.github/pr_body.md', 'w') as f:
            f.write(pr_body)

def main():
    """Main execution function."""
    days_back = int(os.environ.get('DAYS_BACK', 1))
    min_score = float(os.environ.get('MIN_SCORE', 70))
    
    logger.info(f"Starting paper curation (days_back={days_back}, min_score={min_score})")
    
    curator = PaperCurator(days_back=days_back, min_score=min_score)
    
    # Fetch papers from multiple sources
    all_paper_data = []
    all_paper_data.extend(curator.fetch_arxiv_papers())
    all_paper_data.extend(curator.fetch_papers_with_rss())
    
    # Remove duplicates based on URL
    seen_urls = set()
    unique_papers = []
    for paper in all_paper_data:
        if paper['url'] not in seen_urls:
            unique_papers.append(paper)
            seen_urls.add(paper['url'])
    
    logger.info(f"Found {len(unique_papers)} unique papers")
    
    # Process and analyze papers
    processed_papers = curator.process_papers(unique_papers)
    logger.info(f"Processed {len(processed_papers)} papers meeting criteria")
    
    if processed_papers:
        # Organize by subject
        organized_papers = curator.organize_papers(processed_papers)
        
        # Save to filesystem
        added_files = curator.save_papers(organized_papers)
        logger.info(f"Added {len(added_files)} files")
        
        # Print summary
        for category, papers in organized_papers.items():
            logger.info(f"{category}: {len(papers)} papers")
    else:
        logger.info("No papers met the significance criteria")

if __name__ == "__main__":
    main()
