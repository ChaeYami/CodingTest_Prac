from collections import Counter
from datetime import datetime

def count_by_category_and_month(log_file_path):
    category_list = []
    month_counter = Counter()
    total_files_count = 0

    with open(log_file_path, 'r', encoding='cp949') as log_file:
        next(log_file)  # 헤더를 건너뛰기
        for line in log_file:
            # 'created_at' 문자열을 기준으로 나누고 오른쪽 부분을 선택하여 사용
            created_at_str = line.split('created_at : ')[1].strip()
            created_at = datetime.strptime(created_at_str, "%Y-%m-%d %H:%M:%S.%f")

            # [] 안의 글자로 묶어서 갯수 세기
            category = line[line.find('[')+1:line.find(']')]
            category_list.append(category)
            category_counter = sorted(Counter(category_list).items(), key=lambda x: -x[1])

            # 년-월로 묶어서 갯수 세기
            month = created_at.strftime("%Y-%m")
            month_counter[month] += 1

            total_files_count += 1
            
            month_files = sorted(month_counter.items(), key=lambda x: (int(x[0][:4]), int(x[0][5:])))

    return category_counter, month_files, total_files_count


def make_count_site_info(total_files_count, category_counter):
    count_info = f"## 해결한 문제 : {total_files_count}개\n"

    for name in category_counter:
        temp = f"#### {name[0]} - {name[1]}개\n"
        count_info += temp

    return count_info


def make_count_month_info(month_files):
    month_info = f"### 날짜별 해결한 문제 \n"
    
    for month_year, count in month_files:
        formatted_month_year = datetime.strptime(month_year, "%Y-%m").strftime("%b-%Y")
        
        temp = f"#### {formatted_month_year} : {count}개\n"
        month_info += temp
        
    return month_info

def make_read_me(count_info, month_info):
    return f"""# ⭐ 코딩테스트 연습 ( CODINGTEST PRACTICE ) ⭐
{count_info}
{month_info}
"""

def update_readme_md():
    log_file_path = "./file_log.txt"  # 로그 파일 경로
    
    category_counter, month_files, total_files_count = count_by_category_and_month(log_file_path)
    count_info = make_count_site_info(total_files_count=total_files_count, category_counter=category_counter)

    month_info = make_count_month_info(month_files=month_files)
    
    readme = make_read_me(count_info=count_info, month_info=month_info)

    return readme



    
if __name__ == "__main__":
    readme = update_readme_md()
    with open("./README.md", 'w', encoding='utf-8') as f:
        f.write(readme)