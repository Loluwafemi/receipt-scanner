from dataclasses import dataclass, astuple
from pydantic import BaseModel


class RecieptResponseOutput(BaseModel):
    name: str | None
    bank: str | None
    amount: str | None
    date: str | None
    status: bool


date_patterns = [
    # DD/MM/YYYY, DD-MM-YYYY, DD.MM.YYYY
    r'\b\d{1,2}[/\-\.]\d{1,2}[/\-\.]\d{4}\b',
    
    # MM/DD/YYYY, MM-DD-YYYY, MM.DD.YYYY  
    r'\b\d{1,2}[/\-\.]\d{1,2}[/\-\.]\d{4}\b',
    
    # YYYY/MM/DD, YYYY-MM-DD, YYYY.MM.DD
    r'\b\d{4}[/\-\.]\d{1,2}[/\-\.]\d{1,2}\b',
    
    # DD/MM/YY, DD-MM-YY, DD.MM.YY
    r'\b\d{1,2}[/\-\.]\d{1,2}[/\-\.]\d{2}\b',
    
    # Month DD, YYYY (e.g., January 15, 2024)
    r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+\d{4}\b',
    
    # DD Month YYYY (e.g., 15 January 2024)
    r'\b\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}\b',
    
    # Mon DD, YYYY (e.g., Jan 15, 2024)
    r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\.?\s+\d{1,2},?\s+\d{4}\b',
    
    # DD Mon YYYY (e.g., 15 Jan 2024)
    r'\b\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\.?\s+\d{4}\b',
    
    # DDMMYYYY (no separators)
    r'\b\d{8}\b',
    
    # DD-Mon-YYYY (e.g., 15-Jan-2024)
    r'\b\d{1,2}-(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)-\d{4}\b',
    
    # ISO format: YYYY-MM-DDTHH:MM:SS or YYYY-MM-DD HH:MM:SS
    r'\b\d{4}-\d{2}-\d{2}[T\s]\d{2}:\d{2}:\d{2}\b',
    
    # YYYY-MM-DD (simple ISO date)
    r'\b\d{4}-\d{2}-\d{2}\b'
]