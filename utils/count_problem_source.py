from collections import Counter
from datetime import datetime
import re

def count_by_category_and_month(log_file_path):
    category_list = []
    month_counter = Counter()
    total_files_count = 0

    with open(log_file_path, 'r', encoding='cp949') as log_file:
        next(log_file)  # 헤더를 건너뛰기
        for line in log_file:
            
            file_name, status, created_at_str = re.split(', | : ', line.strip())

            created_at = datetime.strptime(created_at_str, "%Y-%m-%d %H:%M:%S.%f")

            # [] 안의 글자로 묶어서
            category = line[line.find('[')+1:line.find(']')]
            category_list.append(category)
            
            month = created_at.strftime("%Y-%m")
            
            if status == 'created_at':
                month_counter[month] += 1
                total_files_count += 1
                category_counter = Counter(category_list)
            
            elif status == 'deleted_at':
                month_counter[month] -= 1
                total_files_count -= 1
                category_counter[category] -= 1
                
            # 카테고리 개수세기
            category_files = sorted(category_counter.items(), key=lambda x: -x[1])
            
            month_files = sorted(month_counter.items(), key=lambda x: (int(x[0][:4]), int(x[0][5:])))

    return category_files, month_files, total_files_count


def make_count_site_info(total_files_count, category_files):
    count_info = f"## 해결한 문제 : {total_files_count}개\n"

    for name in category_files:
        if name[1] > 0:
            temp = f"#### {name[0]} - {name[1]}개\n"
            count_info += temp

    return count_info


def make_count_month_info(month_files):
    month_info = f"### 날짜별 해결한 문제 \n"
    
    for month_year, count in month_files:
        formatted_month_year = datetime.strptime(month_year, "%Y-%m").strftime("%b-%Y")
        if count > 0:
            temp = f"#### {formatted_month_year} : {count}개\n"
            month_info += temp
        
    return month_info

def make_read_me(count_info, month_info):
    return f"""# ⭐ 코딩테스트 연습 ( CODINGTEST PRACTICE ) ⭐
<div align="center"><img src="https://github.com/ChaeYami/ChaeYami/assets/120750451/7c8742a2-96f5-4f80-948f-fc5fc8afdcd2" width="128"/></div>

{count_info}
{month_info}
"""

def update_readme_md():
    log_file_path = "./file_log.txt"  # 로그 파일 경로
    
    category_files, month_files, total_files_count = count_by_category_and_month(log_file_path)
    count_info = make_count_site_info(total_files_count=total_files_count, category_files=category_files)

    month_info = make_count_month_info(month_files=month_files)
    
    readme = make_read_me(count_info=count_info, month_info=month_info)

    return readme



    
if __name__ == "__main__":
    readme = update_readme_md()
    with open("./README.md", 'w', encoding='utf-8') as f:
        f.write(readme)