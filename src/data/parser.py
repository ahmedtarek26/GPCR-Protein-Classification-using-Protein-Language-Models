"""
FASTA File Parser for GPCR Sequences
Parses aligned protein sequences from FASTA format
"""

from Bio import SeqIO
import pandas as pd
from pathlib import Path
from typing import List, Dict, Tuple
import re


class GPCRFastaParser:
    """Parser for GPCR FASTA alignment files"""

    def __init__(self, fasta_path: str):
        """
        Initialize parser with FASTA file path

        Args:
            fasta_path: Path to FASTA file
        """
        self.fasta_path = Path(fasta_path)
        if not self.fasta_path.exists():
            raise FileNotFoundError(f"FASTA file not found: {fasta_path}")

    def parse(self) -> pd.DataFrame:
        """
        Parse FASTA file and extract sequences

        Returns:
            DataFrame with columns: id, uniref_id, sequence, length, gap_count, gap_percentage
        """
        sequences_data = []

        print(f"Parsing {self.fasta_path}...")

        for record in SeqIO.parse(self.fasta_path, "fasta"):
            # Extract UniRef ID from header
            header = record.description
            seq_id = record.id
            uniref_id = self._extract_uniref_id(header)

            # Get sequence information
            sequence = str(record.seq)
            length = len(sequence)
            gap_count = sequence.count('-')
            gap_percentage = (gap_count / length) * 100 if length > 0 else 0

            sequences_data.append({
                'id': seq_id,
                'uniref_id': uniref_id,
                'full_header': header,
                'sequence': sequence,
                'length': length,
                'gap_count': gap_count,
                'gap_percentage': round(gap_percentage, 2)
            })

        df = pd.DataFrame(sequences_data)
        print(f"✅ Parsed {len(df)} sequences")
        print(f"   Average length: {df['length'].mean():.0f} aa")
        print(f"   Average gaps: {df['gap_percentage'].mean():.1f}%")

        return df

    def _extract_uniref_id(self, header: str) -> str:
        """
        Extract UniRef ID from FASTA header

        Args:
            header: FASTA header line

        Returns:
            UniRef ID (e.g., 'UPI0002747C2C')
        """
        # Pattern: UniRef100_UPIXXXXXXXXX
        match = re.search(r'UniRef\d+_([A-Z0-9]+)', header)
        if match:
            return match.group(1)

        # Fallback: just take first part after >
        return header.split()[0].replace('>', '')

    def get_sequence_by_id(self, df: pd.DataFrame, uniref_id: str) -> str:
        """Get sequence by UniRef ID"""
        result = df[df['uniref_id'] == uniref_id]
        if len(result) == 0:
            raise ValueError(f"UniRef ID not found: {uniref_id}")
        return result.iloc[0]['sequence']

    def remove_gaps(self, sequence: str) -> str:
        """Remove gap characters from sequence"""
        return sequence.replace('-', '')

    def get_statistics(self, df: pd.DataFrame) -> Dict:
        """
        Calculate statistics about the sequences

        Returns:
            Dictionary with statistics
        """
        stats = {
            'total_sequences': len(df),
            'avg_length': df['length'].mean(),
            'min_length': df['length'].min(),
            'max_length': df['length'].max(),
            'avg_gap_percentage': df['gap_percentage'].mean(),
            'sequences_with_gaps': (df['gap_count'] > 0).sum(),
        }
        return stats


def main():
    """Example usage"""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python parser.py <fasta_file>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    parser = GPCRFastaParser(fasta_file)

    # Parse sequences
    df = parser.parse()

    # Save to CSV
    output_path = Path('data/processed/sequences_parsed.csv')
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"\n💾 Saved to {output_path}")

    # Print statistics
    stats = parser.get_statistics(df)
    print("\n📊 Statistics:")
    for key, value in stats.items():
        print(f"   {key}: {value}")

    # Show first few sequences
    print("\n🔍 First 3 sequences:")
    print(df[['uniref_id', 'length', 'gap_percentage']].head(3))


if __name__ == '__main__':
    main()