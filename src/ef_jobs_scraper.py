import requests
import json
from typing import List, Dict, Optional
from pathlib import Path


class EFJobsScraper:
    def __init__(self, base_url: str = "https://careers.ef.com"):
        self.base_url = base_url
        self.api_endpoint = "https://www.ef.com/central-api/careers/job/v2/getjobs/we/?pageIndex=1&pageSize=50&sortColumn=0"
    
    def fetch_jobs(self) -> Optional[List[Dict]]:
        try:
            response = requests.get(self.api_endpoint)
            response.raise_for_status()
            
            data = response.json()
            
            if 'jobs' not in data:
                print("Error: 'jobs' key not found in API response")
                return None
            
            return data['jobs']
            
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None
    
    def process_job(self, job: Dict) -> Dict:
        processed_job = job.copy()
        
        if 'image' in processed_job:
            del processed_job['image']
        
        if 'jobUrl' in processed_job:
            processed_job['job_url'] = self.base_url + processed_job['jobUrl']
        else:
            processed_job['job_url'] = self.base_url
        
        return processed_job
    
    def process_jobs(self, jobs: List[Dict]) -> List[Dict]:
        return [self.process_job(job) for job in jobs]
    
    def save_to_json(self, jobs: List[Dict], filename: str = "ef_jobs.json") -> bool:
        if not jobs:
            print("No data to save")
            return False
        
        try:
            data_to_save = {"jobs": jobs}
            
            output_path = Path("../data") / filename
            output_path.parent.mkdir(exist_ok=True)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(data_to_save, f, ensure_ascii=False, indent=2)
            
            print(f"Successfully saved {len(jobs)} jobs to {output_path}")
            return True
            
        except Exception as e:
            print(f"Error saving file: {e}")
            return False
    
    def run(self) -> bool:
        print("Starting to fetch jobs from careers.ef.com...")
        
        jobs = self.fetch_jobs()
        if not jobs:
            print("Failed to fetch jobs")
            return False
        
        print(f"Retrieved {len(jobs)} jobs")
        
        processed_jobs = self.process_jobs(jobs)
        
        if self.save_to_json(processed_jobs):
            print("Task completed successfully!")
            return True
        else:
            print("Error saving file")
            return False


def main():
    scraper = EFJobsScraper()
    scraper.run()


if __name__ == "__main__":
    main()

